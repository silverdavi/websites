#!/usr/bin/env python3
"""
Convert Markdown files to PDF for USPTO filing.
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

CSS_STYLE = """
@page {
    size: letter;
    margin: 1in;
}
body {
    font-family: "Times New Roman", Times, serif;
    font-size: 12pt;
    line-height: 1.5;
}
h1 {
    font-size: 16pt;
    font-weight: bold;
    margin-top: 24pt;
    margin-bottom: 12pt;
}
h2 {
    font-size: 14pt;
    font-weight: bold;
    margin-top: 18pt;
    margin-bottom: 10pt;
}
h3 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 14pt;
    margin-bottom: 8pt;
}
table {
    border-collapse: collapse;
    margin: 10pt 0;
    width: 100%;
}
th, td {
    border: 1px solid black;
    padding: 6pt 8pt;
    text-align: left;
}
th {
    background-color: #f0f0f0;
}
code {
    font-family: "Courier New", Courier, monospace;
    font-size: 10pt;
    background-color: #f5f5f5;
    padding: 2pt 4pt;
}
pre {
    font-family: "Courier New", Courier, monospace;
    font-size: 10pt;
    background-color: #f5f5f5;
    padding: 10pt;
    margin: 10pt 0;
    white-space: pre-wrap;
    word-wrap: break-word;
}
blockquote {
    border-left: 3pt solid #ccc;
    margin-left: 0;
    padding-left: 12pt;
    font-style: italic;
}
hr {
    border: none;
    border-top: 1pt solid #ccc;
    margin: 20pt 0;
}
ul, ol {
    margin: 10pt 0;
    padding-left: 20pt;
}
"""

def md_to_pdf(input_file: str, output_file: str):
    """Convert a markdown file to PDF."""
    md_content = Path(input_file).read_text()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc']
    )
    
    # Wrap in HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
    {html_content}
    </body>
    </html>
    """
    
    # Convert to PDF
    HTML(string=full_html).write_pdf(
        output_file,
        stylesheets=[CSS(string=CSS_STYLE)]
    )
    print(f"Created: {output_file}")


if __name__ == '__main__':
    # Convert all patent documents
    md_to_pdf('draft.md', 'SPECIFICATION.pdf')
    md_to_pdf('CLAIMS.md', 'CLAIMS.pdf')
    md_to_pdf('COVER_SHEET.md', 'COVER_SHEET.pdf')
    
    print("\n" + "="*50)
    print("USPTO Filing Documents Ready:")
    print("="*50)
    print("  1. SPECIFICATION.pdf  - Main specification (required)")
    print("  2. COVER_SHEET.pdf    - Cover sheet (required)")
    print("  3. CLAIMS.pdf         - Claim language (recommended)")
    print("  4. DRAWINGS.pdf       - 5 figures (recommended)")
    print("\nUpload all to USPTO Patent Center.")

