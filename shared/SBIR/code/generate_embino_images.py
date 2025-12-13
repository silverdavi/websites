#!/usr/bin/env python3
"""
Embino Website Image Generator
==============================
High-quality images for the embino.com startup website.

Two modes:
1. ABSTRACT/GEOMETRIC - Circuit traces, data flow, patterns
2. PHOTOREALISTIC - Hardware shots, dev boards, components

Uses Google Gemini 3 Pro Image generation.

Usage:
    # Activate venv first
    source venv/bin/activate
    
    # Generate all hero images
    python generate_embino_images.py --all
    
    # Generate specific category
    python generate_embino_images.py --geometric
    python generate_embino_images.py --hardware
    
    # Single image
    python generate_embino_images.py --image hero_circuit
"""

import os
import sys
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class EmbinoImageGenerator:
    """
    Generates startup-quality images for embino.com.
    Terminal aesthetic, dark mode, no AI-slop.
    """
    
    MODEL = "gemini-3-pro-image-preview"
    
    # Output settings
    ASPECT_RATIOS = {
        "hero": "16:9",      # Hero banner
        "square": "1:1",     # Cards, icons
        "wide": "21:9",      # Ultra-wide banners
        "tall": "9:16",      # Mobile hero
    }
    
    # ═══════════════════════════════════════════════════════════════════════════
    # ABSTRACT / GEOMETRIC PROMPTS
    # ═══════════════════════════════════════════════════════════════════════════
    
    GEOMETRIC_PROMPTS = {
        "hero_circuit": {
            "prompt": """Abstract circuit board trace pattern on pure black background.
            
            Extremely minimalist. Only thin geometric lines.
            Electric green (#33FF33) traces forming clean right-angle paths.
            Occasional orange (#FF6B35) highlight nodes at intersections.
            
            The traces should suggest data flow, signal routing, intelligence.
            NOT a real circuit board - an artistic abstraction.
            
            Deep black void background (#0C0C0C).
            Lines are crisp, vector-like, perfectly geometric.
            Subtle glow on the green traces - like they're carrying current.
            
            No components, no chips, just the elegant geometry of traces.
            Bauhaus meets cyberpunk. Mathematical precision.
            
            8K resolution, extreme sharpness, no noise, no grain.""",
            "aspect": "hero",
            "style": "abstract"
        },
        
        "hero_dataflow": {
            "prompt": """Abstract visualization of data flowing through a constrained channel.
            
            Black background (#0C0C0C).
            Horizontal streams of tiny geometric particles - squares, dots, dashes.
            Electric green (#33FF33) primary color.
            Cyan (#00FFCC) secondary accents.
            
            The particles flow from chaotic/scattered on the left
            to organized/aligned on the right.
            Suggests: messy input → clean deterministic output.
            
            Minimalist. No realistic elements. Pure geometric abstraction.
            Like a scientific visualization from a research paper.
            
            Vector-clean edges. No blur except motion suggestion.
            Mathematical beauty. Information theory aesthetic.
            
            8K resolution, crisp, no AI artifacts.""",
            "aspect": "wide",
            "style": "abstract"
        },
        
        "pattern_grid": {
            "prompt": """Subtle repeating pattern for website background tile.
            
            Near-black background (#0C0C0C to #1E1E1E gradient).
            Extremely subtle grid of tiny dots or crosses.
            Dark green (#1a3a1a) - barely visible.
            
            The pattern should be so subtle it's almost subliminal.
            Creates texture without distraction.
            Like looking at a high-end audio equipment surface.
            
            Perfectly tileable. Seamless edges.
            No variation, pure repetition.
            
            8K resolution, mathematically precise.""",
            "aspect": "square",
            "style": "abstract"
        },
        
        "node_network": {
            "prompt": """Abstract network diagram on black background.
            
            Central node glowing electric green (#33FF33).
            Connected to 6-8 smaller nodes via thin geometric lines.
            Some nodes are orange (#FF6B35) - representing different states.
            
            Clean, minimal, like a scientific figure.
            Nodes are simple circles with subtle glow.
            Lines are perfectly straight.
            
            Suggests: distributed system, event routing, state machine.
            
            NOT a social network graph. More like a circuit diagram abstracted.
            Technical, precise, beautiful.
            
            Deep black void behind. Nothing else.
            
            8K resolution, vector-clean.""",
            "aspect": "square",
            "style": "abstract"
        },
        
        "bytecode_stream": {
            "prompt": """Abstract visualization of bytecode/binary data.
            
            Black background.
            Vertical columns of tiny rectangles in varying shades of green.
            Like looking at memory cells or a hex dump abstracted into art.
            
            Electric green (#33FF33) for "active" cells.
            Dark green (#0a2a0a) for background cells.
            Occasional orange (#FF6B35) highlight.
            
            Perfectly aligned grid. Mathematical precision.
            Creates a Matrix-inspired aesthetic but more minimal and elegant.
            
            Not literally the Matrix - no falling characters.
            Static, contemplative, like frozen data.
            
            8K resolution, sharp pixels, no blur.""",
            "aspect": "tall",
            "style": "abstract"
        },
    }
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PHOTOREALISTIC HARDWARE PROMPTS
    # ═══════════════════════════════════════════════════════════════════════════
    
    HARDWARE_PROMPTS = {
        "esp32_hero": {
            "prompt": """Professional product photography of an ESP32 development board.
            
            Real ESP32-DevKit board on a matte black surface.
            Dramatic side lighting creating crisp shadows.
            Shallow depth of field - chip in sharp focus, edges soft.
            
            The blue ESP32 module clearly visible.
            USB port, GPIO pins, antenna area.
            
            Shot on medium format camera. Commercial product photography.
            Like an Apple product shot but for dev hardware.
            
            Pure black background fading to void.
            Single directional light source, professional studio setup.
            
            EXTREMELY PHOTOREALISTIC. A real photo, not a render.
            No AI artifacts. Could be on Adafruit or SparkFun homepage.
            
            8K resolution, tack sharp, professional color grading.""",
            "aspect": "hero",
            "style": "photorealistic"
        },
        
        "microcontroller_macro": {
            "prompt": """Extreme macro photography of a microcontroller chip.
            
            Close-up of the actual silicon die or chip package.
            Showing the tiny bonding wires, the surface texture.
            Industrial precision meets microscopic beauty.
            
            Dramatic lighting - single harsh light creating texture.
            Dark background, chip emerging from shadow.
            
            Real photography aesthetic - slight chromatic aberration at edges.
            Shallow DOF, some areas falling to blur.
            
            Like an image from a semiconductor industry magazine.
            Technical beauty. Manufacturing precision.
            
            PHOTOREALISTIC. Not a render. A real photograph.
            
            8K, macro lens quality, no AI distortion.""",
            "aspect": "square",
            "style": "photorealistic"
        },
        
        "breadboard_prototype": {
            "prompt": """Professional photo of a prototype on a breadboard.
            
            White breadboard with colorful jumper wires (red, black, green, yellow).
            An ESP32 or Arduino module plugged in.
            A few LEDs, maybe a sensor module.
            
            Shot from 45-degree angle on a clean wood desk.
            Natural window light from the side.
            Shallow depth of field.
            
            The aesthetic of a maker's workbench, but styled.
            Clean, organized, professional.
            
            Like a photo from Make Magazine or Hackster.io
            
            PHOTOREALISTIC. Real components, real photo.
            No CGI look. Authentic maker aesthetic.
            
            8K, shallow DOF, warm natural tones.""",
            "aspect": "hero",
            "style": "photorealistic"
        },
        
        "pcb_traces_closeup": {
            "prompt": """Macro photography of PCB traces on a circuit board.
            
            Close-up showing copper traces on green soldermask.
            The geometric beauty of PCB routing.
            Some solder joints catching the light.
            
            Shot with macro lens, very shallow DOF.
            Side lighting creating contrast in the trace elevation.
            
            Dark, moody, industrial aesthetic.
            Like a detail shot in an electronics manufacturing documentary.
            
            PHOTOREALISTIC. Real PCB, real photograph.
            The texture of soldermask, the sheen of copper.
            
            8K, extreme detail, professional studio lighting.""",
            "aspect": "square",
            "style": "photorealistic"
        },
        
        "robot_closeup": {
            "prompt": """Close-up photo of a small robot's electronics compartment.
            
            A small wheeled robot or robotic arm showing the ESP32/Arduino inside.
            Wires neatly bundled, motor drivers visible.
            
            Professional product photography lighting.
            The robot shell partially open, revealing the brain inside.
            
            Clean, professional, startup product aesthetic.
            Like a photo from a robotics company's website.
            
            PHOTOREALISTIC. Real robot, real electronics, real photo.
            Could be on Boston Dynamics or a robotics Kickstarter.
            
            8K, commercial photography quality.""",
            "aspect": "hero",
            "style": "photorealistic"
        },
        
        "dev_desk_overhead": {
            "prompt": """Overhead flat-lay photo of a hardware developer's desk.
            
            Clean, organized workspace. Dark wood or matte black surface.
            ESP32 board, breadboard with simple circuit.
            Laptop showing terminal/code (screen partially visible).
            Coffee cup. Multimeter. Soldering iron.
            
            Morning light from the side creating long shadows.
            Everything precisely arranged, minimal but authentic.
            
            Like a "workstation tour" photo from a tech blog.
            Professional lifestyle photography for a hardware startup.
            
            PHOTOREALISTIC. Real objects, real scene.
            Not staged perfectly - authentically tidy.
            
            8K, editorial photography quality.""",
            "aspect": "square",
            "style": "photorealistic"
        },
    }
    
    def __init__(self, output_dir: Optional[str] = None):
        """Initialize the generator."""
        self._client = None
        self._genai = None
        self._types = None
        
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = Path(__file__).parent.parent / "images" / "generated"
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Output directory: {self.output_dir}")
    
    def _get_client(self):
        """Lazy load the genai client."""
        if self._client is None:
            try:
                from google import genai
                from google.genai import types
                self._genai = genai
                self._types = types
            except ImportError:
                print("❌ google-genai package not installed.")
                print("Install with: pip install google-genai")
                sys.exit(1)
            
            api_key = os.getenv('GOOGLE_API_KEY')
            if not api_key or api_key == 'your_google_api_key_here':
                raise ValueError(
                    "GOOGLE_API_KEY not found in environment. "
                    "Please set it in your .env file."
                )
            
            self._client = genai.Client(api_key=api_key)
        
        return self._client
    
    def generate_image(self, name: str, prompt_data: dict) -> Path:
        """Generate a single image from prompt data."""
        client = self._get_client()
        types = self._types
        
        prompt = prompt_data["prompt"]
        aspect = self.ASPECT_RATIOS[prompt_data["aspect"]]
        style = prompt_data["style"]
        
        # Add style reinforcement
        if style == "photorealistic":
            prompt += "\n\nCRITICAL: This must look like a real photograph. No CGI, no AI artifacts, no smooth/plastic look. Real textures, real lighting, photographic imperfections."
        elif style == "abstract":
            prompt += "\n\nCRITICAL: Pure geometric abstraction. Vector-clean edges. No organic shapes. Mathematical precision. No photorealistic elements."
        
        save_path = self.output_dir / f"{name}.png"
        
        print(f"\n🎨 Generating: {name}")
        print(f"   Style: {style} | Aspect: {aspect}")
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
    
    def generate_geometric(self) -> dict:
        """Generate all geometric/abstract images."""
        results = {}
        print("\n" + "═" * 60)
        print("GENERATING GEOMETRIC/ABSTRACT IMAGES")
        print("═" * 60)
        
        for name, prompt_data in self.GEOMETRIC_PROMPTS.items():
            try:
                results[name] = self.generate_image(name, prompt_data)
            except Exception as e:
                print(f"⚠️  Failed {name}: {e}")
        
        return results
    
    def generate_hardware(self) -> dict:
        """Generate all photorealistic hardware images."""
        results = {}
        print("\n" + "═" * 60)
        print("GENERATING PHOTOREALISTIC HARDWARE IMAGES")
        print("═" * 60)
        
        for name, prompt_data in self.HARDWARE_PROMPTS.items():
            try:
                results[name] = self.generate_image(name, prompt_data)
            except Exception as e:
                print(f"⚠️  Failed {name}: {e}")
        
        return results
    
    def generate_all(self) -> dict:
        """Generate all images."""
        results = {}
        results.update(self.generate_geometric())
        results.update(self.generate_hardware())
        
        print("\n" + "═" * 60)
        print(f"COMPLETE: Generated {len(results)} images")
        print("═" * 60)
        for name, path in results.items():
            print(f"   {name}: {path}")
        
        return results
    
    def list_available(self):
        """List all available image prompts."""
        print("\n📋 AVAILABLE IMAGES")
        print("\n🔷 GEOMETRIC/ABSTRACT:")
        for name, data in self.GEOMETRIC_PROMPTS.items():
            print(f"   {name:<25} [{data['aspect']}]")
        
        print("\n📷 PHOTOREALISTIC HARDWARE:")
        for name, data in self.HARDWARE_PROMPTS.items():
            print(f"   {name:<25} [{data['aspect']}]")


