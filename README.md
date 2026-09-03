# 巴哈姆特論壇排行榜自動更新

每日自動爬取巴哈姆特論壇三大分類的專版排行，前20名顯示於此，完整120名存入 `data/` 資料夾。

> 資料來源：[巴哈姆特電玩資訊站](https://forum.gamer.com.tw/)
> 更新時間：每日台灣時間 09:00（UTC 01:00）

---

## 手機遊戲哈啦區 Top 20

<!-- MOBILE_TABLE_START -->
_更新時間: 2026-09-03_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
| 1 | 瑪奇 Mobile | 190084 | 87 |
| 2 | 鳴潮 | 146768 | 36 |
| 3 | SD 鋼彈 G 世代 永恆 | 105570 | 64 |
| 4 | 明日方舟：終末地 | 102322 | 53 |
| 5 | 神魔之塔 | 99596 | 96 |
| 6 | Fate/Grand Order | 83791 | 71 |
| 7 | 棕色塵埃 2 | 75994 | 12 |
| 8 | 勝利女神：妮姬 | 75162 | 35 |
| 9 | 原神 | 63749 | 55 |
| 10 | 崩壞：星穹鐵道 | 56185 | 35 |
| 11 | 異環 | 50444 | 44 |
| 12 | 貓咪大戰爭（にゃんこ大戦争） | 50076 | 8 |
| 13 | 天堂 Mobile | 39394 | 12 |
| 14 | 絕區零 | 38073 | 19 |
| 15 | 塔塔冒險隊 | 36095 | 9 |
| 16 | 辟邪除妖 Variants Daphne | 35775 | 18 |
| 17 | 怪物彈珠 | 35021 | 40 |
| 18 | Pokemon GO | 34850 | 14 |
| 19 | Monster Hunter Now | 30441 | 7 |
| 20 | 三國觀滄海 | 25829 | 20 |
<!-- MOBILE_TABLE_END -->

---

## PC遊戲哈啦區 Top 20

<!-- PC_TABLE_START -->
_更新時間: 2026-09-03_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
| 1 | 新楓之谷 | 229904 | 67 |
| 2 | 新楓之谷：經典版 | 180707 | 127 |
| 3 | MapleStory Worlds | 116161 | 31 |
| 4 | RO 仙境傳說 Online | 82824 | 27 |
| 5 | 英雄聯盟 League of Legends | 81608 | 560 |
| 6 | 燕雲十六聲 | 69830 | 74 |
| 7 | 黑色沙漠 BLACK DESERT | 48246 | 15 |
| 8 | Final Fantasy XIV | 47429 | 34 |
| 9 | 流亡黯道 Path of Exile | 44875 | 15 |
| 10 | SpiritVale | 43563 | 7 |
| 11 | 天堂：經典版 | 41284 | 28 |
| 12 | 暗黑破壞神 | 40331 | 75 |
| 13 | AION2 | 35772 | 24 |
| 14 | WOW 魔獸世界 | 35517 | 17 |
| 15 | 爐石戰記 | 31874 | 5 |
| 16 | 幻獸帕魯 | 24537 | 18 |
| 17 | APEX 英雄 | 21704 | 3 |
| 18 | 決勝時刻 | 20432 | 1 |
| 19 | Minecraft 我的世界（當個創世神） | 19425 | 53 |
| 20 | 流亡黯道 PoE 2 | 18688 | 7 |
<!-- PC_TABLE_END -->

---

## 宅生活哈拉區 Top 20

<!-- LIFESTYLE_TABLE_START -->
_更新時間: 2026-09-03_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
| 1 | 電腦應用綜合討論 | 157054 | 67 |
| 2 | Steam 綜合討論板 | 51928 | 21 |
| 3 | 綜合公仔玩具討論區 | 35587 | 12 |
| 4 | 模型技術與資訊 | 30089 | 0 |
| 5 | 動漫相關綜合 | 17779 | 75 |
| 6 | 影音視聽討論區 | 17154 | 32 |
| 7 | 智慧型手機 | 14640 | 10 |
| 8 | 職場甘苦談 | 13081 | 5 |
| 9 | ACG二手交易板 | 10472 | 74 |
| 10 | 歡樂惡搞 KUSO | 8907 | 13 |
| 11 | 電影娛樂新視界 | 8321 | 13 |
| 12 | 桌上角色扮演遊戲(TRPG)討論 | 5153 | 4 |
| 13 | 布袋戲文化綜合討論區 | 4603 | 1 |
| 14 | 汽機車討論 | 4395 | 0 |
| 15 | 講談說論 | 4158 | 25 |
| 16 | 野戰 (生存) 遊戲 | 4125 | 4 |
| 17 | 虛擬 Youtuber（Vtuber） | 3882 | 13 |
| 18 | 電視遊樂器綜合討論區 | 3620 | 3 |
| 19 | 恐怖驚悚 | 3149 | 1 |
| 20 | 軍事策略 | 2698 | 3 |
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
