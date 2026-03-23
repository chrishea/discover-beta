#!/bin/bash
# Image Optimization Script for Discover Cloudcroft
#
# Prerequisites: Install ImageMagick
#   macOS:   brew install imagemagick
#   Ubuntu:  sudo apt install imagemagick
#
# This script:
# 1. Resizes images wider than 2000px to 2000px max width
# 2. Compresses JPEGs to 80% quality
# 3. Creates a backup of originals first
#
# Usage: ./optimize-images.sh

MEDIA_DIR="$(dirname "$0")/media"
BACKUP_DIR="$(dirname "$0")/media-originals"

if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick is not installed."
    echo "Install it with: brew install imagemagick (macOS) or sudo apt install imagemagick (Ubuntu)"
    exit 1
fi

echo "Creating backup of original images..."
mkdir -p "$BACKUP_DIR"
cp "$MEDIA_DIR"/*.jpg "$BACKUP_DIR/"

echo "Optimizing images..."
for img in "$MEDIA_DIR"/*.jpg; do
    filename=$(basename "$img")
    size_before=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)

    convert "$img" \
        -resize '2000x2000>' \
        -quality 80 \
        -strip \
        "$img"

    size_after=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
    saved=$((size_before - size_after))

    if [ $saved -gt 0 ]; then
        echo "  $filename: saved $(numfmt --to=iec $saved 2>/dev/null || echo "${saved} bytes")"
    else
        echo "  $filename: already optimized"
    fi
done

echo ""
echo "Done! Originals backed up to: $BACKUP_DIR/"
echo "To also convert to WebP (recommended), install cwebp and run:"
echo "  for f in media/*.jpg; do cwebp -q 80 \"\$f\" -o \"\${f%.jpg}.webp\"; done"
