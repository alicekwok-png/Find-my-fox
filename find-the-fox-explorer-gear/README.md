# Find The Fox — Explorer Gear Bank

本套件根據 `find-the-fox-explorer-gear-bank.md` 製作，包含 8 件可跨關卡重用嘅探險家／博物學家裝備素材。所有圖像均採用 cozy storybook cartoon hidden-object game 風格，適合放入岩石地、神龕、崖頂及其他荒野低密度場景，以 anchor 同 mimicry 描述再嵌入實際關卡。

## 套件內容

| ID | 裝備 | 輸出格式 | 用途 |
|---|---|---|---|
| E1 | 狐紋放大鏡 | PNG，1920×1920，RGBA | 放喺補給箱、石面或木枱上 |
| E2 | 標本瓶 | PNG，1920×1920，RGBA | 放喺採集袋、岩架或標本區 |
| E3 | 野外素描本 | PNG，1920×1920，RGBA | 靠住繩圈、石堆或裝備箱 |
| E4 | 採集標籤 | PNG，1920×1920，RGBA | 綁喺植物、籃子或工具上 |
| E5 | 壓花標本冊 | PNG，1920×1920，RGBA | 放喺背包、木箱或神龕邊 |
| E6 | 捲軸地圖 | PNG，1920×1920，RGBA | 放喺岩石平台、供應箱或地面 |
| E7 | 黃銅捲尺 | PNG，1920×1920，RGBA | 放喺工具捲、木箱或測量站 |
| E8 | 皮革工具捲 | PNG，1920×1920，RGBA | 放喺攀爬裝備、補給箱或岩地 |

## 整合備註

8 件素材均為獨立透明 cutout，已清除生成時嘅 checkerboard 背景。使用時應按實際關卡指定 anchor，例如「放喺 weathered supply crate 頂部」，再補充與周圍材質相近嘅 mimicry 描述。每件 sprite 保留正方形畫布比例，建議由遊戲 runtime 以 alpha 通道合成及設定 hitbox。

## 目錄結構

```text
find-the-fox-explorer-gear/
├── gear/
├── asset_manifest.csv
├── source_spec.md
└── README.md
```

詳細檔名、類型及推薦 anchor 請參考 `asset_manifest.csv`。
