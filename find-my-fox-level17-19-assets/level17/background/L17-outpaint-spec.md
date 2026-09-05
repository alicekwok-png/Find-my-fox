# Level 17 背景 outpaint 規格（方案 C）

**日期：** 2026-09-05 · **原圖：** `L17_background_panorama.png` 2688×1152（2.33:1，唔合規）
**目標：** **3456×1920（1.8:1）** — 上下各加 384px，左右各加 384px。原圖置中：落喺 (384,384)–(3072,1536)。

附件：
- `L17_outpaint_canvas_3456x1920.png` — 原圖置中、四邊透明（俾 generative fill / inpaint 工具用）
- `L17_outpaint_mask_3456x1920.png` — 白＝要生成，黑＝保留原圖
- `L17_outpaint_preview.png` — 四條擴出嚟嘅帶同要求一覽

## 共用 prompt（四邊一樣）

```
Cozy storybook cartoon illustration style, thick clean black linework, soft cel-shaded coloring, family-friendly mobile hidden-object game art, detailed but readable at small size, NOT chibi, NOT photorealistic, NOT 3D render. Deep winter conifer-night palette — near-black indigo shadows under snow-laden pines, cold silver-blue moonlight, warm amber lantern glow. Seamlessly extend the existing snowy coniferous night scene outward; keep the same horizon and snowline height, the same moonlight direction, the same linework weight. No fox characters, no fox-shaped objects, no new people, no new animals, no UI.
```

## 每條帶嘅 station 要求（技術文件 §2.6 第 4 點：擴出嚟嘅範圍唔可以留空）

| 帶 | 範圍（新畫布座標） | 要生成嘅實物（俾 target 用） | 對應 target |
|---|---|---|---|
| 上 | y 0–384，全寬 | 厚壓雪松枝橫過畫面上方（最少 2–3 枝伸入畫面、有明顯枝節可以掛嘢）；左上延伸伐木小屋嘅斷屋樑同柱 | A02 松枝後探頭、O14 風箏纏樹枝、N5 屋樑燈籠 |
| 下 | y 1536–1920，全寬 | 雪地前景：散落松果堆（一堆 5–8 粒）、半埋雪嘅倒木、一對雪鞋靠住樺樹樁、平坦嘅雪面（俾影子）、新鮮雪面（俾腳印） | N2 松果雕刻、N4 雪鞋扣、C5 雪地影子、C1 腳印、A11 打滾、A14 雪堤 |
| 左 | x 0–384，y 384–1536 | 伐木小屋遺跡嘅外牆延伸（有陰影暗角）、多幾把生鏽斧頭插喺雪、切好嘅木頭堆再長一截、雪地平石 | A03 小屋牆影、N3 斧柄雕刻、O1 平石杯、O11 木頭堆圍巾、C4 木頭罅隙 |
| 右 | x 3072–3456，y 384–1536 | 深色松樹林線（樹影之間有暗位）、多 2–3 個樺樹樁、路標柱旁多一棵松樹 | C3 樹影中發光眼、A09／C6／O8 樺樹樁、A13 松樹幹後 |

## 唔可以做嘅嘢

- 唔好改動原圖範圍（家庭、兩隻馴鹿、狗、營火、雪橇、工具箱位置全部要保持）
- 唔好加新人物或新動物（搵伴一律用現有馴鹿／狗）
- 四邊嘅雪線、月光方向、線稿粗幼要同原圖一致，接口唔可以有明顯 seam

出咗圖請覆核：實際尺寸 3456×1920（我會用 code 再量一次先開工）。
