import sys
import logging
from scraper.categories import CATEGORIES, PAGES_NEEDED, TOP_N_FOR_README
from scraper.fetch import collect_category
from save_csv import save_csv
from save_json import save_json
from update_readme import update_readme

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def main() -> None:
    results: dict[str, list[dict]] = {}
    failed: list[str] = []

    for slug, cfg in CATEGORIES.items():
        label = cfg["label"]
        c = cfg["c"]
        logger.info("=== Collecting '%s' (c=%s) ===", label, c)
        try:
            boards = collect_category(c, PAGES_NEEDED)
            expected_count = PAGES_NEEDED * 30
            if not boards:
                logger.error("'%s' returned 0 boards; refusing to publish empty data.", label)
                failed.append(slug)
                continue
            if len(boards) < expected_count:
                logger.warning(
                    "'%s' returned only %d boards (expected %d).",
                    label, len(boards), expected_count,
                )
            results[slug] = boards
            logger.info("Collected %d boards for '%s'.", len(boards), label)
        except Exception as exc:
            logger.error("Failed to collect '%s': %s", label, exc, exc_info=True)
            failed.append(slug)

    if failed:
        logger.error("Aborting: failed categories: %s", failed)
        sys.exit(1)

    # Save CSVs
    for slug, boards in results.items():
        try:
            save_csv(slug, boards)
        except Exception as exc:
            logger.error("Failed to save CSV for '%s': %s", slug, exc, exc_info=True)
            sys.exit(1)

    # Save JSON feeds for GitHub Pages embeds and external consumers
    try:
        save_json(results, CATEGORIES)
    except Exception as exc:
        logger.error("Failed to save JSON feeds: %s", exc, exc_info=True)
        sys.exit(1)

    # Update README
    try:
        update_readme(results, TOP_N_FOR_README)
    except Exception as exc:
        logger.error("Failed to update README: %s", exc, exc_info=True)
        sys.exit(1)

    logger.info("All done.")


if __name__ == "__main__":
    main()
