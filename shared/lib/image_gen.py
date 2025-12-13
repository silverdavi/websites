#!/usr/bin/env python3
"""
Shared Image Generation Module
==============================
Reusable image generation using Google Gemini + background removal.

Usage:
    from lib.image_gen import ImageGenerator, generate_image, remove_background
    
    # Simple one-liner
    image_bytes = generate_image("A beautiful sunset over mountains")
    
    # Or with more control
    gen = ImageGenerator()
    gen.generate(
        prompt="A circuit board pattern",
        output_path="output.png",
        aspect_ratio="16:9",
        size="2K"
    )
    
    # Generate and resize
    gen.generate(
        prompt="Abstract neural network",
        output_path="hero.png",
        target_size=(1920, 1080)
    )
    
    # Generate with background removal
    gen.generate(
        prompt="A robot character",
        output_path="robot_nobg.png",
        remove_bg=True
    )
    
    # Remove background from existing image
    result = remove_background("input.png", "output.png")
    
    # Or from bytes
    output_bytes = remove_background(input_bytes)
"""

import os
import sys
import io
import time
from pathlib import Path
from typing import Optional, Tuple, Union, Literal

# Load .env from shared directory
from dotenv import load_dotenv

_ENV_PATH = Path(__file__).parent.parent / ".env"
load_dotenv(_ENV_PATH)


# Type aliases
AspectRatio = Literal["1:1", "3:4", "4:3", "9:16", "16:9", "21:9"]
ImageSize = Literal["1K", "2K"]


