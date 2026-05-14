import json
import unittest

from scraper.parse import parse_boards_from_html


class ParseBoardsFromHtmlTest(unittest.TestCase):
    def test_parses_current_rank_card_markup(self):
        html = """
        <div class="forum-card" data-rank="1">
          <a href="https://forum.gamer.com.tw/B.php?bsn=80679">
            <img alt="異環" />
          </a>
          <div>
            <span>
              <data value="419026">42萬</data>
              <data value="419026">419,026</data>
            </span>
            <span><data value="280">280</data></span>
          </div>
          <h3>異環</h3>
        </div>
        """

        self.assertEqual(
            parse_boards_from_html(html),
            [{
                "rank": 1,
                "title": "異環",
                "popularity": 419026,
                "article": 280,
                "bsn": 80679,
            }],
        )

    def test_falls_back_to_legacy_next_chunks(self):
        payload = {
            "children": [{
                "rank": 2,
                "title": "鳴潮",
                "popularity": 363713,
                "article": 271,
                "bsn": 74934,
            }],
        }
        content = "12:" + json.dumps(payload, ensure_ascii=False)
        escaped_content = json.dumps(content, ensure_ascii=False)[1:-1]
        html = f'<script>self.__next_f.push([1,"{escaped_content}"])</script>'

        self.assertEqual(
            parse_boards_from_html(html),
            [{
                "rank": 2,
                "title": "鳴潮",
                "popularity": 363713,
                "article": 271,
                "bsn": 74934,
            }],
        )

    def test_empty_html_returns_no_boards(self):
        self.assertEqual(parse_boards_from_html("<html></html>"), [])


if __name__ == "__main__":
    unittest.main()
