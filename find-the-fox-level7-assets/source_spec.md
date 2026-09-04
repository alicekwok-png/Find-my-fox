# Find The Fox — Level 7 素材生成 Prompt 套件（v3補充版）

**主角／場景：** 魯氏狐 Rüppell's Fox／中東沙漠夜景
**客串：** 耳廓狐 Fennec Fox（返場）、布氏狐 Blanford's Fox（預告）
**日期：** 2026-09-02
**本文件範圍：** Tier A（15隻）沿用`find-the-fox-level7-asset-prompts.md`嘅v2版本，**不變、不重複貼**。本文件只做v3新增部分——背景（加真人貝都因家庭+駱駝）、Tier B、Tier C。

---

## 共用風格咒語（沿用）

```
Cozy storybook cartoon illustration style, thick clean black linework, soft cel-shaded coloring, family-friendly mobile hidden-object game art, detailed but readable at small size, NOT chibi, NOT photorealistic, NOT 3D render.
```

## Level 7 專屬色調

```
Deep desert night palette — indigo and midnight-blue sky, warm amber campfire-ember accents, cool sand-blue dune shadows.
```

## 人物角色渲染守則

- 人數6-9個（人＋動物），每Zone foreground站最少2個一齊，搵伴用動物唔用新人類
- **動物要合乎中東沙漠夜景場景**：用單峰駝（Dromedary camel）做伴（同L3嘅賽路基獵犬區分開，呢關淨係用駱駝）
- 3個Zone各拆做至少3個站點，留白；`ground_only`嘅嘢一律地面

---

## A. 背景場景 Prompt（單張全景版，含真人貝都因家庭＋駱駝）

```
[共用風格咒語+色調] A single wide continuous panoramic illustration of a Middle Eastern desert at night, spanning left to right in one unbroken scene, gently populated with a bedouin-traveling family and their two dromedary camels — rendered in the same storybook cartoon style purely as background scenery and atmosphere, simplified faces, not hidden-object targets, no independent hitboxes needed. The scene is composed of clearly separated clusters of activity, every foreground activity cluster containing at least two figures together, with open patches of sand dunes and starry sky between clusters: on the far left, a father figure kneels beside a dying bedouin campfire together with a resting camel nearby, rolling sand dunes stretching behind them under a star-filled midnight sky (foreground cluster, two figures together); a stretch of open dune away, woven saddle bags and coiled rope sit stacked beside a rock (a second, separate cluster); above, a tall wooden signpost with a hanging lantern rises against the night sky (an elevated third cluster). In the center, a mother and young child sit together near an ancient stone archway half-buried in sand, weathered ruins around them (foreground cluster, two figures together); a stretch of open sand away, a second camel rests quietly near a fallen column (a second, separate cluster); rising above, the archway's weathered top rises against the deep indigo sky (an elevated third cluster). On the far right, an older sibling kneels together with a Saluki hound near a rocky desert outcrop, scattered stones and old pottery shards nearby (foreground cluster, two figures together); a stretch of open sand away, the glowing embers of a second, smaller fire flicker near a collapsed pillar (a second, separate cluster); to one side, a jagged rock formation rises against the star-filled sky (a third, elevated cluster). Ground covered throughout with fine sand and scattered footprints concentrated around each cluster, consistent deep-night moonlight across the entire scene, consistent dune-line height from left to right. Ultra-wide panoramic landscape composition (approx. 1.7:1 to 2:1 aspect ratio), single continuous image with no seams or breaks, background only — no fox characters, no fox-shaped objects, no UI; these will be composited on top as separate layers afterward.
```

---

## B. Tier B：狐形物件 Prompt（20件＝14件reskin＋6件全新中東沙漠限定款式）

**14件reskin**（沿用bank，圖案換做魯氏狐配色）：