class ImageGenerator:
    """
    Google Gemini image generator with resize support.
    
    Attributes:
        MODEL: The Gemini model to use for image generation.
    """
    
    MODEL = "gemini-3-pro-image-preview"
    
    ASPECT_RATIOS: dict[str, AspectRatio] = {
        "square": "1:1",
        "portrait": "3:4",
        "landscape": "4:3",
        "tall": "9:16",
        "hero": "16:9",
        "wide": "21:9",
    }
    
    def __init__(self, api_key: Optional[str] = None, verbose: bool = True):
        """
        Initialize the image generator.
        
        Args:
            api_key: Google API key. If not provided, uses GOOGLE_API_KEY env var.
            verbose: Whether to print progress messages.
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.verbose = verbose
        self._client = None
        self._genai = None
        self._types = None
        self._pil = None
        self._rembg = None
        
        if not self.api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found. "
                f"Set it in {_ENV_PATH} or pass api_key parameter."
            )
    
    def _log(self, msg: str):
        """Print if verbose mode is on."""
        if self.verbose:
            print(msg)
    
    def _get_client(self):
        """Lazy-load the Google GenAI client."""
        if self._client is None:
            try:
                from google import genai
                from google.genai import types
                self._genai = genai
                self._types = types
            except ImportError:
                print("❌ google-genai package not installed.")
                print("   Install with: pip install google-genai")
                sys.exit(1)
            
            self._client = genai.Client(api_key=self.api_key)
            self._log("✅ Google GenAI client initialized")
        
        return self._client
    
    def _get_pil(self):
        """Lazy-load PIL."""
        if self._pil is None:
            try:
                from PIL import Image
                self._pil = Image
            except ImportError:
                print("❌ Pillow not installed.")
                print("   Install with: pip install Pillow")
                sys.exit(1)
        return self._pil
    
    def _get_rembg(self):
        """Lazy-load rembg."""
        if self._rembg is None:
            try:
                from rembg import remove
                self._rembg = remove
                self._log("✅ rembg loaded (first use may download model)")
            except ImportError:
                print("❌ rembg not installed.")
                print("   Install with: pip install rembg")
                sys.exit(1)
        return self._rembg
    
    def _determine_aspect_ratio(self, target_size: Tuple[int, int]) -> AspectRatio:
        """Determine best aspect ratio for target dimensions."""
        w, h = target_size
        ratio = w / h
        
        if ratio > 2.0:
            return "21:9"
        elif ratio > 1.5:
            return "16:9"
        elif ratio > 1.1:
            return "4:3"
        elif ratio > 0.9:
            return "1:1"
        elif ratio > 0.7:
            return "3:4"
        else:
            return "9:16"
    
    def generate(
        self,
        prompt: str,
        output_path: Optional[Union[str, Path]] = None,
        aspect_ratio: Optional[AspectRatio] = None,
        size: ImageSize = "2K",
        target_size: Optional[Tuple[int, int]] = None,
        style_suffix: Optional[str] = None,
        remove_bg: bool = False,
    ) -> bytes:
        """
        Generate an image from a prompt.
        
        Args:
            prompt: The image generation prompt.
            output_path: Optional path to save the image.
            aspect_ratio: Aspect ratio (e.g., "16:9", "1:1"). 
                         Auto-determined if target_size is provided.
            size: Image size from Gemini ("1K" or "2K").
            target_size: Optional (width, height) to resize the output.
            style_suffix: Optional text to append to prompt (e.g., style guidelines).
            remove_bg: Whether to remove the background (uses rembg).
        
        Returns:
            The image as PNG bytes.
        
        Raises:
            ValueError: If generation fails or no image is returned.
        """
        client = self._get_client()
        types = self._types
        
        # Build final prompt
        final_prompt = prompt
        if style_suffix:
            final_prompt += f"\n\n{style_suffix}"
        
        # Determine aspect ratio
        if target_size and not aspect_ratio:
            aspect_ratio = self._determine_aspect_ratio(target_size)
        aspect_ratio = aspect_ratio or "1:1"
        
        self._log(f"🎨 Generating image...")
        self._log(f"   📝 Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
        self._log(f"   📐 Aspect ratio: {aspect_ratio}")
        self._log(f"   📏 Size: {size}")
        if target_size:
            self._log(f"   🎯 Target resize: {target_size[0]}x{target_size[1]}")
        if remove_bg:
            self._log(f"   🔲 Background removal: enabled")
        
        start = time.time()
        
        try:
            response = client.models.generate_content(
                model=self.MODEL,
                contents=[final_prompt],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                    image_config=types.ImageConfig(
                        aspect_ratio=aspect_ratio,
                        image_size=size,
                    ),
                ),
            )
            
            elapsed = time.time() - start
            self._log(f"   ⏱️  Generated in {elapsed:.1f}s")
            
            # Extract image data
            image_data = None
            for part in response.parts:
                if part.text is not None:
                    self._log(f"   💬 Model note: {part.text[:100]}...")
                elif image := part.as_image():
                    # Save to temp file and read bytes (Gemini SDK API)
                    import tempfile
                    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                        tmp_path = tmp.name
                    image.save(tmp_path)
                    with open(tmp_path, 'rb') as f:
                        image_data = f.read()
                    os.unlink(tmp_path)
                    self._log(f"   📦 Got image: {len(image_data)} bytes")
            
            if not image_data:
                raise ValueError("No image in response from Gemini")
            
            # Resize if target_size specified
            if target_size:
                Image = self._get_pil()
                img = Image.open(io.BytesIO(image_data))
                self._log(f"   📏 Original size: {img.size}")
                
                # Convert to RGBA for transparency support
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                
                # Resize with high-quality resampling
                img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                self._log(f"   ✂️  Resized to: {img_resized.size}")
                
                # Save to bytes
                output = io.BytesIO()
                img_resized.save(output, format='PNG')
                image_data = output.getvalue()
            
            # Remove background if requested
            if remove_bg:
                self._log("   🔲 Removing background...")
                rembg_remove = self._get_rembg()
                Image = self._get_pil()
                
                img = Image.open(io.BytesIO(image_data))
                img_nobg = rembg_remove(img)
                
                output = io.BytesIO()
                img_nobg.save(output, format='PNG')
                image_data = output.getvalue()
                self._log(f"   ✅ Background removed: {len(image_data)} bytes")
            
            # Save to file if path provided
            if output_path:
                output_path = Path(output_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(image_data)
                self._log(f"   💾 Saved: {output_path}")
            
            self._log("✅ Done!")
            return image_data
            
        except Exception as e:
            self._log(f"❌ Error: {e}")
            raise
    
    def generate_batch(
        self,
        prompts: dict[str, dict],
        output_dir: Union[str, Path],
        default_aspect: AspectRatio = "1:1",
        default_size: ImageSize = "2K",
    ) -> dict[str, Path]:
        """
        Generate multiple images from a dictionary of prompts.
        
        Args:
            prompts: Dict mapping names to prompt configs.
                     Each config can have: prompt, aspect, size, target_size, style_suffix
            output_dir: Directory to save images.
            default_aspect: Default aspect ratio if not specified in prompt config.
            default_size: Default size if not specified in prompt config.
        
        Returns:
            Dict mapping names to saved file paths.
        
        Example:
            prompts = {
                "hero": {
                    "prompt": "Abstract circuit pattern",
                    "aspect": "16:9",
                },
                "icon": {
                    "prompt": "Simple gear icon",
                    "target_size": (256, 256),
                }
            }
            results = gen.generate_batch(prompts, "output/")
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        results = {}
        total = len(prompts)
        
        self._log(f"\n{'═' * 60}")
        self._log(f"BATCH GENERATION: {total} images")
        self._log(f"Output: {output_dir}")
        self._log(f"{'═' * 60}\n")
        
        for i, (name, config) in enumerate(prompts.items(), 1):
            self._log(f"\n[{i}/{total}] {name}")
            self._log("-" * 40)
            
            try:
                prompt = config.get("prompt", config) if isinstance(config, dict) else config
                aspect = config.get("aspect", default_aspect) if isinstance(config, dict) else default_aspect
                size = config.get("size", default_size) if isinstance(config, dict) else default_size
                target = config.get("target_size") if isinstance(config, dict) else None
                style = config.get("style_suffix") if isinstance(config, dict) else None
                
                # Map named aspects to actual ratios
                if aspect in self.ASPECT_RATIOS:
                    aspect = self.ASPECT_RATIOS[aspect]
                
                output_path = output_dir / f"{name}.png"
                
                self.generate(
                    prompt=prompt,
                    output_path=output_path,
                    aspect_ratio=aspect,
                    size=size,
                    target_size=target,
                    style_suffix=style,
                )
                
                results[name] = output_path
                
            except Exception as e:
                self._log(f"⚠️  Failed {name}: {e}")
        
        self._log(f"\n{'═' * 60}")
        self._log(f"COMPLETE: {len(results)}/{total} images generated")
        self._log(f"{'═' * 60}\n")
        
        return results


