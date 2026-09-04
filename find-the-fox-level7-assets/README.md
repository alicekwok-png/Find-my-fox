# Find The Fox — Level 7 遊戲素材套件

本套件根據 `find-the-fox-level7-asset-prompts-v3.md` 製作，並按使用者要求**跳過 Tier A 角色**，直接製作 v3 文件內嘅背景、Tier B 物件及 Tier C 局部線索。主題為**魯氏狐（Rüppell's Fox）／中東沙漠夜景**，採用深靛藍及午夜藍天空、暖琥珀營火餘燼、冷沙藍沙丘陰影嘅故事書卡通風格。

## 套件內容

| 類別 | 數量 | 輸出格式 | 說明 |
|---|---:|---|---|
| 背景場景 | 1 | PNG，2560×1440 | 中東沙漠夜景全景，含貝都因家庭、兩隻單峰駱駝、營火、古代拱門及岩地活動區 |
| Tier A | 0 | 未製作 | 按使用者要求跳過；原 v3 文件亦未附上 15 個角色 prompt |
| Tier B | 20 | PNG，1920×1920，RGBA | 14 件 reskin 物件及 6 件中東沙漠限定物件 |
| Tier C | 7 | PNG，1920×1920，RGBA | 爪印、尾尖、狐影、耳朵、鼻鬚及發光狐眼等局部線索 |
| **今次交付總計** | **28** |  | **1 張背景＋27 張透明合成素材** |

所有 Tier B 及 Tier C 圖像已整理為真正透明背景，方便疊加到背景上。建議以 `background/level7_desert_night_panorama.png` 作底層，再按 Zone 及指定錨點放置素材。

## 目錄結構

```text
find-the-fox-level7-assets/
├── background/
├── tier-b/
├── tier-c/
├── asset_manifest.csv
├── source_spec.md
└── README.md
```

## Zone 對應

| Zone | 主場景 | 素材範圍 |
|---|---|---|
| Zone 1 | 營火、鞍袋、繩圈及駱駝挽具 | O1–O4、O12、N1、N3、C1、C5 |
| Zone 2 | 古代石拱門、廢墟、倒塌石柱及沙地 | O5–O7、O11、O14、N2、N5、C2、C4、C7 |
| Zone 3 | 尖角岩地、木製路標、陶器碎片及第二個火堆 | O8–O10、O13、N4、N6、C3、C6 |

## 整合備註

背景係 RGB 全景圖；Tier B–C 係 RGBA 透明 PNG。遊戲內縮放時應保持每張 sprite 嘅正方形畫布比例，並以 alpha 通道控制顯示範圍。Tier C 屬於細小局部線索，建議先按指定錨點嵌入背景，再於測試裝置上調整顯示尺寸及 hitbox。

詳細 ID、檔名、難度及指定錨點請參考 `asset_manifest.csv`。
