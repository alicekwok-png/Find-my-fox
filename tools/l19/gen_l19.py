# -*- coding: utf-8 -*-
from PIL import Image
import sys, os
sys.path.insert(0,os.path.expanduser("~"))
from l19_spec import SPEC
CL="find-my-fox-level17-19-assets/level19/clean/"
EN={
"fox_01":"sitting on its own basalt stump on the rock shelf left of the tidepool",
"fox_02":"peeking from behind its own grass tuft on the turf right of the brown dog",
"fox_03":"in the shadow of its own net shed against the cliff foot, left of the beached boat",
"fox_04":"standing on the flat top of the sea stack",
"fox_05":"juvenile peeking out of the driftwood pile on the headland",
"fox_06":"older fox sitting on the rock shelf left of the boy",
"fox_07":"trotting across the open turf below the driftwood",
"fox_08":"sitting beside its own rope ladder on the right cliff's rock ledge, left of the painted ladder",
"fox_09":"lying among its own tidepool rocks at the pool's left edge",
"fox_10":"peeking from the left side of the big lobster crate",
"fox_11":"mid-pounce in its own tidepool splash",
"fox_12":"cross fox sitting by its own hut on the rocks behind the beached boat",
"fox_13":"cross fox peeking from behind its own upturned boat beside the beached one",
"fox_14":"cross fox hidden in the foreground driftwood raft",
"fox_15":"arctic fox on the rock face below and right of the puffin ledge",
"obj_E1":"measuring tape lying on the ground at the spread net's right edge",
"obj_E2":"specimen jar standing among the shells at the bottom-right of the shore",
"obj_N1":"fishing float hanging on the shed wall right of the door",
"obj_N2":"fox pawprint on the puffin rock right of the painted puffins",
"obj_N3":"net scoop lying at the tidepool's right waterline",
"obj_N4":"shell windchime hanging under the shed's left eave; its hook is the connector",
"obj_O1":"mug on its own crab traps in the fishing gear on the shore",
"obj_O2":"blanket draped over the spread net's right half",
"obj_O3":"cookie on its own rope mat on the grass left of the picnic blanket",
"obj_O4":"knitted plush on its own rug at the blanket's right edge, beside the child",
"obj_O5":"thermos and rolled mat on the grass below the picnic blanket",
"obj_O6":"salt and pepper pair on the rock face below the puffin ledge",
"obj_O7":"tail keychain hooked on the painted rope ladder's rung; the ring is the connector",
"obj_O8":"knitted ear hat resting on the rock shelf left of the tidepool",
"obj_O9":"windchime hanging from its own lantern post planted on the headland turf",
"obj_O10":"field guide lying open among the shells at the tidepool's front edge",
"obj_O11":"scarf draped over the foreground driftwood",
"obj_O12":"pincushion tucked in the coiled net at the spread net's left edge",
"obj_O13":"preserve jar standing on the big lobster crate's lid",
"clue_C1":"print trail pressed into the turf left of the sleeping dog",
"clue_C2":"only the tail, out from under the picnic blanket's lower edge",
"clue_C3":"ear tips showing between the foreground rocks",
"clue_C4":"fox-shaped shadow on the net shed's plank wall",
"clue_C5":"nose and eyes in the gap under the foreground driftwood",
"clue_C6":"glowing eyes in the crevice at the sea stack's base",
}
def species(tid,f):
    if f.startswith("L19_A1") and f[5:8] in ("A12","A13","A14"): return "cross_fox"
    if "arctic" in f: return "arctic_fox"
    return "blue_fox"
def ttype(tid):
    if tid.startswith("fox_"):
        n=int(tid.split("_")[1]); return "hero_fox" if n<=11 else "cameo_fox"
    if tid.startswith("obj_"): return "fox_object"
    return "partial_clue"
