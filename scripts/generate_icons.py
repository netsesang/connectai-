import os
from PIL import Image, ImageDraw, ImageFilter

def make_squircle_mask(size, radius, supersample=4):
    w, h = size
    sw, sh = w * supersample, h * supersample
    sr = radius * supersample
    
    mask = Image.new('L', (sw, sh), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), (sw, sh)], radius=sr, fill=255)
    
    # Downsample with Lanczos for silky smooth antialiasing
    return mask.resize((w, h), Image.Resampling.LANCZOS)

def generate_icon():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = os.path.join(base_dir, 'assets', 'icon.png')
    out_ico_path = os.path.join(base_dir, 'assets', 'icon.ico')
    out_png_path = os.path.join(base_dir, 'assets', 'icon_rounded.png')

    if not os.path.exists(src_path):
        print(f"Error: {src_path} not found.")
        return

    img = Image.open(src_path).convert('RGBA')
    w, h = img.size

    # Ensure square 1024x1024
    if w != h:
        dim = min(w, h)
        left = (w - dim) // 2
        top = (h - dim) // 2
        img = img.crop((left, top, left + dim, top + dim))
    
    img = img.resize((1024, 1024), Image.Resampling.LANCZOS)

    # 1. Generate smooth squircle mask (radius: 220px for modern iOS/macOS/Win11 style squircle)
    mask = make_squircle_mask((1024, 1024), radius=220)

    # 2. Composite with rounded mask
    rounded = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
    rounded.paste(img, (0, 0), mask=mask)

    # Add a subtle elegant 1px border for crisp contrast on any desktop background
    border_mask = make_squircle_mask((1024, 1024), radius=220)
    border_draw = ImageDraw.Draw(rounded)
    # Highlight rim
    border_draw.rounded_rectangle([(1, 1), (1023, 1023)], radius=220, outline=(255, 255, 255, 40), width=2)

    rounded.save(out_png_path, 'PNG')
    print(f"Saved: {out_png_path}")

    # 3. Save multi-resolution Windows ICO
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    rounded.save(out_ico_path, format='ICO', sizes=sizes)
    print(f"Saved: {out_ico_path} with sizes {sizes}")

if __name__ == '__main__':
    generate_icon()
