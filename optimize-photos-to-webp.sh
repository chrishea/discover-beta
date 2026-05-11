#!/usr/bin/env bash
# optimize-photos-to-webp.sh
#
# Convert every JPG / JPEG / PNG / HEIC / GIF in ~/Desktop/Discover-Cloudcroft-Photos
# to .webp at quality 82, backing up originals first to a timestamped sibling folder.
# Existing .webp files in the source are left alone.
#
# Requirements:
#   brew install webp        # provides cwebp
#   (sips is preinstalled on macOS; used for the lone HEIC file)
#
# Usage:
#   bash optimize-photos-to-webp.sh            # do it
#   bash optimize-photos-to-webp.sh --dry-run  # list what would be converted, change nothing
#
# Tested on macOS with bash 3.2 (the default /bin/bash) and zsh.

set -u

SRC="$HOME/Desktop/Discover-Cloudcroft-Photos"
TS="$(date +%Y%m%d-%H%M%S)"
BACKUP="$HOME/Desktop/Discover-Cloudcroft-Photos-originals-$TS"
QUALITY=82
LOG="$HOME/Desktop/discover-cloudcroft-webp-$TS.log"

DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

# ------------ pre-flight ------------
command -v cwebp >/dev/null 2>&1 || { echo "ERROR: cwebp not found. Install with: brew install webp"; exit 1; }
command -v sips  >/dev/null 2>&1 || { echo "ERROR: sips not found (should ship with macOS)."; exit 1; }
[[ -d "$SRC" ]] || { echo "ERROR: source folder not found: $SRC"; exit 1; }

echo "Source : $SRC"
echo "Backup : $BACKUP"
echo "Quality: $QUALITY"
echo "Log    : $LOG"
echo "Dry run: $DRY_RUN"
echo

# ------------ collect files to convert ------------
# Convert these extensions; leave existing .webp alone.
TMP_LIST="$(mktemp -t dc_webp_list)"
trap 'rm -f "$TMP_LIST"' EXIT

# Use null-delimited paths to handle spaces and weird chars.
find "$SRC" -maxdepth 1 -type f \
  \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.heic' -o -iname '*.gif' \) \
  -print0 > "$TMP_LIST"

TOTAL=$(tr -cd '\0' < "$TMP_LIST" | wc -c | tr -d ' ')
echo "Files to convert: $TOTAL"
if [[ "$TOTAL" -eq 0 ]]; then
  echo "Nothing to do."
  exit 0
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "--- dry run: files that would be converted ---"
  tr '\0' '\n' < "$TMP_LIST"
  echo "--- end dry run ---"
  exit 0
fi

# ------------ confirmation ------------
read -r -p "Back up to $BACKUP and convert $TOTAL files in place? [y/N] " ans
[[ "$ans" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 1; }

# ------------ backup ------------
mkdir -p "$BACKUP" || { echo "ERROR: could not create backup folder"; exit 1; }
echo "Backing up..."
# Copy only the files we plan to touch. Preserve mtime.
xargs -0 -I{} cp -p "{}" "$BACKUP"/ < "$TMP_LIST"

BACKUP_COUNT=$(find "$BACKUP" -maxdepth 1 -type f | wc -l | tr -d ' ')
if [[ "$BACKUP_COUNT" -ne "$TOTAL" ]]; then
  echo "ERROR: backup count ($BACKUP_COUNT) != source count ($TOTAL). Aborting before any conversion."
  exit 1
fi
echo "Backup OK ($BACKUP_COUNT files)."

# ------------ convert ------------
echo "Converting..."
: > "$LOG"
SUCCESS=0
FAIL=0
BEFORE_BYTES=0
AFTER_BYTES=0

# Read NUL-delimited list portably.
while IFS= read -r -d '' f; do
  base="${f##*/}"           # filename
  stem="${base%.*}"          # without extension
  ext="${base##*.}"          # extension
  ext_lc="$(printf '%s' "$ext" | tr '[:upper:]' '[:lower:]')"
  out="$SRC/$stem.webp"

  # If a .webp with the same stem already exists, append " (webp)" to avoid clobbering.
  if [[ -e "$out" ]]; then
    out="$SRC/$stem (converted).webp"
  fi

  src_size=$(stat -f '%z' "$f" 2>/dev/null || echo 0)
  BEFORE_BYTES=$((BEFORE_BYTES + src_size))

  if [[ "$ext_lc" == "heic" ]]; then
    # cwebp doesn't read HEIC. Use sips to bridge via PNG in a temp file.
    tmp_png="$(mktemp -t dc_webp_heic).png"
    if sips -s format png "$f" --out "$tmp_png" >/dev/null 2>&1 \
       && cwebp -q "$QUALITY" -mt -quiet "$tmp_png" -o "$out"; then
      rm -f "$tmp_png"
      ok=1
    else
      rm -f "$tmp_png"
      ok=0
    fi
  else
    if cwebp -q "$QUALITY" -mt -quiet "$f" -o "$out"; then
      ok=1
    else
      ok=0
    fi
  fi

  if [[ "$ok" -eq 1 && -s "$out" ]]; then
    out_size=$(stat -f '%z' "$out" 2>/dev/null || echo 0)
    AFTER_BYTES=$((AFTER_BYTES + out_size))
    rm -f "$f"
    SUCCESS=$((SUCCESS + 1))
    printf 'OK  %s -> %s (%d -> %d bytes)\n' "$base" "${out##*/}" "$src_size" "$out_size" >> "$LOG"
  else
    FAIL=$((FAIL + 1))
    printf 'FAIL %s\n' "$base" >> "$LOG"
    rm -f "$out"  # don't leave a partial output behind
  fi

  # Progress dot every 25 files
  if (( (SUCCESS + FAIL) % 25 == 0 )); then
    printf '  %d / %d processed\n' "$((SUCCESS + FAIL))" "$TOTAL"
  fi
done < "$TMP_LIST"

echo
echo "Done."
echo "  Converted: $SUCCESS"
echo "  Failed   : $FAIL"
if [[ "$BEFORE_BYTES" -gt 0 ]]; then
  pct=$(awk -v a="$AFTER_BYTES" -v b="$BEFORE_BYTES" 'BEGIN { printf "%.1f", (1 - a/b)*100 }')
  printf '  Size     : %.1f MB -> %.1f MB (%s%% smaller)\n' \
    "$(awk -v x=$BEFORE_BYTES 'BEGIN{print x/1048576}')" \
    "$(awk -v x=$AFTER_BYTES  'BEGIN{print x/1048576}')" \
    "$pct"
fi
echo "  Backup   : $BACKUP"
echo "  Log      : $LOG"