IMPRINT={"clue_C4","clue_C1"}
lines=[]
sec=None
for tid,f,anc,x,y,h,tier,kls,sr in SPEC:
    w=int(round(h*Image.open(CL+f).size[0]/Image.open(CL+f).size[1]))
    tt=ttype(tid); sp=species(tid,f)
    head=None
    if tid=="fox_01": head="      // ---- Tier A: blue fox hero (11) — anchors from the v3 prompts ----"
    if tid=="fox_12": head="      // ---- Tier A: cross fox cameo (3) + arctic fox cameo (1) ----"
    if tid=="obj_E1": head="      // ---- Tier B: explorer gear (2) ----"
    if tid=="obj_N1": head="      // ---- Tier B: sea-cliff only (4) ----"
    if tid=="obj_O1": head="      // ---- Tier B: family object bank (13) ----"
    if tid=="clue_C1": head="      // ---- Tier C: partial clues (6) ----"
    if head: lines.append(head)
    rnd = ' render:"imprint",' if tid in IMPRINT else ''
    lines.append(f'      {{ id:"{tid}",{rnd} target_type:"{tt}", species:"{sp}", sprite_asset: ASSET_DIR19_CLEAN + "{f}", position:{{x:{x},y:{y}}}, hitbox:{{width:{w},height:{h}}}, difficulty_tier:"{tier}", placement_class:"{kls}", anchor_ref:"{anc} — {EN[tid]}", intended_scale_ref:"{sr}" }},')
lines[-1]=lines[-1].rstrip(",")
body="\n".join(lines)
block = '''
  /* =========================================================
     Level 19 — 藍狐 Blue Fox（北極狐色型變異）／阿留申海崖
     Source: find-my-fox-level17-19-assets/level19 pack.
     §2.4.1 交收（2026-09-06）: 呢 40 個 vendor PNG 全部係「假透明」——
     四角 alpha 係 0，但畫布 60-73%%係實心不透明嘅棋盤格（淺格 RGB≈254、
     深格 RGB≈239），而且狐狸嘅白色部分（胸毛、尾尖）連格一齊被挖穿。
     clean/ 係用 clean_l19_v3.py 修好嘅版本：由邊界 8-連通 flood fill 刪走
     真背景格，包住喺造型入面嘅格用 cv2.inpaint 補返白毛，A08／O09 兩個
     （繩梯、燈柱）改為一律刪格保留真透明，再 de-fringe + tight crop。
     修完 40/40 過閘：mode==RGBA、四角 alpha==0、殘餘棋盤格 <0.5%%。
     §2.4 背景閘門: backgrounds-v5 3440x1920 = 1.792:1、高度 1920 → PASS
     （vendor 原檔 2688x1152 = 2.33:1 FAIL，唔用）。
     Scale: 米色狗蜷住 ≈303px ≈ 75cm；右邊棕狗身長 ≈344px ≈ 80cm → 1cm ≈ 4.1px。
     §2.7 face no-go boxes: 漁夫 (487-619,1078-1181), 棕狗頭左 (722-872,1296-1445),
     媽媽 (1669-1760,751-837), 細路 (1772-1835,854-929), 米色狗頭 (1606-1743,1457-1583),
     男仔 (2867-2981,1204-1308), 棕狗頭右 (3038-3165,1445-1560).
     Hiding interfaces used (§2.5): 漁屋牆 (C4, N1), 屋簷 (N4), 大木箱／蟹籠 (fox_10, O13),
     攤開漁網 (O2, O12, E1), 沙灘漁船 (fox_13, fox_12), 漂流木 (fox_05, fox_14, C5, O11),
     野餐氈 (O3, O4, O5, C2), 海鸚岩 (N2, O6), 海蝕柱 (fox_04, C6),
     背景繩梯 (O7), 潮池 (fox_01, fox_09, fox_11, O8, O10, N3, E2).
     ========================================================= */
  var ASSET_DIR19 = "find-my-fox-level17-19-assets/level19/";
  var ASSET_DIR19_CLEAN = ASSET_DIR19 + "clean/";

  var LEVEL_19 = {
    level_id: "blue_fox_seacliff_19",
    level_name: "阿留申海崖",
    theme: "blue_fox_aleutian_seacliff",
    background_asset: ASSET_DIR19 + "background/L19_background_v5_3440x1920.jpg",
    background_size: { width: 3440, height: 1920 },
    viewport_size: { width: 1080, height: 1920 },
    initial_camera_position: { x: 0, y: 0 },
    target_count_total: 40, // 15 Tier A (11 blue-fox hero + 3 cross-fox cameo + 1 arctic-fox cameo) + 19 Tier B (13 family bank + 2 explorer gear + 4 sea-cliff only) + 6 Tier C
    targets: [
%s
    ]
  };
''' % body
open("_l19_block.js","w",encoding="utf-8").write(block)
print(block[:400])
print("...lines:",len(lines))
