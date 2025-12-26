#!/usr/bin/env python3
"""
Generate branding assets for Embino using Gemini.
Logo variations with terminal aesthetic.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LOGOS = {
    "logo-square": {
        "prompt": """Logo for "embino_" tech company.
        Pure black background (#0C0C0C).
        The text "embino_" in electric green (#33FF33).
        Monospace terminal font style.
        The underscore should look like a blinking cursor.
        Minimal, clean, technical aesthetic.
        Like a terminal prompt or code editor.
        Subtle green dot grid pattern in background (very faint).
        512x512 pixels, centered text.""",
        "size": "512",
        "ratio": "1:1",
    },
    "icon-square": {
        "prompt": """Logo icon showing just "e_" for embino.
        Pure black background (#0C0C0C) with rounded corners.
        The text "e_" in electric green (#33FF33).
        Monospace terminal font style, bold.
        The underscore is a cursor.
        Minimal, clean, app icon style.
        256x256 pixels, centered.""",
        "size": "256",
        "ratio": "1:1",
    },
    "logo-wide": {
        "prompt": """Wide logo for "embino_" tech company.
        Pure black background (#0C0C0C).
        The text "embino_" in electric green (#33FF33).
        Monospace terminal font style.
        The underscore should look like a blinking cursor.
        Minimal, clean, technical aesthetic.
        Like a terminal prompt or code editor.
        Subtle green dot grid pattern in background (very faint).
        800x200 pixels, centered text, horizontal layout.""",
        "size": "800",
        "ratio": "4:1",
    },
    "logo-tagline": {
        "prompt": """Logo for "embino_" with tagline.
        Pure black background (#0C0C0C).
        Main text "embino_" in electric green (#33FF33).
        Below it: "Tiny intelligence for tiny devices" in cyan (#00FFCC).
        Monospace terminal font style.
        The underscore should look like a cursor.
        Minimal, clean, technical aesthetic.
        800x240 pixels, centered, stacked layout.""",
        "size": "800",
        "ratio": "10:3",
    },
}


def generate_logos(output_dir: Path):
    """Generate all logo variations."""
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
        
        prompt = data["prompt"] + """

CRITICAL REQUIREMENTS:
- Pure black background, NOT white
- Electric green text color (#33FF33)
- Monospace/terminal font aesthetic
- Clean, minimal, no 3D effects
- No photorealism
- Text must be perfectly legible"""
        
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
                    print(f"   Note: {part.text[:80]}...")
                elif hasattr(part, 'inline_data') and part.inline_data:
                    # Save image from inline_data
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
            print(f"❌ Error generating {name}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    output = Path(__file__).parent.parent / "branding" / "generated"
    generate_logos(output)
    print(f"\n✅ Logos saved to: {output}")

