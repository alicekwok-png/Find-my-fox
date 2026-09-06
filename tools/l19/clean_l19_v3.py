from PIL import Image
import numpy as np, glob, os, sys, cv2
root="find-my-fox-level17-19-assets/level19"
out=root+"/clean"; os.makedirs(out,exist_ok=True)
files=sorted(glob.glob(root+"/characters/*.png"))+sorted(glob.glob(root+"/objects/*.png"))+sorted(glob.glob(root+"/clues/*.png"))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for f in files[lo:hi]:
    im=Image.open(f).convert("RGBA"); a=np.array(im); h,w=a.shape[:2]
    al=a[:,:,3].astype(np.int16); rgb=a[:,:,:3]
    r=rgb.astype(np.int16); mx=r.max(axis=2); mn=r.min(axis=2); neutral=(mx-mn)<=4
    op=(al==255)
    cand = op & neutral & ((mn>=252) | ((mn>=236)&(mx<=242)))
    zero = (al==0)
    passable=(zero|cand).astype(np.uint8)
    n,lab=cv2.connectedComponents(passable, connectivity=8)
    border=set(np.unique(np.concatenate([lab[0,:],lab[-1,:],lab[:,0],lab[:,-1]])).tolist()); border.discard(0)
    reached=np.isin(lab,list(border))
    remove = (cand|zero) & reached
    fill   = (cand|zero) & ~reached          # enclosed holes -> restore artwork
    bgr=cv2.cvtColor(a[:,:,:3], cv2.COLOR_RGB2BGR).copy()
    if fill.any():
        bgr=cv2.inpaint(bgr, fill.astype(np.uint8)*255, 5, cv2.INPAINT_TELEA)
    rgb2=cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    a[:,:,:3]=rgb2
    a[:,:,3][fill]=255
    a[:,:,3][remove]=0; a[:,:,0][remove]=0; a[:,:,1][remove]=0; a[:,:,2][remove]=0
    alv=(a[:,:,3]>0).astype(np.uint8)
    n2,lab2,stats,_=cv2.connectedComponentsWithStats(alv, connectivity=8)
    small=[i for i in range(1,n2) if stats[i,cv2.CC_STAT_AREA]<400]
    if small:
        m=np.isin(lab2,small); a[:,:,3][m]=0; a[:,:,:3][m]=0
    im2=Image.fromarray(a,"RGBA"); bb=im2.getbbox(); im2=im2.crop(bb)
    im2.save(os.path.join(out,os.path.basename(f)))
    print(f"{os.path.basename(f):50s} -> {im2.size[0]}x{im2.size[1]} fill={100*fill.mean():.2f}% speckles={len(small)}")