# Convenience function for quick one-off generation
def generate_image(
    prompt: str,
    output_path: Optional[Union[str, Path]] = None,
    aspect_ratio: Optional[AspectRatio] = None,
    target_size: Optional[Tuple[int, int]] = None,
    verbose: bool = True,
) -> bytes:
    """
    Quick function to generate a single image.
    
    Args:
        prompt: The image generation prompt.
        output_path: Optional path to save the image.
        aspect_ratio: Aspect ratio (e.g., "16:9", "1:1").
        target_size: Optional (width, height) to resize.
        verbose: Whether to print progress.
    
    Returns:
        The image as PNG bytes.
    
    Example:
        # Generate and get bytes
        img_bytes = generate_image("A cat sitting on a laptop")
        
        # Generate and save
        generate_image("A sunset", output_path="sunset.png")
        
        # Generate with specific size
        generate_image(
            "Website hero banner",
            output_path="hero.png",
            target_size=(1920, 1080)
        )
    """
    gen = ImageGenerator(verbose=verbose)
    return gen.generate(
        prompt=prompt,
        output_path=output_path,
        aspect_ratio=aspect_ratio,
        target_size=target_size,
    )


def remove_background(
    input_image: Union[str, Path, bytes],
    output_path: Optional[Union[str, Path]] = None,
    verbose: bool = True,
) -> bytes:
    """
    Remove background from an image using rembg.
    
    Args:
        input_image: Path to image file, or image bytes.
        output_path: Optional path to save the result.
        verbose: Whether to print progress.
    
    Returns:
        The image with transparent background as PNG bytes.
    
    Example:
        # From file
        remove_background("photo.jpg", "photo_nobg.png")
        
        # From bytes
        output_bytes = remove_background(input_bytes)
        
        # Chain with generation
        img = generate_image("A cat")
        nobg = remove_background(img, "cat_nobg.png")
    """
    try:
        from rembg import remove
        from PIL import Image
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("   Install with: pip install rembg Pillow")
        sys.exit(1)
    
    if verbose:
        print("🔲 Removing background...")
    
    # Load image
    if isinstance(input_image, (str, Path)):
        input_path = Path(input_image)
        if verbose:
            print(f"   📂 Loading: {input_path}")
        img = Image.open(input_path)
    else:
        # Assume bytes
        if verbose:
            print(f"   📦 Processing {len(input_image)} bytes")
        img = Image.open(io.BytesIO(input_image))
    
    if verbose:
        print(f"   📏 Size: {img.size}")
    
    # Remove background
    img_nobg = remove(img)
    
    # Convert to bytes
    output = io.BytesIO()
    img_nobg.save(output, format='PNG')
    result = output.getvalue()
    
    if verbose:
        print(f"   ✅ Done: {len(result)} bytes")
    
    # Save if path provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(result)
        if verbose:
            print(f"   💾 Saved: {output_path}")
    
    return result


if __name__ == "__main__":
    # Quick test
    print("Testing image generation...")
    print(f"Using .env from: {_ENV_PATH}")
    
    gen = ImageGenerator()
    
    # Test generation
    result = gen.generate(
        prompt="A simple geometric pattern with green lines on black background. Minimalist, clean, vector-style.",
        output_path=Path(__file__).parent.parent / "test_output.png",
        aspect_ratio="1:1",
    )
    
    print(f"\nGenerated {len(result)} bytes")
