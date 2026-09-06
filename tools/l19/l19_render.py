from PIL import Image, ImageDraw
import sys, os
sys.path.insert(0,os.path.expanduser("~"))
from l19_spec import SPEC
BG="find-my-fox-level17-19-assets/level19/background/L19_background_v5_3440x1920.jpg"
CL="find-my-fox-level17-19-assets/level19/clean/"
bg=Image.open(BG).convert("RGBA")
label = len(sys.argv)>1 and sys.argv[1]=="label"
for tid,f,anc,x,y,h,tier,kls,sr in SPEC:
    im=Image.open(CL+f).convert("RGBA")
    w=int(round(h*im.size[0]/im.size[1]))
    im=im.resize((w,h), Image.LANCZOS)
    bg.alpha_composite(im,(x-w//2,y-h//2))
if label:
    d=ImageDraw.Draw(bg)
    for tid,f,anc,x,y,h,tier,kls,sr in SPEC:
        im=Image.open(CL+f); w=int(round(h*im.size[0]/im.size[1]))
        d.rectangle([x-w//2,y-h//2,x+w//2,y+h//2], outline=(255,0,255,255), width=3)
        d.text((x-w//2+4,y-h//2+4), tid, fill=(255,0,255))
out="_qa_l19_composite%s.jpg"%("_label" if label else "")
bg.convert("RGB").resize((2064,1152), Image.LANCZOS).save(out, quality=90)
bg.convert("RGB").save("_qa_l19_composite_full.jpg", quality=88)
print("saved",out)
