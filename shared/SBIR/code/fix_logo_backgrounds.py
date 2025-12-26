#!/usr/bin/env python3
"""
Fix logo backgrounds - replace pure black with transparency.
"""

from pathlib import Path
from PIL import Image

def make_black_transparent(image_path: Path, threshold: int = 30):
    """Replace near-black pixels with transparency."""
    img = Image.open(image_path).convert('RGBA')
    pixels = img.load()
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # If pixel is near-black, make it transparent
            if r < threshold and g < threshold and b < threshold:
                pixels[x, y] = (r, g, b, 0)
    
    img.save(image_path)
    print(f"✅ Fixed: {image_path.name}")

if __name__ == "__main__":
    team_dir = Path(__file__).parent.parent / "images" / "team"
    
    logos = [
        "logo_apple.png",
        "logo_intel.png", 
        "logo_nature.png",
        "logo_embryonics.png",
    ]
    
    for logo in logos:
        logo_path = team_dir / logo
        if logo_path.exists():
            make_black_transparent(logo_path)
        else:
            print(f"❌ Not found: {logo}")
    
    print("\n✅ Done! Logos now have transparent backgrounds.")
