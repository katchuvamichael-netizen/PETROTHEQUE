from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

root = Path(__file__).resolve().parent
icons_dir = root / 'icons'
icons_dir.mkdir(exist_ok=True)


def draw_icon(size, out_name):
    img = Image.new('RGBA', (size, size), (7, 17, 31, 255))
    draw = ImageDraw.Draw(img)

    # Background with subtle radial-like shading
    for y in range(size):
        tone = 7 + int((y / size) * 18)
        draw.line((0, y, size, y), fill=(tone, 17 + int((y / size) * 14), 31 + int((y / size) * 18), 255))

    # Outer circular badge
    margin = int(size * 0.12)
    radius = size // 2 - margin
    draw.ellipse((margin, margin, size - margin, size - margin), fill=(12, 25, 39, 255), outline=(103, 232, 249, 255), width=max(3, int(size * 0.02)))
    draw.ellipse((int(size * 0.2), int(size * 0.2), size - int(size * 0.2), size - int(size * 0.2)), outline=(103, 232, 249, 90), width=max(2, int(size * 0.012)))

    # Rock layers at bottom
    rock_a = [
        (int(size * 0.22), int(size * 0.62)),
        (int(size * 0.35), int(size * 0.50)),
        (int(size * 0.46), int(size * 0.58)),
        (int(size * 0.56), int(size * 0.40)),
        (int(size * 0.66), int(size * 0.52)),
        (int(size * 0.76), int(size * 0.42)),
        (int(size * 0.84), int(size * 0.62)),
        (int(size * 0.84), int(size * 0.82)),
        (int(size * 0.22), int(size * 0.82)),
    ]
    rock_b = [
        (int(size * 0.18), int(size * 0.74)),
        (int(size * 0.30), int(size * 0.68)),
        (int(size * 0.42), int(size * 0.70)),
        (int(size * 0.52), int(size * 0.58)),
        (int(size * 0.62), int(size * 0.68)),
        (int(size * 0.74), int(size * 0.60)),
        (int(size * 0.88), int(size * 0.74)),
        (int(size * 0.88), int(size * 0.86)),
        (int(size * 0.18), int(size * 0.86)),
    ]
    draw.polygon(rock_a, fill=(150, 162, 177, 220))
    draw.polygon(rock_b, fill=(238, 245, 250, 255))

    # Crystal form in center
    crystal = [
        (size // 2, int(size * 0.22)),
        (int(size * 0.63), int(size * 0.31)),
        (int(size * 0.63), int(size * 0.50)),
        (size // 2, int(size * 0.60)),
        (int(size * 0.37), int(size * 0.50)),
        (int(size * 0.37), int(size * 0.31)),
    ]
    draw.polygon(crystal, fill=(34, 211, 238, 255))

    # Crystal facets
    draw.line((size // 2, int(size * 0.22), size // 2, int(size * 0.60)), fill=(255, 255, 255, 220), width=max(3, int(size * 0.02)))
    draw.line((int(size * 0.37), int(size * 0.31), size // 2, int(size * 0.40), int(size * 0.63), int(size * 0.31)), fill=(255, 255, 255, 190), width=max(2, int(size * 0.015)))
    draw.line((int(size * 0.37), int(size * 0.50), size // 2, int(size * 0.40), int(size * 0.63), int(size * 0.50)), fill=(255, 255, 255, 190), width=max(2, int(size * 0.015)))

    # Monogram P inside crystal
    draw.rounded_rectangle((int(size * 0.42), int(size * 0.32), int(size * 0.58), int(size * 0.60)), radius=max(6, int(size * 0.06)), fill=(248, 250, 252, 255))
    draw.rectangle((int(size * 0.46), int(size * 0.34), int(size * 0.50), int(size * 0.58)), fill=(7, 17, 31, 255))
    draw.rectangle((int(size * 0.46), int(size * 0.34), int(size * 0.56), int(size * 0.39)), fill=(7, 17, 31, 255))

    # Little dots for mineral points
    for x in [int(size * 0.28), int(size * 0.72)]:
        for y in [int(size * 0.30), int(size * 0.48)]:
            draw.ellipse((x - max(4, int(size * 0.02)), y - max(4, int(size * 0.02)), x + max(4, int(size * 0.02)), y + max(4, int(size * 0.02))), fill=(103, 232, 249, 255))

    img.save(icons_dir / out_name, format='PNG')


for size, name in [(192, 'icon-192.png'), (512, 'icon-512.png'), (180, 'apple-touch-icon.png')]:
    draw_icon(size, name)

print(f'Icons generated in {icons_dir}')