def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate Embino website images using Gemini 3 Pro"
    )
    parser.add_argument("--all", action="store_true", help="Generate all images")
    parser.add_argument("--geometric", action="store_true", help="Generate only geometric/abstract images")
    parser.add_argument("--hardware", action="store_true", help="Generate only photorealistic hardware images")
    parser.add_argument("--image", help="Generate a specific image by name")
    parser.add_argument("--list", action="store_true", help="List all available images")
    parser.add_argument("--output-dir", help="Output directory for images")
    
    args = parser.parse_args()
    
    gen = EmbinoImageGenerator(output_dir=args.output_dir)
    
    if args.list:
        gen.list_available()
        return
    
    if args.all:
        gen.generate_all()
        return
    
    if args.geometric:
        gen.generate_geometric()
        return
    
    if args.hardware:
        gen.generate_hardware()
        return
    
    if args.image:
        # Find the image in either dict
        name = args.image
        if name in gen.GEOMETRIC_PROMPTS:
            gen.generate_image(name, gen.GEOMETRIC_PROMPTS[name])
        elif name in gen.HARDWARE_PROMPTS:
            gen.generate_image(name, gen.HARDWARE_PROMPTS[name])
        else:
            print(f"❌ Unknown image: {name}")
            gen.list_available()
            sys.exit(1)
        return
    
    # Default: show help
    parser.print_help()
    print("\n")
    gen.list_available()


if __name__ == "__main__":
    main()

