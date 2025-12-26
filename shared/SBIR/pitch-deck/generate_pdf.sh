#!/bin/bash

# Embino Pitch Deck PDF Generator
# Requires: WeasyPrint (pip install weasyprint)

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🎨 Generating Embino pitch deck PDF..."

# Check if WeasyPrint is installed
if ! command -v weasyprint &> /dev/null; then
    echo "❌ WeasyPrint is not installed."
    echo "Install with: pip install weasyprint"
    exit 1
fi

# Generate PDF
weasyprint \
    pitch.html \
    pitch.pdf \
    --presentational-hints \
    --optimize-images

echo "✅ Generated: pitch.pdf"
echo "📄 12 slides, landscape format"
echo ""
echo "Preview with: open pitch.pdf (macOS) or xdg-open pitch.pdf (Linux)"

