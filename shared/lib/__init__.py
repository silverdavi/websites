"""
Shared library modules for website projects.

Usage:
    from lib.image_gen import ImageGenerator, generate_image, remove_background
"""

from .image_gen import ImageGenerator, generate_image, remove_background

__all__ = ["ImageGenerator", "generate_image", "remove_background"]
