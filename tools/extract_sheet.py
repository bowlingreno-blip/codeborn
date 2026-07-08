#!/usr/bin/env python3
"""CODEBORN sheet extractor.
Slices a magenta-keyed sprite sheet (see docs/codeborn_sheet_prompt.md)
into 64x64 indexed sprites ready to paste into the game's HAND table.

Usage: python3 extract_sheet.py sheet.png [rows] [cols] > sprites.json
"""
import sys, json
from PIL import Image

def ismag(p): return p[0]>150 and p[2]>150 and p[1]<min(p[0],p[2])*0.6

def table_bounds(img):
    W,H=img.size; px=img.load()
    def rowdark(y): return sum(1 for x in range(0,W,4) if max(px[x,y][:3])<70)
    def coldark(x,t,b): return sum(1 for y in range(t,b,4) if max(px[x,y][:3])<70)
    top=next((y for y in range(40,H//3) if rowdark(y)>W//8), 0)
    bot=next((y for y in range(H-1,H-H//4,-1) if rowdark(y)>W//8), H-1)
    left=next((x for x in range(0,W//6) if coldark(x,top,bot)>(bot-top)//8), 0)
    right=next((x for x in range(W-1,W-W//6,-1) if coldark(x,top,bot)>(bot-top)//8), W-1)
    return left,top,right,bot

def extract_cell(img,L,T,R,B,r,c,rows,cols,out_size=64,colors=14):
    x0=L+(R-L)*c/cols+8; x1=L+(R-L)*(c+1)/cols-8
    y0=T+(B-T)*r/rows+8; y1=T+(B-T)*(r+1)/rows-8
    crop=img.crop((int(x0),int(y0),int(x1),int(y1))).convert('RGBA')
    W2,H2=crop.size; p=crop.load()
    minx,miny,maxx,maxy=W2,H2,0,0
    for y in range(H2):
        for x in range(W2):
            pix=p[x,y]
            edge=(x<4 or y<4 or x>W2-5 or y>H2-5)
            dark=max(pix[:3])<60
            if ismag(pix) or (edge and dark): p[x,y]=(0,0,0,0)
            elif pix[3]>0:
                minx=min(minx,x);maxx=max(maxx,x);miny=min(miny,y);maxy=max(maxy,y)
    if maxx<=minx: return None
    crop=crop.crop((minx,miny,maxx+1,maxy+1))
    w,h=crop.size; side=max(w,h)
    sq=Image.new('RGBA',(side,side),(0,0,0,0)); sq.paste(crop,((side-w)//2,(side-h)//2))
    small=sq.resize((out_size,out_size),Image.NEAREST)
    rgb=small.convert('RGB').quantize(colors=colors,method=Image.MEDIANCUT).convert('RGB')
    pal={};rows_out=[];sp=small.load();qp=rgb.load()
    CH='0123456789ABCDEFGH'
    for y in range(out_size):
        row=''
        for x in range(out_size):
            if sp[x,y][3]<120: row+='.'
            else:
                cq=qp[x,y]
                if cq not in pal:
                    if len(pal)>=len(CH): cq=min(pal,key=lambda k:sum(abs(k[i]-cq[i]) for i in range(3)))
                    else: pal[cq]=CH[len(pal)]
                row+=pal[cq]
        rows_out.append(row)
    palette=['#%02X%02X%02X'%k for k,v in sorted(pal.items(),key=lambda kv:kv[1])]
    return {'pal':palette,'rows':rows_out}

if __name__=='__main__':
    path=sys.argv[1]; nrows=int(sys.argv[2]) if len(sys.argv)>2 else 5; ncols=int(sys.argv[3]) if len(sys.argv)>3 else 8
    img=Image.open(path).convert('RGBA')
    L,T,R,B=table_bounds(img)
    out={}
    for r in range(nrows):
        for c in range(ncols):
            e=extract_cell(img,L,T,R,B,r,c,nrows,ncols)
            if e: out[f"{r}_{c}"]=e
    json.dump(out,sys.stdout)
    print(f"\n# extracted {len(out)}/{nrows*ncols}",file=sys.stderr)
