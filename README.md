# 巴哈姆特論壇排行榜自動更新

每日自動爬取巴哈姆特論壇三大分類的專版排行，前20名顯示於此，完整120名存入 `data/` 資料夾。

> 資料來源：[巴哈姆特電玩資訊站](https://forum.gamer.com.tw/)
> 更新時間：每日台灣時間 09:00（UTC 01:00）

---

## 手機遊戲哈啦區 Top 20

<!-- MOBILE_TABLE_START -->
_更新時間: 2026-05-12_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
<!-- MOBILE_TABLE_END -->

---

## PC遊戲哈啦區 Top 20

<!-- PC_TABLE_START -->
_更新時間: 2026-05-12_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
<!-- PC_TABLE_END -->

---

## 宅生活哈拉區 Top 20

<!-- LIFESTYLE_TABLE_START -->
_更新時間: 2026-05-12_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
<!-- LIFESTYLE_TABLE_END -->

---

## 完整排行 CSV

每日完整 120 名排行存放於 [`data/`](./data/) 資料夾，檔名格式：`YYYY-MM-DD_{slug}.csv`

| slug | 分類 |
|------|------|
| `mobile` | 手機遊戲哈啦區 |
| `pc` | PC遊戲哈啦區 |
| `lifestyle` | 宅生活哈拉區 |

欄位：`rank`、`title`（專版名稱）、`popularity`（人氣）、`article`（昨日文章數）、`bsn`（板號）

---

## GitHub Pages 展示站

專案另外提供 GitHub Pages 展示站，包含：

- 三種嵌入版型的即時預覽
- 可直接複製的 `iframe` 嵌入語法
- 實際可嵌入網站的榜單頁面

啟用後可從這裡查看：

- 展示首頁：<https://dbs1203531.github.io/BahaForumRankData/>
- 嵌入頁範例：<https://dbs1203531.github.io/BahaForumRankData/embed/ranking.html?layout=sidebar&category=mobile&limit=8>

---

## JSON 資料輸出

除了每日 CSV，專案也會輸出給嵌入頁使用的 JSON：

- [`data/latest.json`](./data/latest.json)：三個分類的合併資料
- [`data/latest/`](./data/latest/)：各分類獨立資料

每筆榜單資料包含：

- `rank`
- `title`
- `popularity`
- `article`
- `bsn`
- `board_url`
- `category_slug`
- `category_label`

---

## 嵌入語法

官方建議使用 `iframe`，因為最通用，也最不容易和使用者網站樣式衝突。

```html
<iframe
  src="https://dbs1203531.github.io/BahaForumRankData/embed/ranking.html?layout=sidebar&category=mobile&limit=8"
  width="340"
  height="560"
  style="border:0;"
  loading="lazy">
</iframe>
```

可用參數：

- `layout=sidebar|banner|inline`
- `category=mobile|pc|lifestyle`
- `limit=數量`
- `theme=light`

如果你是 fork 這個專案，請把網址改成你自己的 GitHub Pages 網址。

---

## 本地執行

```bash
pip install -r requirements.txt
python main.py
```

## GitHub Actions

專案透過 GitHub Actions 排程自動執行，會：

- 抓取最新排行
- 更新 `README.md`
- 產生 `CSV` 與 `JSON`
- 部署 `docs/` 到 GitHub Pages

詳見 [`.github/workflows/update_rankings.yml`](.github/workflows/update_rankings.yml)。
