#!/bin/bash

export PATH="$HOME/.local/bin/myscripts:$PATH"

gnome-terminal -- bash -c '
mkdir -p /tmp/sort-unique-inline

echo "Sorting lines of *.sq file and removing duplicates..."
flag=false
for file in "$@"; do
  if [[ -f "$file"  && "$file" == *.sq ]]; then
    flag=true
    echo "Processing: $file"
    cp "$file" "/tmp/sort-unique-inline/${file}.bak"
    # awk '"'"'{$1=$1}; NF { $0=toupper(substr($0,1,1)) substr($0,2); print }'"'"' "$file" | sort -fu > "/tmp/${file}.tmp" && mv "/tmp/${file}.tmp" "$file"
    awk '"'"'NF {$1=$1; print }'"'"' "$file" | sort -fu > "/tmp/${file}.tmp" && mv "/tmp/${file}.tmp" "$file"
  fi
done
echo "Done!"
if [ "$flag" = true ]; then
  sleep 2
fi
# exec bash
' bash "$@"

