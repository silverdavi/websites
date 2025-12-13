#!/usr/bin/env python3
"""
Render HTML Templates to PDF
============================
Converts letter.html and quotation.html to PDF using weasyprint.

Usage:
    cd /Users/davidsilver/dev/websites/shared/KERNELKEYS/templates
    source ../../venv/bin/activate
    python render_pdf.py letter.html output.pdf
    python render_pdf.py quotation.html output.pdf
"""

import sys
from pathlib import Path

try:
    from weasyprint import HTML
except ImportError:
    print("❌ weasyprint not installed.")
    print("   Install with: pip install weasyprint")
    sys.exit(1)


def render_pdf(html_path: str, output_path: str):
    """
    Render an HTML file to PDF.
    
    Args:
        html_path: Path to HTML template file
        output_path: Path for output PDF file
    """
    html_path = Path(html_path)
    output_path = Path(output_path)
    
    if not html_path.exists():
        print(f"❌ HTML file not found: {html_path}")
        sys.exit(1)
    
    # Resolve relative paths in HTML (for images, etc.)
    base_url = html_path.parent.absolute().as_uri()
    
    print(f"📄 Rendering: {html_path}")
    print(f"   Base URL: {base_url}")
    print(f"   Output: {output_path}")
    
    try:
        html_doc = HTML(filename=str(html_path), base_url=base_url)
        html_doc.write_pdf(output_path)
        print(f"✅ PDF created: {output_path}")
        print(f"   Size: {output_path.stat().st_size:,} bytes")
    except Exception as e:
        print(f"❌ Error rendering PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python render_pdf.py <input.html> <output.pdf>")
        print("\nExample:")
        print("  python render_pdf.py letter.html letter_output.pdf")
        print("  python render_pdf.py quotation.html quote_output.pdf")
        sys.exit(1)
    
    render_pdf(sys.argv[1], sys.argv[2])
