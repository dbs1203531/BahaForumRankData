const DEFAULTS = {
  category: "mobile",
  layout: "sidebar",
  limit: 8,
  theme: "light",
};

const VALID_CATEGORIES = new Set(["mobile", "pc", "lifestyle"]);
const VALID_LAYOUTS = new Set(["sidebar", "banner", "inline"]);
const CATEGORY_CHIPS = {
  mobile: "手機",
  pc: "PC",
  lifestyle: "宅生活",
};

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll("\"", "&quot;")
    .replaceAll("'", "&#39;");
}

function formatNumber(value) {
  if (value === null || value === undefined || value === "") {
    return "-";
  }
  return new Intl.NumberFormat("zh-TW").format(Number(value));
}

function parseConfig() {
  const params = new URLSearchParams(window.location.search);
  const category = VALID_CATEGORIES.has(params.get("category")) ? params.get("category") : DEFAULTS.category;
  const layout = VALID_LAYOUTS.has(params.get("layout")) ? params.get("layout") : DEFAULTS.layout;
  const limitValue = Number(params.get("limit"));
  const limit = Number.isFinite(limitValue) && limitValue > 0 ? Math.min(limitValue, 20) : DEFAULTS.limit;
  const theme = params.get("theme") || DEFAULTS.theme;
  return { category, layout, limit, theme };
}

function boardHue(board, index) {
  const seed = Number(board.bsn || index + 1);
  return 180 + ((seed * 17) % 120);
}

function renderBoard(container, payload, config) {
  const categoryData = payload.categories?.[config.category];
  if (!categoryData || !Array.isArray(categoryData.boards) || categoryData.boards.length === 0) {
    container.className = "ranking-widget is-error";
    container.innerHTML = '<p class="ranking-status">目前沒有可顯示的排行資料。</p>';
    return;
  }

  const boards = categoryData.boards.slice(0, config.limit);
  const items = boards
    .map((board, index) => {
      const rank = Number(board.rank || index + 1);
      const topClass = rank <= 3 ? " is-top3" : "";
      const hue = boardHue(board, index);
      return `
        <a
          class="ranking-card${topClass}"
          data-layout="${config.layout}"
          href="${escapeHtml(board.board_url)}"
          target="_blank"
          rel="noreferrer noopener"
          style="--accent-h:${hue};"
        >
          <span class="ranking-rank">${escapeHtml(rank)}</span>
          <span class="ranking-media" aria-hidden="true">
            <span class="ranking-media__label">${escapeHtml(CATEGORY_CHIPS[config.category])}</span>
          </span>
          <span class="ranking-copy">
            <span class="ranking-title">${escapeHtml(board.title)}</span>
            <span class="ranking-meta">
              <span>人氣 ${escapeHtml(formatNumber(board.popularity))}</span>
              <span>文章 ${escapeHtml(formatNumber(board.article))}</span>
            </span>
          </span>
        </a>
      `;
    })
    .join("");

  container.className = "ranking-widget";
  container.innerHTML = `
    <div class="ranking-board" data-layout="${config.layout}" data-theme="${escapeHtml(config.theme)}">
      ${items}
    </div>
    <div class="ranking-footer">
      <span>更新日期 ${escapeHtml(payload.generated_at || "-")}</span>
      <a href="${escapeHtml(payload.source_url || "https://forum.gamer.com.tw/")}" target="_blank" rel="noreferrer noopener">資料來源</a>
    </div>
  `;
}

async function init() {
  const container = document.getElementById("ranking-widget");
  const config = parseConfig();

  try {
    const response = await fetch("../data/latest.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const payload = await response.json();
    renderBoard(container, payload, config);
  } catch (error) {
    container.className = "ranking-widget is-error";
    container.innerHTML = '<p class="ranking-status">排行載入失敗，請稍後再試。</p>';
    console.error("Failed to load ranking feed", error);
  }
}

document.addEventListener("DOMContentLoaded", init);
