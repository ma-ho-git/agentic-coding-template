#!/usr/bin/env bash
# Package each skill under cowork/skills/ as a .skill archive for upload to claude.ai.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
out="$here/dist"
mkdir -p "$out"
rm -f "$out"/*.skill

for dir in "$here"/skills/*/; do
  name="$(basename "$dir")"
  ( cd "$here/skills" && zip -q -r "$out/$name.skill" "$name" -x '.*' )
  echo "built $out/$name.skill"
done

echo
echo "Upload these in the Desktop app under Customize -> Skills, or in the skill settings on claude.ai."
