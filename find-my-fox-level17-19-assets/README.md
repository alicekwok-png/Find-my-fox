# Find My Fox — Level 17–19 Game Assets

這個素材包根據專案內 `find-the-fox-level17-asset-prompts-v3.md`、`find-the-fox-level18-asset-prompts-v3.md` 及 `find-the-fox-level19-asset-prompts-v3.md` 製作，包含三個關卡嘅全景背景、狐狸角色、狐形物件及局部線索。

## 素材統計

| 關卡 | 背景 | 角色 Tier A | 物件 Tier B | 線索 Tier C | PNG 總數 |
|---|---:|---:|---:|---:|---:|
| Level 17 | 1 | 15 | 22 | 6 | 44 |
| Level 18 | 1 | 15 | 21 | 5 | 42 |
| Level 19 | 1 | 15 | 19 | 6 | 41 |
| **合計** | **3** | **45** | **62** | **17** | **127** |

## 輸出規格

每個關卡嘅 `background/` 內係一張 2688×1152 PNG 全景背景；`characters/`、`objects/` 及 `clues/` 內嘅 124 張疊加素材係 1920×1920 PNG，並已轉成 RGBA 透明背景，方便直接作為遊戲圖層使用。背景全景圖保留 RGB，角色、物件及線索均已通過 PNG 完整性及 RGBA 檢查。

## 目錄結構

```text
assets/
├── level17/
│   ├── background/
│   ├── characters/
│   ├── objects/
│   └── clues/
├── level18/
│   ├── background/
│   ├── characters/
│   ├── objects/
│   └── clues/
└── level19/
    ├── background/
    ├── characters/
    ├── objects/
    └── clues/
```

檔名編碼沿用提示文件：`A` 代表 Tier A 角色、`O/E/N` 代表 Tier B 物件類型、`C` 代表 Tier C 局部線索。每個檔案名亦包含關卡編號及主要識別描述，方便匯入資產管理系統。
