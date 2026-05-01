#!/bin/bash
# Recursive image optimizer using built-in macOS `sips` (no ImageMagick required).
#
# Resizes any .jpg/.jpeg larger than 2 MB to max 2000px on the longest dimension
# and re-encodes at JPEG quality 80. Originals backed up to media-originals/<path>/.
#
# Usage: ./optimize-images-recursive.sh
#
# Excludes: .claude/, media-originals/, hidden dirs.

set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
BACKUP_DIR="$ROOT/media-originals"
SIZE_THRESHOLD=$((2 * 1024 * 1024))   # 2 MB
MAX_PIXELS=2000

mkdir -p "$BACKUP_DIR"

count=0
saved_total=0
processed=0
failed=0

# Find all .jpg/.jpeg/.JPG/.JPEG larger than 2 MB, excluding hidden/legacy dirs.
while IFS= read -r -d '' img; do
  count=$((count+1))
  rel="${img#$ROOT/}"
  size_before=$(stat -f%z "$img")
  if [ "$size_before" -le "$SIZE_THRESHOLD" ]; then
    continue
  fi

  # Backup if not already there
  backup_path="$BACKUP_DIR/$rel"
  if [ ! -f "$backup_path" ]; then
    mkdir -p "$(dirname "$backup_path")"
    cp "$img" "$backup_path"
  fi

  # Resize + recompress in place (sips writes back to source)
  if sips -Z "$MAX_PIXELS" -s formatOptions 80 "$img" --out "$img" >/dev/null 2>&1; then
    size_after=$(stat -f%z "$img")
    saved=$((size_before - size_after))
    if [ "$saved" -gt 0 ]; then
      saved_total=$((saved_total + saved))
      processed=$((processed + 1))
      printf '  %-70s  %5d KB -> %5d KB (saved %4d KB)\n' "$rel" \
        $((size_before/1024)) $((size_after/1024)) $((saved/1024))
    fi
  else
    failed=$((failed+1))
    echo "  ! sips failed: $rel"
  fi
done < <(find "$ROOT" \
  -type d \( -name '.*' -o -name 'media-originals' -o -name 'node_modules' \) -prune -o \
  -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -print0)

echo
echo "============================================================"
echo "Files scanned:    $count"
echo "Files processed:  $processed"
echo "Files failed:     $failed"
echo "Total saved:      $((saved_total / 1024 / 1024)) MB ($saved_total bytes)"
echo "Originals backed up to: $BACKUP_DIR/"
