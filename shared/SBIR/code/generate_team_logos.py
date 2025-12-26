#!/usr/bin/env python3
"""
Generate simple company logos for Team slide.
Minimalist style matching embino aesthetic.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LOGOS = {
    "logo_apple": {
        "prompt": """Minimal Apple Inc logo.
        Pure black background (#0C0C0C).
        The iconic Apple silhouette in electric green (#33FF33).
        Simple, clean, recognizable.
        128x128 pixels.""",
    },
    "logo_intel": {
        "prompt": """Minimal Intel Corporation logo.
        Pure black background (#0C0C0C).
        The word "intel" in electric green (#33FF33) lowercase.
        Simple, clean, tech style.
        128x128 pixels.""",
    },
    "logo_nature": {
        "prompt": """Minimal Nature journal logo.
        Pure black background (#0C0C0C).
        The word "Nature" in electric green (#33FF33).
        Academic, scientific journal style.
        128x128 pixels.""",
    },
    "logo_embryonics": {
        "prompt": """Minimal biotech company logo for "Embryonics".
        Pure black background (#0C0C0C).
        Abstract embryo or cell shape in electric green (#33FF33).
        Simple geometric, scientific style.
        128x128 pixels.""",
    },
}


def generate_logos(output_dir: Path):
    """Generate all logos."""
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
    
    for name, data in LOGOS.items():
        print(f"\n🎨 Generating: {name}")
        save_path = output_dir / f"{name}.png"
        
        prompt = data["prompt"] + "\n\nCRITICAL: Pure black background. Electric green color only. Simple minimalist icon. No 3D, no gradients."
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp-image-generation",
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                ),
            )
            
            for part in response.parts:
                if part.text:
                    print(f"   Note: {part.text[:50]}...")
                elif hasattr(part, 'inline_data') and part.inline_data:
                    import base64
                    image_data = part.inline_data.data
                    if isinstance(image_data, str):
                        image_data = base64.b64decode(image_data)
                    with open(save_path, 'wb') as f:
                        f.write(image_data)
                    print(f"✅ Saved: {save_path}")
                    break
                elif image := getattr(part, 'as_image', lambda: None)():
                    image.save(str(save_path))
                    print(f"✅ Saved: {save_path}")
                    break
                    
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    output = Path(__file__).parent.parent / "images" / "team"
    generate_logos(output)
    print(f"\n✅ Logos saved to: {output}")

