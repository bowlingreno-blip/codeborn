from PIL import Image

# ---- PIXEL STYLE BIBLE palette (Fire) ----
LEGEND = {
    '.': None,              # transparent
    'K': (58, 21, 8, 255),  # outline (dark warm brown)
    'R': (255, 90, 60, 255),# base  (Fire base)
    'D': (199, 56, 31, 255),# shadow (Fire dark)
    'H': (255, 173, 143,255),# highlight (Fire light)
    'Y': (255, 210, 63,255),# ember glow accent
    'W': (255, 255, 255,255),# eye white
}

# ---- SCORCHI  draft 1  (24x24) ----
GRID = [
    "........................",
    "...........KYK..........",
    "..........KYYYK.........",
    ".........KYYRYYK........",
    ".........KYRRRYK........",
    "........KYRRRRRYK.......",
    "........KKRRRRRKK.......",
    ".......KRRRRRRRRRK......",
    "......KRRRRRRRRRRRK.....",
    ".....KRRRRRRRRRRRRRK....",
    ".....KRRWWWRRRWWWRRK....",
    ".....KRRWKWRRRWKWRRK....",
    ".....KRRWWWRRRWWWRRK....",
    ".....KRRRRRRRRRRRRRK....",
    ".....KDRRRRRRRRRRRDK....",
    "......KRRRRRRRRRRRK.....",
    "......KDRRRHHHRRRDK.....",
    ".....KRRRHHHHHHHRRRK....",
    ".....KRRRHHHHHHHRRRK....",
    ".....KDRRRHHHHHRRRDK....",
    "......KDRRRRRRRRRDK.....",
    "......KRRK...KRRK.......",
    ".....KKKK...KKKK........",
    "........................",
]

def validate(grid):
    ok = True
    for i, row in enumerate(grid):
        if len(row) != 24:
            print(f"  ROW {i}: len {len(row)} (need 24)"); ok = False
        for ch in row:
            if ch not in LEGEND:
                print(f"  ROW {i}: bad char {ch!r}"); ok = False
    return ok

def render(grid, scale, bg=None, paint=None):
    grid = [list(r) for r in grid]
    if paint:
        for (x,y,ch) in paint:
            if 0<=y<len(grid) and 0<=x<len(grid[0]): grid[y][x]=ch
    h = len(grid); w = len(grid[0])
    img = Image.new("RGBA", (w*scale, h*scale), bg if bg else (0,0,0,0))
    px = img.load()
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            c = LEGEND[ch]
            if c is None: continue
            for dy in range(scale):
                for dx in range(scale):
                    px[x*scale+dx, y*scale+dy] = c
    return img

print("VALIDATE:", "OK" if validate(GRID) else "ERRORS ABOVE")

PAINT = [
    # left paw
    (4,13,'R'),(4,14,'R'),(3,13,'K'),(3,14,'K'),(4,15,'K'),
    # right paw
    (20,13,'R'),(20,14,'R'),(21,13,'K'),(21,14,'K'),(20,15,'K'),
    # flame tail (lower-right, curling up)
    (18,20,'R'),(19,20,'R'),(19,19,'R'),(20,19,'R'),(20,18,'Y'),(21,18,'Y'),(21,17,'Y'),
    (18,21,'K'),(19,21,'K'),(20,20,'K'),(21,19,'K'),(22,18,'K'),(22,17,'K'),(20,17,'K'),(21,16,'K'),
]

big = render(GRID, 16, paint=PAINT)
big.save("scorchi_big.png")

# readability strip on the LCD-dark background at in-game sizes
LCD = (11,18,15,255)
strip = Image.new("RGBA", (152+72+60+80, 200), LCD)
for spr_w, xoff in [(152,20),(72,192),(60,284)]:
    s = render(GRID, 6, paint=PAINT)
    s = s.resize((spr_w, spr_w), Image.NEAREST)
    strip.alpha_composite(s, (xoff, (200-spr_w)//2))
strip.save("scorchi_sizes.png")
print("saved scorchi_big.png + scorchi_sizes.png")
