# frame.py <png> <W> <H> <barBottom>: the journey's wafer rule (lum > 34 under the bar) on a saved step frame
import sys
from PIL import Image
p, W, H, yb = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
# optional mask x0,y0,x1,y1 (the SEE THROUGH strip, chrome not wafer, as the script masks #kuiper-star-strip)
M = [int(v) for v in sys.argv[5].split(',')] if len(sys.argv) > 5 else None
im = Image.open(p).convert('RGB'); print('png', im.size)
im = im.resize((W, H), Image.BILINEAR); d = im.load()
lit = tot = 0; minx = miny = 10**9; maxx = maxy = -1
for y in range(max(0, int(yb)), H):
    for x in range(W):
        if M and M[0] <= x <= M[2] and M[1] <= y <= M[3]: continue
        r, g, b = d[x, y]; tot += 1
        if 0.299*r + 0.587*g + 0.114*b > 34:
            lit += 1; minx = min(minx, x); miny = min(miny, y); maxx = max(maxx, x); maxy = max(maxy, y)
bw, bh = maxx-minx+1, maxy-miny+1
whole = bw > 0.4*min(W, H-yb) and abs(bw/bh-1) < 0.25 and miny >= yb-1 and maxy <= H
print({'bbox': [minx, miny, maxx, maxy], 'bboxW': bw, 'bboxH': bh, 'ratio': round(min(bw, bh)/max(bw, bh), 3), 'litFraction': round(lit/tot, 4), 'whole_by_script_rule': whole})
