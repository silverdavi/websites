#!/usr/bin/env python3
"""
Rhea Labs Holiday Image Generator
=================================
Generate a festive holiday image for the 2025 year-end presentation.

Uses Google Gemini 3 Pro Image generation.

Usage:
    python generate_holiday_image.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def generate_holiday_image():
    """Generate a holiday-themed image with Rhea brand colors."""
    
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("❌ google-genai package not installed.")
        print("Install with: pip install google-genai")
        sys.exit(1)
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ GOOGLE_API_KEY not found in environment.")
        print("Set it with: export GOOGLE_API_KEY=your_key")
        sys.exit(1)
    
    client = genai.Client(api_key=api_key)
    
    # Rhea brand colors:
    # --rhea-amber: #F5AF50 (warm amber/orange)
    # --rhea-sage: #C1DCA0 (soft sage green)
    # Background: #0A0A0F (near black)
    
    prompt = """Abstract, elegant holiday celebration visual for a biotech/fertility company.

    STYLE: Minimalist, sophisticated, modern. NOT cute or cartoonish. Think high-end corporate holiday card.
    
    COMPOSITION:
    - Deep, rich near-black background (#0A0A0F to #12121A gradient)
    - Elegant abstract elements suggesting celebration and new beginnings
    - Flowing organic curves reminiscent of the Rhea triskelion logo (three curved petals)
    - Subtle sparkles or light particles floating, suggesting hope and possibility
    
    COLOR PALETTE (strict):
    - Primary accent: Warm amber/gold (#F5AF50) - glowing, luminous
    - Secondary accent: Soft sage green (#C1DCA0) - gentle, organic
    - Background: Near black with subtle deep blue undertones
    - White/cream sparkles and highlights
    
    MOOD: Hopeful, warm, professional. Celebrates both the holidays and fertility/new life.
    
    ELEMENTS TO SUGGEST (abstractly, not literally):
    - New beginnings, growth, life
    - Warmth of the season
    - Scientific elegance
    - Celebration without being kitschy
    
    AVOID:
    - Santa, reindeer, snowmen, Christmas trees
    - Anything childish or cartoonish
    - Literal holiday imagery
    - Red and green traditional Christmas colors
    - Any text or typography
    
    The image should feel like a premium, abstract art piece that happens to evoke 
    warmth and celebration. Think Olafur Eliasson meets fertility science.
    
    Photorealistic lighting effects. 8K quality. Cinematic color grading.
    Wide aspect ratio (16:9) for use as a presentation slide background."""

    output_path = Path(__file__).parent / "holiday_bg.png"
    
    print("🎨 Generating Rhea Labs holiday image...")
    print(f"   Model: gemini-3-pro-image-preview")
    print(f"   Output: {output_path}")
    
    try:
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
                image_config=types.ImageConfig(
                    aspect_ratio="16:9",
                    image_size="2K"
                ),
            )
        )
        
        image_saved = False
        for part in response.parts:
            if part.text is not None:
                print(f"   Model note: {part.text[:150]}...")
            elif image := part.as_image():
                image.save(str(output_path))
                image_saved = True
                print(f"✅ Saved: {output_path}")
        
        if not image_saved:
            raise RuntimeError("No image was generated in the response")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    generate_holiday_image()