| # | 原款式 | Zone | 指定錨點 | 難度 | Prompt |
|---|---|---|---|---|---|
| O1 | 狐面杯 | Zone 1（營火） | 放喺營火邊嘅平沙石 | 明處 | `[共用風格咒語+色調] A small ceramic mug printed with a cute Rüppell's fox face design, black-and-white tail-tip motif border, its glaze tone matching the warm ember glow of the campfire beside it, sitting near the campfire, an object not a living creature, isolated on transparent background.` |
| O2 | 狐紋毛毯 | Zone 1（營火） | 搭喺鞍袋上面 | 半遮 | `[共用風格咒語+色調] A folded woven blanket with a repeating Rüppell's fox pattern, its earthy tones matching the woven saddle bag beneath it, draped over a saddle bag, only one corner visible, an object not a living creature, isolated on transparent background.` |
| O3 | 狐尾鎖匙扣 | Zone 1（營火） | 掛喺鞍袋帶 | 半遮 | `[共用風格咒語+色調] A small black-and-white fox-tail-shaped keychain charm hanging from a saddle bag strap, an object not a living creature, isolated on transparent background.` |
| O4 | 狐形曲奇 | Zone 1（營火） | 放喺熄咗嘅炭火邊嘅布上 | 明處 | `[共用風格咒語+色調] A small Rüppell's-fox-shaped cookie, its golden-brown color matching the dying embers beside it, resting on a cloth near the dying embers, an object not a living creature, isolated on transparent background.` |
| O5 | 織冷公仔 | Zone 2（拱門） | 靠住石拱門座腳 | 明處 | `[共用風格咒語+色調] A small knitted plush Rüppell's fox toy, its sandy yarn tone matching the weathered stone archway it leans against, sitting near the ancient stone archway, an object not a living creature, isolated on transparent background, full item visible.` |
| O6 | 狐紋thermos | Zone 2（拱門） | 企喺廢墟碎石中間 | 明處 | `[共用風格咒語+色調] A metal thermos flask printed with a repeating Rüppell's fox pattern, standing upright near the ruins, an object not a living creature, isolated on transparent background, full item visible.` |
| O7 | 狐形鹽椒樽 | Zone 2（拱門） | 貼住倒塌石柱 | 半遮 | `[共用風格咒語+色調] A ceramic salt-and-pepper shaker set shaped like two sitting Rüppell's foxes, its sandstone glaze matching the fallen column beside it, tucked beside a fallen column, an object not a living creature, isolated on transparent background.` |
| O8 | 狐耳冷帽 | Zone 3（岩地） | 掛喺尖角岩石凸出處 | 半遮 | `[共用風格咒語+色調] A knitted hat with two pointed fox-ear shapes, its sand-toned wool matching the jagged rock it hangs from, hanging off a jagged rock, only the ear tips visible, an object not a living creature, isolated on transparent background.` |
| O9 | 狐形風鈴 | Zone 3（岩地） | 掛喺木製路標柱 | 明處 | `[共用風格咒語+色調] A small metal wind chime with a fox-shaped charm, hanging from the wooden signpost, an object not a living creature, isolated on transparent background.` |
| O10 | 狐狸圖鑑書 | Zone 3（岩地） | 半掩喺陶器碎片之間 | 半遮 | `[共用風格咒語+色調] A field guide book with a printed Rüppell's fox illustration on its sand-dusted cover, matching the scattered pottery shards around it, tucked beside scattered pottery shards, an object not a living creature, isolated on transparent background.` |
| O11 | 狐紋圍巾 | Zone 2（拱門） | 搭喺石拱門底座 | 半遮 | `[共用風格咒語+色調] A knitted scarf with a fox-head pattern, its faded tones matching the weathered stone archway base, draped over the stone archway's base, only one patterned corner visible, an object not a living creature, isolated on transparent background.` |
| O12 | 狐形針插 | Zone 1（營火） | 塞入盤好嘅繩圈 | 全藏 | `[共用風格咒語+色調] A small fox-shaped pincushion charm, its felt tone matching the coiled rope's fiber, tucked into coiled rope, only partially visible, isolated on transparent background.` |
| O13 | 果醬樽狐紋 | Zone 3（岩地） | 塞入散落石堆之間 | 半遮 | `[共用風格咒語+色調] A small preserve jar with a hand-drawn Rüppell's fox illustration on its label, its glass tone matching the pale stones around it, tucked among scattered stones, an object not a living creature, isolated on transparent background.` |
| O14 | 狐形風箏 | Zone 2（拱門） | 纏喺拱門頂部 | 半遮 | `[共用風格咒語+色調] A small kite shaped like a fox face, its sandy fabric tone matching the stone archway it's tangled on, tangled near the top of the stone archway, an object not a living creature, isolated on transparent background.` |

