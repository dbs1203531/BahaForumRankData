import unittest
from unittest.mock import patch

import main


class MainFailureTest(unittest.TestCase):
    @patch("main.collect_category", return_value=[])
    @patch("main.save_csv")
    @patch("main.save_json")
    @patch("main.update_readme")
    def test_empty_category_result_exits_before_publishing(
        self,
        update_readme_mock,
        save_json_mock,
        save_csv_mock,
        collect_category_mock,
    ):
        with self.assertRaises(SystemExit) as exc:
            main.main()

        self.assertEqual(exc.exception.code, 1)
        self.assertGreaterEqual(collect_category_mock.call_count, 1)
        save_csv_mock.assert_not_called()
        save_json_mock.assert_not_called()
        update_readme_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
