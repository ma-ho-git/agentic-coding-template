#!/usr/bin/env bash
# @contract
# provides:   packages each skill under cowork/skills/ into dist/<name>.skill for claude.ai
# depends-on: zip (system tool), cowork/skills/*/ (the skill sources)
# consumers:  none - run by hand per cowork/README.md
# invariants: overwrites only cowork/dist/; aborts on the first error (set -e);
#             hidden files stay out of the archives
# updated:    2026-08-20
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
