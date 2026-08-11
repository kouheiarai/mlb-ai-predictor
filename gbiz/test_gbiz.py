"""Tests for the gBizINFO pipeline.

Every test runs offline against fixtures shaped like the real API responses, so
the pipeline can be verified before an API token exists.

    python -m unittest gbiz.test_gbiz -v
"""

from __future__ import annotations

import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path

from .client import EVENT_KINDS, GBizClient, GBizError
from .main import build_signal
from .normalize import flatten_records, normalize_amount, normalize_date
from .probe import month_bounds, recent_months
from .store import EventStore

# Shaped after HojinInfoUpdateInfoResponseForChildV2 / SubsidyInfoV2.
SUBSIDY_PAGE = {
    "message": "OK",
    "totalCount": "2",
    "totalPage": "1",
    "pageNumber": "1",
    "hojin-infos": [
        {
            "corporate_number": "1000012070001",
            "name": "テスト株式会社",
            "location": "東京都千代田区霞が関一丁目",
            "subsidy": [
                {
                    "title": "ものづくり補助金",
                    "amount": "10,000,000",
                    "date_of_approval": "2026-07-15",
                    "government_departments": "経済産業省",
                    "target": "中小企業",
                    "meta-data": {
                        "source": "経済産業省",
                        "import_frequency": "毎月",
                        "last_update_date": "20260801",
                    },
                },
                {
                    "title": "事業再構築補助金",
                    "amount": "5000000",
                    "date_of_approval": "20260720",
                    "government_departments": "経済産業省",
                    "target": "中小企業",
                    "meta-data": {"source": "経済産業省", "import_frequency": "毎月"},
                },
            ],
        },
        {
            "corporate_number": "2000012070002",
            "name": "サンプル合同会社",
            "location": "大阪府大阪市",
            "subsidy": [
                {
                    "title": "IT導入補助金",
                    "amount": None,
                    "date_of_approval": "2026-07-01",
                    "government_departments": "経済産業省",
                    "meta-data": {},
                }
            ],
        },
    ],
}

PROCUREMENT_PAGE = {
    "totalCount": "1",
    "totalPage": "1",
    "hojin-infos": [
        {
            "corporate_number": "1000012070001",
            "name": "テスト株式会社",
            "location": "東京都千代田区",
            "procurement": [
                {
                    "title": "システム更改業務",
                    "amount": 24000000,
                    "date_of_order": "2026-07-10",
                    "government_departments": "デジタル庁",
                    "note": "一般競争入札",
                    "meta-data": {"source": "調達", "import_frequency": "毎週"},
                }
            ],
        }
    ],
}


class NormalizeTest(unittest.TestCase):
    def test_amount_accepts_both_shapes(self):
        self.assertEqual(normalize_amount("10,000,000"), 10_000_000)
        self.assertEqual(normalize_amount(24000000), 24000000)
        self.assertEqual(normalize_amount("5000000"), 5000000)
        self.assertIsNone(normalize_amount(None))
        self.assertIsNone(normalize_amount(""))
        self.assertIsNone(normalize_amount("非公開"))

    def test_date_accepts_both_shapes(self):
        self.assertEqual(normalize_date("2026-07-15"), "2026-07-15")
        self.assertEqual(normalize_date("20260720"), "2026-07-20")
        self.assertIsNone(normalize_date(""))
        self.assertIsNone(normalize_date(None))

    def test_flatten_inverts_the_nesting(self):
        rows = flatten_records(SUBSIDY_PAGE["hojin-infos"], "subsidy")
        # Two corporations, three subsidy events between them.
        self.assertEqual(len(rows), 3)
        first = rows[0]
        self.assertEqual(first["corporate_number"], "1000012070001")
        self.assertEqual(first["name"], "テスト株式会社")
        self.assertEqual(first["event_type"], "subsidy")
        self.assertEqual(first["amount"], 10_000_000)
        self.assertEqual(first["event_date"], "2026-07-15")
        self.assertEqual(first["import_frequency"], "毎月")
        self.assertTrue(first["event_id"])

    def test_event_ids_are_stable_and_distinct(self):
        first = flatten_records(SUBSIDY_PAGE["hojin-infos"], "subsidy")
        second = flatten_records(SUBSIDY_PAGE["hojin-infos"], "subsidy")
        self.assertEqual([r["event_id"] for r in first], [r["event_id"] for r in second])
        self.assertEqual(len({r["event_id"] for r in first}), 3)

    def test_procurement_uses_its_own_date_field(self):
        rows = flatten_records(PROCUREMENT_PAGE["hojin-infos"], "procurement")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["event_date"], "2026-07-10")
        self.assertEqual(rows[0]["amount"], 24_000_000)
        self.assertEqual(rows[0]["note"], "一般競争入札")

    def test_every_declared_kind_has_a_date_field(self):
        for kind, spec in EVENT_KINDS.items():
            self.assertIn("list_key", spec, kind)
            self.assertIn("date_field", spec, kind)


class StoreTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.store = EventStore(Path(self._tmp.name))
        self.rows = flatten_records(SUBSIDY_PAGE["hojin-infos"], "subsidy")

    def tearDown(self):
        self._tmp.cleanup()

    def test_first_ingest_reports_everything_as_new(self):
        result = self.store.ingest(self.rows)
        self.assertEqual(len(result["new"]), 3)
        self.assertEqual(len(result["revised"]), 0)

    def test_second_ingest_of_same_data_reports_nothing(self):
        self.store.ingest(self.rows)
        result = self.store.ingest(self.rows)
        self.assertEqual(len(result["new"]), 0, "re-fetching a window must not duplicate")
        self.assertEqual(len(result["revised"]), 0)
        self.assertEqual(self.store.stats()["unique_events"], 3)

    def test_changed_payload_is_reported_as_revised(self):
        self.store.ingest(self.rows)
        amended = [dict(row) for row in self.rows]
        amended[0]["target"] = "中小企業（変更後）"
        from .normalize import content_hash

        amended[0]["content_hash"] = content_hash(amended[0])
        result = self.store.ingest(amended)
        self.assertEqual(len(result["new"]), 0)
        self.assertEqual(len(result["revised"]), 1)

    def test_new_event_appears_on_a_later_run(self):
        self.store.ingest(self.rows[:2])
        result = self.store.ingest(self.rows)
        self.assertEqual(len(result["new"]), 1)
        self.assertEqual(result["new"][0]["event_id"], self.rows[2]["event_id"])

    def test_first_seen_survives_a_revision(self):
        early = datetime(2026, 8, 1, tzinfo=timezone.utc)
        self.store.ingest(self.rows, observed_at=early)
        amended = [dict(row) for row in self.rows]
        amended[0]["content_hash"] = "changed"
        result = self.store.ingest(amended, observed_at=datetime(2026, 8, 9, tzinfo=timezone.utc))
        self.assertEqual(result["revised"][0]["first_seen_utc"], early.isoformat())

    def test_events_persist_across_store_instances(self):
        self.store.ingest(self.rows)
        reopened = EventStore(Path(self._tmp.name))
        self.assertEqual(len(reopened.ingest(self.rows)["new"]), 0)
        self.assertEqual(reopened.stats()["unique_events"], 3)

    def test_events_partition_by_event_month(self):
        self.store.ingest(self.rows)
        partitions = {p.stem for p in (Path(self._tmp.name) / "events").glob("*.jsonl")}
        self.assertEqual(partitions, {"2026-07"})

    def test_mixed_kinds_accumulate_together(self):
        self.store.ingest(self.rows)
        self.store.ingest(flatten_records(PROCUREMENT_PAGE["hojin-infos"], "procurement"))
        stats = self.store.stats()
        self.assertEqual(stats["unique_events"], 4)
        self.assertEqual(stats["rows_by_type"], {"subsidy": 3, "procurement": 1})


class SignalTest(unittest.TestCase):
    def test_signal_ranks_by_amount_and_counts_by_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = EventStore(Path(tmp))
            rows = flatten_records(SUBSIDY_PAGE["hojin-infos"], "subsidy")
            rows += flatten_records(PROCUREMENT_PAGE["hojin-infos"], "procurement")
            result = store.ingest(rows)
            signal = build_signal(
                date(2026, 8, 11),
                date(2026, 8, 5),
                date(2026, 8, 11),
                {"subsidy": 3, "procurement": 1},
                result,
                store.stats(),
            )
            self.assertEqual(signal["new_event_count"], 4)
            self.assertEqual(signal["new_events_by_type"], {"subsidy": 3, "procurement": 1})
            amounts = [row["amount"] for row in signal["top_new_events_by_amount"]]
            self.assertEqual(amounts, sorted(amounts, reverse=True))
            self.assertIn("gBizINFO", signal["attribution"])