**6件全新中東沙漠限定款式：**

| # | 款式 | Zone | 指定錨點 | 難度 | Prompt |
|---|---|---|---|---|---|
| N1 | 黃銅油燈狐紋 | Zone 1（營火） | 直接放喺營火邊 | 明處 | `[共用風格咒語+色調] A small brass oil lantern with a fox silhouette cut into its side, its warm glow matching the campfire beside it, glowing warmly near the campfire, an object not a living creature, isolated on transparent background, full item visible.` |
| N2 | 陶罐雕刻狐紋 | Zone 2（拱門） | 靠住石拱門牆身 | 半遮 | `[共用風格咒語+色調] A ceramic amphora jar with a fox pattern etched into its surface, its clay tone matching the stone archway it leans against, leaning against the stone archway, an object not a living creature, isolated on transparent background.` |
| N3 | 駱駝鞍飾 | Zone 1（營火） | 直接掛喺休息嗰隻駱駝嘅挽具 | 半遮 | `[共用風格咒語+色調] A woven camel saddle charm shaped like a small fox, hanging from the resting camel's harness, an object not a living creature, isolated on transparent background.` |
| N4 | 貝都因披肩狐紋 | Zone 3（岩地） | 搭喺尖角岩石上 | 半遮 | `[共用風格咒語+色調] A woven bedouin shawl with a fox pattern, its faded indigo tones matching the moonlit rock it drapes over, draped over a jagged rock, an object not a living creature, isolated on transparent background.` |
| N5 | 星盤狐座 | Zone 2（拱門） | 半埋喺廢墟旁邊嘅沙地 | 全藏 | `[共用風格咒語+色調] A small brass astrolabe marked with a tiny fox-shaped constellation, its brass tone dulled by sand matching the dune it's buried in, tucked half-buried in sand near the ruins, an object not a living creature, isolated on transparent background.` |
| N6 | 香料罐狐紋 | Zone 3（岩地） | 放喺平石面近第二個火堆 | 明處 | `[共用風格咒語+色調] A small spice jar with a fox-head label, its warm terracotta tone echoing the second fire's glow beside it, resting on a flat stone near the second fire, an object not a living creature, isolated on transparent background, full item visible.` |

---

## C. Tier C：純局部線索（7件）

| # | Zone | 指定錨點 | 難度 | Prompt |
|---|---|---|---|---|
| C1 | Zone 1（營火） | 營火周圍嘅細沙 | 全藏 | `[共用風格咒語+色調] A trail of small fox-paw footprints pressed into fine desert sand near a campfire, isolated on transparent background.` |
| C2 | Zone 2（拱門） | 石拱門背後 | 全藏 | `[共用風格咒語+色調] A fox tail tip with a black-and-white pattern peeking out from behind the stone archway, isolated on transparent background.` |
| C3 | Zone 3（岩地） | 尖角岩石表面 | 全藏 | `[共用風格咒語+色調] A faint fox-shaped shadow cast on a jagged rock by moonlight, isolated on transparent background.` |
| C4 | Zone 2（拱門） | 廢墟牆身裂縫 | 全藏 | `[共用風格咒語+色調] A pair of fox ears barely visible poking out from a crack in the ruins wall, isolated on transparent background.` |
| C5 | Zone 1（營火） | 疊起嘅鞍袋背後 | 全藏 | `[共用風格咒語+色調] A fox nose and whiskers peeking out from behind stacked saddle bags, isolated on transparent background.` |
| C6 | Zone 3（岩地） | 岩石罅隙 | 全藏 | `[共用風格咒語+色調] A set of small fox-paw footprints trailing into a rocky crevice, isolated on transparent background.` |
| C7 | Zone 2（拱門） | 倒塌石柱之間嘅暗隙 | 全藏 | `[共用風格咒語+色調] A faint pair of glowing fox eyes visible in a dark gap between fallen columns, isolated on transparent background.` |

---

## 數量清點（Level 7）

| Tier | 內容 | 數量 |
|---|---|---|
| A | 沿用v2（11主角+3+1客串） | 15 |
| B | 14件reskin＋6件全新（30%新款式） | 20 |
| C | 純局部線索 | 7 |
| **合計** | | **42** |
