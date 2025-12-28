#!/usr/bin/env python3
"""
Export rhea-labs-2025.html to PDF using Playwright (headless Chrome).
Renders exactly like the browser.

Usage:
    python export_pdf.py
"""

from pathlib import Path
from playwright.sync_api import sync_playwright


def export_to_pdf():
    html_path = Path(__file__).parent / "rhea-labs-2025.html"
    pdf_path = Path(__file__).parent / "rhea-labs-2025.pdf"

    print(f"📄 Converting: {html_path.name}")
    print(f"   Using: Playwright (headless Chromium)")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Load the HTML file
        page.goto(f"file://{html_path.absolute()}")
        
        # Wait for fonts and animations to settle
        page.wait_for_timeout(1000)
        
        # Export to PDF - landscape US Letter with margins
        page.pdf(
            path=str(pdf_path),
            format="Letter",
            landscape=True,
            print_background=True,
            margin={"top": "0.5in", "right": "0.5in", "bottom": "0.5in", "left": "0.5in"},
        )
        
        browser.close()

    print(f"✅ PDF saved: {pdf_path}")
    print(f"   Size: {pdf_path.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    export_to_pdf()
