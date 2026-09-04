# Find The Fox — 探險家裝備 Bank（新增，專門解決荒野場景密度不足問題）

**用途：** 呢家人係認真嘅博物學家/探險家，隨身帶住成套採集裝備。呢批物件同原本16件「家庭紀念品」bank係同一個概念（跨全部關卡reuse，換個anchor同mimicry就用得），但專門解決我哋一直撞到嘅問題——荒野場景（岩石地、神龕、崖頂）先天物件密度低過室內場景，靠呢批細細粒、成套嘅裝備補返。
**日期：** 2026-09-02
**同技術文件關係：** 呢個bank係第2.2節「Tier B reskin bank」嘅正式擴充，用法一樣——套落實際關卡嗰陣，要跟2.10（指定錨點）＋2.11（度身訂造融入）補返實際嘅anchor同mimicry描述，呢度先寫底層概念prompt。

---

## 共用風格咒語（沿用）

```
Cozy storybook cartoon illustration style, thick clean black linework, soft cel-shaded coloring, family-friendly mobile hidden-object game art, detailed but readable at small size, NOT chibi, NOT photorealistic, NOT 3D render.
```

---

## 探險家裝備清單（8件，底層概念prompt）

| # | 裝備 | 概念Prompt（套落實際關卡時要加返anchor+mimicry） |
|---|---|---|
| E1 | 狐紋放大鏡 | `A small brass magnifying glass with a tiny fox emblem etched into the handle, an object not a living creature, isolated on transparent background.` |
| E2 | 標本瓶 | `A small corked glass specimen jar with a hand-drawn fox illustration on its paper label, an object not a living creature, isolated on transparent background.` |
| E3 | 野外素描本 | `A small open field sketchbook showing a rough pencil sketch of a fox mid-page, a pencil resting in the book's spine, an object not a living creature, isolated on transparent background.` |
| E4 | 採集標籤 | `A small paper collection tag tied with string, a tiny fox-paw stamp printed on it, an object not a living creature, isolated on transparent background.` |
| E5 | 壓花標本冊 | `A small pressed-flower album with a fox-shaped ribbon bookmark hanging out of its pages, an object not a living creature, isolated on transparent background.` |
| E6 | 捲軸地圖 | `A small rolled paper map tied with string, sealed with a wax stamp shaped like a fox, an object not a living creature, isolated on transparent background.` |
| E7 | 黃銅捲尺 | `A small brass measuring tape with a fox emblem stamped on its case, an object not a living creature, isolated on transparent background.` |
| E8 | 皮革工具捲 | `A small rolled leather tool pouch with a stitched fox emblem, tied shut with a leather cord, an object not a living creature, isolated on transparent background.` |

**同現有bank重疊嘅提醒：** 之前L2用過嘅「狐紋指南針」（N4）、原有嘅「狐形針插」都屬於同一個「探險裝備」精神,可以正式歸入呢個bank一齊管理,唔使當成獨立類別。

---

## 用法示範（點樣填補一個已知嘅低密度位）

以L3嗰個岩石尖峰空地為例，加返E1、E3兩件落去：

```
[共用風格咒語+色調] A small brass magnifying glass with a tiny fox emblem etched into the handle, its warm brass tone matching the weathered supply crate it rests on, resting on top of a supply crate near the jagged rock spires, an object not a living creature, isolated on transparent background.
```

```
[共用風格咒語+色調] A small open field sketchbook showing a rough pencil sketch of a fennec fox mid-page, its worn leather cover matching the rocks around it, tucked beside the coiled rope at the base of the rock spires, an object not a living creature, isolated on transparent background.
```

即係話，用法同其他bank item一樣——揀件裝備，指定一個實際錨點，加一句mimicry描述，就完成。

---

## 建議下一步

1. 呢8件裝備可以直接補落之前已經標低「密度不足」嘅位（L3岩石尖峰、L4神龕周邊）
2. 之後做新關卡（L11-50）嗰陣，呢個bank都可以直接攞嚟填低密度嘅空地，唔使每次都諗新概念
