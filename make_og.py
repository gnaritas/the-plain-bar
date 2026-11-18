#!/usr/bin/env python3
"""og.png 1200x630 — The Plain Bar (2x supersample).
Poster share art: deep espresso field with faint hairline grid, tracked brass
eyebrow, cream serif masthead, amber event line, plain geometric ring motif.
Shop identity only — no builder markers, no photo claims."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

INK = (23, 18, 14); INK2 = (30, 23, 17); LINE = (56, 44, 28)
CREAM = (241, 231, 212); BRASS = (200, 162, 75); AMBER = (226, 180, 94); MUTE = (163, 148, 124)

def font(paths, size):
    bases = ["/System/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size * S)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Georgia Bold Italic.ttf", "Georgia Bold.ttf", "Palatino Bold.ttc", "Times New Roman Bold.ttf"], s)
sans  = lambda s: font(["Avenir Next.ttc", "HelveticaNeue.ttc", "Helvetica.ttc"], s)

img = Image.new("RGB", (W * S, H * S), INK)
d = ImageDraw.Draw(img)
px = lambda x, y: (int(x * S), int(y * S))

# faint hairline grid field
for xx in range(60, W - 30, 56):
    d.line([px(xx, 0), px(xx, H)], fill=INK2, width=1 * S)
for yy in range(60, H - 30, 56):
    d.line([px(0, yy), px(W, yy)], fill=INK2, width=1 * S)
# soft vertical warming toward bottom
for yy in range(H // 2, H, 6):
    a = (yy - H // 2) / (H // 2)
    d.rectangle([0, yy * S, W * S, (yy + 6) * S], fill=(
        int(INK[0] + (INK2[0] - INK[0]) * a * 0.7),
        int(INK[1] + (INK2[1] - INK[1]) * a * 0.7),
        int(INK[2] + (INK2[2] - INK[2]) * a * 0.7)))

def tracked(x, y, text, fnt, fill, sp):
    cx = x * S
    for ch in text:
        d.text((cx, y * S), ch, font=fnt, fill=fill)
        cx += d.textlength(ch, font=fnt) + sp * S

def left(x, y, text, fnt, fill):
    d.text((x * S, y * S), text, font=fnt, fill=fill)

tracked(72, 96, "OPENING SOON · LONGVIEW MALL · LONGVIEW, TEXAS", sans(21), BRASS, 2.6)
tracked(68, 150, "THE PLAIN BAR", serif(120), CREAM, 1.2)
left(72, 318, "SUNDAY BRUNCHES · BOOK NIGHTS · COCKTAIL CLASSES", sans(24), AMBER)
d.rectangle([72 * S, 384 * S, (72 + 380) * S, (384 + 4) * S], fill=BRASS)
left(72, 412, "A new neighborhood bar inside Longview Mall.", sans(24), CREAM)
left(72, 448, "3500 McCann Rd STE H07B · Longview, TX 75604", sans(21), MUTE)
left(72, 484, "Planned opening: mid-January 2027", sans(21), MUTE)

# plain geometric motif (right): concentric hairline rings + one filled dot
cx, cy = 985, 330
d.ellipse([px(cx - 150, cy - 150), px(cx + 150, cy + 150)], outline=(84, 64, 36), width=2 * S)
d.ellipse([px(cx - 108, cy - 108), px(cx + 108, cy + 108)], outline=BRASS, width=2 * S)
d.ellipse([px(cx - 66, cy - 66), px(cx + 66, cy + 66)], outline=(84, 64, 36), width=2 * S)
d.ellipse([px(cx - 13, cy - 13), px(cx + 13, cy + 13)], fill=BRASS)

# fine frame
d.rectangle([16 * S, 16 * S, (W - 16) * S, (H - 16) * S], outline=(64, 50, 28), width=2 * S)

img = img.resize((W, H), Image.LANCZOS)
img.save(OUT, "PNG", optimize=True)
print("og.png", os.path.getsize(OUT), "bytes")