class ProbeTest(unittest.TestCase):
    def test_month_bounds_handle_year_end_and_february(self):
        self.assertEqual(month_bounds(2026, 12), (date(2026, 12, 1), date(2026, 12, 31)))
        self.assertEqual(month_bounds(2026, 2), (date(2026, 2, 1), date(2026, 2, 28)))
        self.assertEqual(month_bounds(2024, 2), (date(2024, 2, 1), date(2024, 2, 29)))

    def test_recent_months_walks_backwards_across_new_year(self):
        months = recent_months(3, today=date(2026, 2, 15))
        self.assertEqual(months, [(2025, 12), (2026, 1), (2026, 2)])


class ClientTest(unittest.TestCase):
    def test_missing_token_fails_loudly(self):
        with self.assertRaises(GBizError):
            GBizClient(token="")

    def test_pagination_stops_at_total_page(self):
        class FakeSession:
            def __init__(self):
                self.calls = []

            def get(self, url, params=None, headers=None, timeout=None):
                self.calls.append(params["page"])
                page = int(params["page"])
                return _FakeResponse(
                    200,
                    {
                        "totalPage": "3",
                        "totalCount": "3",
                        "hojin-infos": [
                            {
                                "corporate_number": f"100001207000{page}",
                                "name": f"法人{page}",
                                "subsidy": [
                                    {"title": "補助金", "date_of_approval": "2026-07-01"}
                                ],
                            }
                        ],
                    },
                )

        session = FakeSession()
        client = GBizClient(token="t", min_interval=0.0, session=session)
        records = list(client.iter_update_info("subsidy", date(2026, 7, 1), date(2026, 7, 31)))
        self.assertEqual(len(records), 3)
        self.assertEqual(session.calls, ["1", "2", "3"])

    def test_404_is_treated_as_empty_not_an_error(self):
        class NotFoundSession:
            def get(self, url, params=None, headers=None, timeout=None):
                return _FakeResponse(404, None, text="not found")

        client = GBizClient(token="t", min_interval=0.0, session=NotFoundSession())
        records = list(client.iter_update_info("subsidy", date(2026, 7, 1), date(2026, 7, 31)))
        self.assertEqual(records, [])
        self.assertEqual(client.count_update_info("subsidy", date(2026, 7, 1), date(2026, 7, 31)), 0)

    def test_401_raises(self):
        class UnauthorizedSession:
            def get(self, url, params=None, headers=None, timeout=None):
                return _FakeResponse(401, None, text="unauthorized")

        client = GBizClient(token="bad", min_interval=0.0, session=UnauthorizedSession())
        with self.assertRaises(GBizError):
            list(client.iter_update_info("subsidy", date(2026, 7, 1), date(2026, 7, 31)))

    def test_token_is_sent_in_the_documented_header(self):
        captured = {}

        class CapturingSession:
            def get(self, url, params=None, headers=None, timeout=None):
                captured.update(headers=headers, params=params, url=url)
                return _FakeResponse(200, {"totalPage": "1", "hojin-infos": []})

        client = GBizClient(token="secret", min_interval=0.0, session=CapturingSession())
        list(client.iter_update_info("subsidy", date(2026, 7, 1), date(2026, 7, 31)))
        self.assertEqual(captured["headers"]["X-hojinInfo-api-token"], "secret")
        self.assertEqual(captured["params"]["from"], "20260701")
        self.assertEqual(captured["params"]["to"], "20260731")
        self.assertTrue(captured["url"].endswith("/v2/hojin/updateInfo/subsidy"))


class _FakeResponse:
    def __init__(self, status_code: int, payload, text: str = ""):
        self.status_code = status_code
        self._payload = payload
        self.text = text

    def json(self):
        return self._payload


if __name__ == "__main__":
    unittest.main()
