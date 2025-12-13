#!/usr/bin/env python3
"""
Generate small icons for embino.com in circuit/terminal aesthetic.
Green lines on black, geometric, minimal.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Icons needed:
# Pipeline: write, gear, package, plug
# Use cases: lightbulb, thermometer, robot

ICONS = {
    "icon_write": {
        "prompt": """Minimal icon of a pencil or writing tool.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        Simple geometric strokes - like a technical diagram.
        No fill, just clean outlines.
        Like an icon from a terminal UI or circuit schematic.
        256x256 pixels, crisp edges, no gradients, no shadows.""",
    },
    "icon_gear": {
        "prompt": """Minimal icon of a gear/cog.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        Simple geometric - 6 or 8 teeth, clean circle.
        Like a technical diagram or schematic symbol.
        No fill, just clean outlines.
        256x256 pixels, crisp edges, no gradients.""",
    },
    "icon_package": {
        "prompt": """Minimal icon of a cube/box/package.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        3D cube wireframe, simple perspective.
        Like a technical diagram or CAD wireframe.
        No fill, just clean geometric lines.
        256x256 pixels, crisp edges.""",
    },
    "icon_plug": {
        "prompt": """Minimal icon of an electrical plug or connector.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        Simple geometric - like a USB or pin connector symbol.
        Technical/schematic style, not realistic.
        No fill, just clean outlines.
        256x256 pixels, crisp edges.""",
    },
    "icon_lightbulb": {
        "prompt": """Minimal icon of a lightbulb.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        Simple geometric bulb shape with filament lines.
        Like a circuit schematic symbol for a lamp.
        No fill, just clean outlines.
        256x256 pixels, crisp edges.""",
    },
    "icon_thermometer": {
        "prompt": """Minimal icon of a thermometer or temperature sensor.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        Simple geometric - vertical bar with bulb at bottom.
        Like a technical diagram or sensor symbol.
        No fill, just clean outlines.
        256x256 pixels, crisp edges.""",
    },
    "icon_robot": {
        "prompt": """Minimal icon of a robot head or simple robot.
        Pure black background (#0C0C0C).
        Electric green (#33FF33) lines only.
        Simple geometric - square head, antenna, dot eyes.
        Like a retro ASCII art robot or circuit symbol.
        No fill, just clean outlines.
        256x256 pixels, crisp edges.""",
    },
}

def generate_icons(output_dir: Path):
    """Generate all icons."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("❌ google-genai not installed")
        sys.exit(1)
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found")
    
    client = genai.Client(api_key=api_key)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for name, data in ICONS.items():
        print(f"\n🎨 Generating: {name}")
        save_path = output_dir / f"{name}.png"
        
        prompt = data["prompt"] + "\n\nCRITICAL: Pure geometric line art. No photorealism. No 3D rendering. Just clean vector-like lines on black."
        
        try:
            response = client.models.generate_content(
                model="gemini-3-pro-image-preview",
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                    image_config=types.ImageConfig(
                        aspect_ratio="1:1",
                        image_size="256"
                    ),
                )
            )
            
            for part in response.parts:
                if part.text:
                    print(f"   Note: {part.text[:50]}...")
                elif image := part.as_image():
                    image.save(str(save_path))
                    print(f"✅ Saved: {save_path}")
                    break
                    
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    output = Path(__file__).parent.parent / "images" / "icons"
    generate_icons(output)
    print(f"\n✅ Icons saved to: {output}")

