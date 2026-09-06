from PIL import Image
import numpy as np, cv2, glob, os, sys
files=sorted(glob.glob("find-my-fox-level17-19-assets/level19/clean/*.png"))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
k=np.ones((5,5),np.uint8)
for f in files[lo:hi]:
    a=np.array(Image.open(f).convert("RGBA"))
    for _ in range(3):
        al=a[:,:,3]; r=a[:,:,:3].astype(np.int16)
        mx=r.max(2); mn=r.min(2)
        light=(al==255)&((mx-mn)<=16)&(mn>=212)
        near=cv2.dilate((al==0).astype(np.uint8),k,iterations=1).astype(bool)
        rm=light&near
        if not rm.any(): break
        a[:,:,3][rm]=0; a[:,:,:3][rm]=0
    alv=(a[:,:,3]>0).astype(np.uint8)
    n,lab,stats,_=cv2.connectedComponentsWithStats(alv,connectivity=8)
    small=[i for i in range(1,n) if stats[i,cv2.CC_STAT_AREA]<400]
    if small:
        m=np.isin(lab,small); a[:,:,3][m]=0; a[:,:,:3][m]=0
    im=Image.fromarray(a,"RGBA"); bb=im.getbbox(); im=im.crop(bb); im.save(f)
    print(os.path.basename(f),"->",im.size)
