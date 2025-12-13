#!/usr/bin/env python3
"""
Generate images for kernel-keys.com
Professional, technical aesthetic - teal/indigo accents on clean backgrounds.

Uses Google Gemini 3 Pro Image generation (same as embino).

Usage:
    cd /Users/davidsilver/dev/websites/shared/SBIR/code
    source venv/bin/activate
    python /Users/davidsilver/dev/websites/shared/KERNELKEYS/generate_kernel_images.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env from SBIR/code directory
env_path = Path(__file__).parent.parent / "SBIR" / "code" / ".env"
load_dotenv(env_path)


class KernelKeysImageGenerator:
    """
    Generates professional images for kernel-keys.com.
    Clean, technical aesthetic. Teal/indigo on dark backgrounds.
    """
    
    MODEL = "gemini-3-pro-image-preview"
    
    ASPECT_RATIOS = {
        "hero": "16:9",
        "square": "1:1",
        "wide": "21:9",
    }
    
    IMAGES = {
        "hero_neural": {
            "prompt": """Abstract visualization of a neural network or knowledge graph.
            
            Deep navy/slate background (#0F172A to #1E293B gradient).
            Interconnected nodes and edges forming an elegant network structure.
            
            Teal (#00D4AA) glowing nodes of varying sizes.
            Indigo (#6366F1) connection lines with subtle glow.
            Some orange (#F59E0B) accent nodes sparingly placed.
            
            The network should feel intelligent, precise, mathematical.
            Like a visualization from a machine learning research paper.
            
            Clean, minimalist, professional. NOT busy or chaotic.
            Subtle depth - some nodes larger/closer, others smaller/distant.
            
            The aesthetic of a high-end consulting firm or research lab.
            
            8K resolution, vector-clean edges, no noise.""",
            "aspect": "hero",
        },
        
        "research_geometric": {
            "prompt": """Abstract representation of geometric machine learning.
            
            3D wireframe surface - like a manifold or Riemannian geometry visualization.
            Teal (#00D4AA) mesh lines on dark background (#1E293B).
            
            The surface should curve elegantly, showing mathematical structure.
            Subtle gradient glow where lines intersect.
            
            Clean, technical, elegant - like a figure from a math paper.
            NOT photorealistic. Pure geometric abstraction.
            
            Professional research aesthetic.
            
            8K resolution, crisp lines.""",
            "aspect": "square",
        },
        
        "research_social": {
            "prompt": """Abstract visualization of social network or behavioral analysis.
            
            Network graph showing clusters of interconnected nodes.
            Dark background (#0F172A).
            
            Main clusters in teal (#00D4AA).
            Secondary clusters in indigo (#6366F1).
            Connection strength shown by line thickness.
            
            The layout suggests community detection, clustering analysis.
            Like a visualization from a social science research paper.
            
            Clean, data-viz aesthetic. Professional, not playful.
            
            8K resolution, precise geometry.""",
            "aspect": "square",
        },
        
        "research_bio": {
            "prompt": """Abstract representation of computational biology / genomics.
            
            DNA double helix visualization with data overlay.
            Dark background (#0F172A).
            
            Teal (#00D4AA) for the helix structure.
            Subtle data streams or sequence patterns flowing alongside.
            White and cyan accents for data points.
            
            Scientific, elegant, like a journal cover image.
            NOT cartoon DNA - sophisticated abstraction.
            
            The aesthetic of Nature or PNAS cover art.
            
            8K resolution, clean rendering.""",
            "aspect": "square",
        },
        
        "research_food": {
            "prompt": """Abstract visualization of molecular gastronomy / food chemistry.
            
            Molecular structures, chemical bonds, interconnected compounds.
            Dark background (#0F172A).
            
            Teal (#00D4AA) for molecular bonds.
            Warm orange (#F59E0B) for certain atoms or highlights.
            White for neutral elements.
            
            Like a chemistry diagram but artistic.
            Suggests flavor compounds, molecular modeling, recipe science.
            
            Professional, scientific aesthetic.
            NOT cartoon food or realistic food photography.
            
            8K resolution, geometric precision.""",
            "aspect": "square",
        },
        
        "venture_isometric": {
            "prompt": """Abstract isometric illustration of interconnected systems.
            
            Multiple geometric blocks or structures connected by lines.
            Representing different ventures or business units as a network.
            
            Dark background (#0F172A).
            Teal (#00D4AA), indigo (#6366F1), and subtle grays for blocks.
            Clean isometric 3D style, minimalist.
            
            Like a modern infographic or tech company diagram.
            Professional, corporate but not boring.
            
            8K resolution, clean edges.""",
            "aspect": "wide",
        },
    }
    
    def __init__(self, output_dir: str = None):
        self._client = None
        self._genai = None
        self._types = None
        
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = Path(__file__).parent.parent.parent / "kernel-keys-site" / "public" / "images"
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Output directory: {self.output_dir}")
    
    def _get_client(self):
        if self._client is None:
            try:
                from google import genai
                from google.genai import types
                self._genai = genai
                self._types = types
            except ImportError:
                print("❌ google-genai package not installed.")
                sys.exit(1)
            
            api_key = os.getenv('GOOGLE_API_KEY')
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment")
            
            self._client = genai.Client(api_key=api_key)
        
        return self._client
    
    def generate_image(self, name: str, prompt_data: dict) -> Path:
        client = self._get_client()
        types = self._types
        
        prompt = prompt_data["prompt"]
        aspect = self.ASPECT_RATIOS[prompt_data["aspect"]]
        
        # Add style reinforcement
        prompt += "\n\nCRITICAL: Pure geometric abstraction. Vector-clean edges. Professional research/consulting aesthetic. No AI artifacts, no plastic look."
        
        save_path = self.output_dir / f"{name}.png"
        
        print(f"\n🎨 Generating: {name}")
        print(f"   Aspect: {aspect}")
        print(f"   Prompt preview: {prompt[:80]}...")
        
        try:
            response = client.models.generate_content(
                model=self.MODEL,
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                    image_config=types.ImageConfig(
                        aspect_ratio=aspect,
                        image_size="2K"
                    ),
                )
            )
            
            image_saved = False
            for part in response.parts:
                if part.text is not None:
                    print(f"   Model note: {part.text[:100]}...")
                elif image := part.as_image():
                    save_path.parent.mkdir(parents=True, exist_ok=True)
                    image.save(str(save_path))
                    image_saved = True
                    print(f"✅ Saved: {save_path}")
            
            if not image_saved:
                raise RuntimeError("No image was generated in the response")
            
            return save_path
            
        except Exception as e:
            print(f"❌ Error generating {name}: {e}")
            raise
    
    def generate_all(self) -> dict:
        results = {}
        print("\n" + "═" * 60)
        print("GENERATING KERNEL KEYS IMAGES")
        print("═" * 60)
        
        for name, prompt_data in self.IMAGES.items():
            try:
                results[name] = self.generate_image(name, prompt_data)
            except Exception as e:
                print(f"⚠️  Failed {name}: {e}")
        
        print("\n" + "═" * 60)
        print(f"COMPLETE: Generated {len(results)} images")
        print("═" * 60)
        
        return results


if __name__ == "__main__":
    gen = KernelKeysImageGenerator()
    gen.generate_all()
