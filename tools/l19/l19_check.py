from PIL import Image
import os, sys
sys.path.insert(0,os.path.expanduser("~"))
from l19_spec import SPEC, NOGO
CL="find-my-fox-level17-19-assets/level19/clean/"
W,H=3440,1920
boxes={}
print("=== geometry ===")
for tid,f,anc,x,y,h,tier,kls,sr in SPEC:
    im=Image.open(CL+f); w=int(round(h*im.size[0]/im.size[1]))
    x0,y0,x1,y1=x-w//2,y-h//2,x-w//2+w,y-h//2+h
    boxes[tid]=(x0,y0,x1,y1,w,h)
    warn=""
    if x0<0 or y0<0 or x1>W or y1>H: warn+=" OUT-OF-CANVAS"
    for n,(a,b,c,d) in NOGO.items():
        if x0<c and x1>a and y0<d and y1>b: warn+=f" NOGO:{n}"
    print(f"{tid:9s} {f[4:34]:32s} box=({x0},{y0})-({x1},{y1}) {w}x{h}{warn}")
print("=== pairwise overlap > 25% of smaller ===")
ids=list(boxes)
for i in range(len(ids)):
    for j in range(i+1,len(ids)):
        a=boxes[ids[i]]; b=boxes[ids[j]]
        ox=max(0,min(a[2],b[2])-max(a[0],b[0])); oy=max(0,min(a[3],b[3])-max(a[1],b[1]))
        ar=ox*oy
        if ar<=0: continue
        sm=min(a[4]*a[5],b[4]*b[5])
        if ar/sm>0.25: print(f"  {ids[i]} <-> {ids[j]}  {100*ar/sm:.0f}% of smaller")
