# 巴哈姆特論壇排行榜自動更新

每日自動爬取巴哈姆特論壇三大分類的專版排行，前20名顯示於此，完整120名存入 `data/` 資料夾。

> 資料來源：[巴哈姆特電玩資訊站](https://forum.gamer.com.tw/)
> 更新時間：每日台灣時間 09:00（UTC 01:00）

---

## 手機遊戲哈啦區 Top 20

<!-- MOBILE_TABLE_START -->
_更新時間: 2026-03-11_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
<!-- MOBILE_TABLE_END -->

---

## PC遊戲哈啦區 Top 20

<!-- PC_TABLE_START -->
_更新時間: 2026-03-11_

| 排名 | 專版名稱 | 人氣 | 昨日文章 |
|------|----------|------|----------|
<!-- PC_TABLE_END -->

---

## 宅生活哈拉區 Top 20

<!-- LIFESTYLE_TABLE_START -->
_更新時間: 2026-03-11_

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

## 本地執行

```bash
pip install -r requirements.txt
python main.py
```

## GitHub Actions

專案透過 GitHub Actions 排程自動執行，詳見 [`.github/workflows/update_rankings.yml`](.github/workflows/update_rankings.yml)。
