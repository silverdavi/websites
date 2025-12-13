#!/usr/bin/env python3
"""
Generate Kernel Keys Branding Assets
=====================================
Creates logo and icon variants using Gemini 3 Pro image generation.

Usage:
    cd /Users/davidsilver/dev/websites/shared
    source venv/bin/activate  # if using venv
    python KERNELKEYS/generate_branding.py
"""

import sys
from pathlib import Path

# Add parent directory to path to import image_gen
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.image_gen import ImageGenerator

# Output directories
KERNEL_KEYS_SITE = Path(__file__).parent.parent.parent / "kernel-keys-site"
LOGO_DIR = KERNEL_KEYS_SITE / "public" / "images"
ASSETS_DIR = Path(__file__).parent / "assets"

LOGO_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR.mkdir(parents=True, exist_ok=True)


LOGO_CONCEPTS = {
    "neural_key": {
        "prompt": """A professional logo design: a key shape formed from interconnected neural network nodes.
        
        The key should be recognizable but abstract - made of glowing teal (#00D4AA) nodes connected by subtle lines.
        The nodes should vary in size, creating depth and visual interest.
        The overall shape clearly reads as a key (with a head/bit structure).
        
        Clean, minimalist, vector-style. Professional consulting firm aesthetic.
        Suitable for a machine learning and research company.
        
        White or transparent background. High contrast for visibility.
        The design should work at small sizes (favicon) and large sizes (letterhead).
        
        8K resolution, crisp edges, no noise or artifacts.""",
        "aspect_ratio": "1:1",
        "target_size": (1024, 1024),
    },
    
    "geometric_k": {
        "prompt": """A professional logo design: an abstract 3D letter "K" with faceted, crystalline geometry.
        
        The K should be constructed from geometric planes and facets, like a cut gemstone or crystal.
        Gradient from teal (#00D4AA) to indigo (#6366F1), with subtle highlights and shadows.
        The geometry should feel precise, mathematical, technical.
        
        Modern, sophisticated, professional. Suitable for a tech consulting firm.
        The K should be bold and readable even at small sizes.
        
        White or transparent background. High contrast.
        Clean vector-style rendering, no photorealistic textures.
        
        8K resolution, sharp edges, geometric precision.""",
        "aspect_ratio": "1:1",
        "target_size": (1024, 1024),
    },
    
    "circuit_monogram": {
        "prompt": """A professional logo design: interlocked letters "KK" formed as circuit traces with glowing connection points.
        
        The two K's should be stylized as circuit board traces - clean lines that form the letter shapes.
        At connection points and intersections, add small glowing nodes in teal (#00D4AA).
        The design should suggest technology, precision, and interconnected systems.
        
        Minimalist, technical, professional. Suitable for a consulting firm specializing in ML/AI.
        The monogram should be clear and readable.
        
        White or transparent background. High contrast.
        Vector-style, clean lines, no noise.
        
        8K resolution, precise geometry, professional finish.""",
        "aspect_ratio": "1:1",
        "target_size": (1024, 1024),
    },
}


def generate_logos():
    """Generate all logo concepts with background removal."""
    gen = ImageGenerator(verbose=True)
    
    print("\n" + "═" * 70)
    print("KERNEL KEYS BRANDING GENERATION")
    print("═" * 70)
    print(f"Output directory: {LOGO_DIR}")
    print(f"Assets directory: {ASSETS_DIR}\n")
    
    results = {}
    
    for name, config in LOGO_CONCEPTS.items():
        print(f"\n{'─' * 70}")
        print(f"Generating: {name}")
        print(f"{'─' * 70}")
        
        try:
            # Generate logo with background removal
            logo_path = LOGO_DIR / f"logo_{name}.png"
            gen.generate(
                prompt=config["prompt"],
                output_path=logo_path,
                aspect_ratio=config["aspect_ratio"],
                target_size=config["target_size"],
                remove_bg=True,
            )
            results[f"logo_{name}"] = logo_path
            
            # Also save to assets directory
            assets_path = ASSETS_DIR / f"logo_{name}.png"
            assets_path.write_bytes(logo_path.read_bytes())
            print(f"   📦 Also saved to: {assets_path}")
            
            # Generate icon variant (smaller, simplified)
            icon_path = LOGO_DIR / f"icon_{name}.png"
            icon_assets_path = ASSETS_DIR / f"icon_{name}.png"
            
            # For icons, we'll use the same image but at a smaller size
            # In a real workflow, you might want to simplify further, but this works
            from PIL import Image
            img = Image.open(logo_path)
            icon_size = (256, 256)
            icon_img = img.resize(icon_size, Image.Resampling.LANCZOS)
            icon_img.save(icon_path, format='PNG')
            icon_img.save(icon_assets_path, format='PNG')
            print(f"   ✅ Icon variant: {icon_path} ({icon_size[0]}x{icon_size[1]})")
            results[f"icon_{name}"] = icon_path
            
        except Exception as e:
            print(f"   ❌ Error generating {name}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "═" * 70)
    print(f"COMPLETE: Generated {len(results)} assets")
    print("═" * 70)
    print(f"\nGenerated files:")
    for name, path in results.items():
        print(f"  • {name}: {path}")
    
    return results


if __name__ == "__main__":
    generate_logos()
