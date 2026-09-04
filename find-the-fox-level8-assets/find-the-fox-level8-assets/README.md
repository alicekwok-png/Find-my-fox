# Find The Fox — Level 8 遊戲素材套件

本套件根據 `find-the-fox-level8-asset-prompts-v3.md` 製作，主題為**布氏狐（Blanford's Fox）／峭壁岩地黃昏**。全部可合成素材採用同一套故事書卡通視覺方向：粗黑線稿、柔和 cel-shading、玫瑰色及琥珀色黃昏天空、冷 slate-grey 岩石陰影，以及柔和金色邊光。

## 套件內容

| 類別 | 數量 | 輸出格式 | 說明 |
|---|---:|---|---|
| 背景場景 | 1 | PNG，2560×1440 | 單張連續全景背景，含登山家庭、馱騾、營火、岩台及崖頂活動區 |
| Tier A | 15 | PNG，1920×1920，RGBA | 11 隻布氏狐、3 隻藏狐、1 隻孟加拉狐預告角色 |
| Tier B | 21 | PNG，1920×1920，RGBA | 14 件 reskin 狐形物件及 7 件峭壁限定物件 |
| Tier C | 8 | PNG，1920×1920，RGBA | 爪印、尾尖、耳朵、鼻鬚、眼睛及影子等局部線索 |
| **總計** | **45** |  | **1 張背景＋44 張可合成素材** |

所有 Tier A–C 圖像已整理為真正透明背景，方便在遊戲內以獨立 layer 疊加到背景上。建議以 `background/level8_cliffside_dusk_panorama.png` 作為底層，再按 Zone 及指定錨點放置 Tier A–C 素材。

## 目錄結構

```text
find-the-fox-level8-assets/
├── background/
├── tier-a/
├── tier-b/
├── tier-c/
├── asset_manifest.csv
├── source_spec.md
└── README.md
```

## Zone 對應

| Zone | 主場景 | 建議使用素材 |
|---|---|---|
| Zone 1 | 營火、物資木箱、馱騾及登山繩 | O1–O4、O12、N2、N6、C1、C5、C8 |
| Zone 2 | 中央岩台、編織毯、窄岩縫及補給袋 | O5–O7、O11、O14、N3、N5、C2、C4、C7 |
| Zone 3 | 崖頂、石拱、散落石堆及攀山裝備 | O8–O10、O13、N1、N4、N7、C3、C6 |

## 整合備註

背景是 RGB 全景圖；Tier A–C 是 RGBA 透明 PNG。遊戲內縮放時應保持每張 sprite 的原始正方形畫布比例，並以 alpha 通道控制顯示範圍。Tier C 屬於非常細小的局部線索，建議按指定錨點先嵌入背景層，再在測試裝置上調整顯示尺寸及 hitbox；Tier A 角色則可用獨立 hitbox，Tier B 物件可按實際可見範圍設定較細 hitbox。

詳細 ID、檔名、難度及指定錨點請參考 `asset_manifest.csv`。
