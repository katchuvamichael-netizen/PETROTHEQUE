from PIL import Image, ImageDraw, ImageFont

W, H = 512, 512
img = Image.new('RGBA', (W, H), (7, 17, 31, 255))
draw = ImageDraw.Draw(img)

# Background circle
draw.ellipse((30, 30, 482, 482), fill=(12, 25, 39, 255), outline=(103, 232, 249, 255), width=6)
draw.ellipse((62, 62, 450, 450), outline=(103, 232, 249, 80), width=2)

# Layered rock base
points1 = [(120, 310), (170, 248), (220, 300), (290, 198), (345, 258), (392, 220), (422, 306), (422, 390), (120, 390)]
draw.polygon(points1, fill=(139, 148, 163, 220))
points2 = [(110, 350), (165, 310), (205, 340), (248, 290), (300, 334), (350, 300), (406, 340), (440, 350), (440, 410), (110, 410)]
draw.polygon(points2, fill=(232, 240, 235, 255))

# Crystal form
crystal = [
    (256, 120),
    (332, 160),
    (332, 248),
    (256, 292),
    (180, 248),
    (180, 160)
]
draw.polygon(crystal, fill=(34, 211, 238, 255))

# Inner facets
for line in [((256, 120), (256, 292)), ((180, 160), (256, 198), (332, 160)), ((180, 248), (256, 214), (332, 248))]:
    if len(line) == 2:
        draw.line(line, fill=(255, 255, 255, 220), width=5)
    else:
        draw.line(line, fill=(255, 255, 255, 200), width=4)

# Stylized P in the center
p_box = (218, 140, 288, 282)
draw.rounded_rectangle(p_box, radius=18, fill=(248, 250, 252, 255))
# Stem + bowl
stem = (228, 150, 244, 272)
draw.rectangle(stem, fill=(7, 17, 31, 255))
# Bowl
bowl = [(244, 160), (286, 160), (286, 200), (244, 200)]
draw.polygon(bowl, fill=(7, 17, 31, 255))
# Inner cut
cut = (250, 180, 280, 195)
draw.rectangle(cut, fill=(248, 250, 252, 255))

# Small orbit dots
for x in [182, 332, 182, 332]:
    draw.ellipse((x-6, 170-6, x+6, 170+6), fill=(103, 232, 249, 255))
for x in [182, 332]:
    draw.ellipse((x-6, 240-6, x+6, 240+6), fill=(103, 232, 249, 255))

# Text label
try:
    font = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 26)
except Exception:
    font = ImageFont.load_default()
label = 'PETROLOGIE'
text_bbox = draw.textbbox((0, 0), label, font=font)
text_w = text_bbox[2] - text_bbox[0]
text_x = (W - text_w) / 2
text_y = 398
# Add subtle shadow
for offset in [(1,2), (0,1)]:
    draw.text((text_x+offset[0], text_y+offset[1]), label, font=font, fill=(30, 41, 59, 180))
draw.text((text_x, text_y), label, font=font, fill=(226, 232, 240, 255))

img.save('petrologie-logo.png')
print('Generated petrologie-logo.png')
