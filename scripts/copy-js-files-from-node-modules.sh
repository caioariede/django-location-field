#!/bin/bash

# confirm we're covering the right list of extensions
# extensions starting with "!" will be skipped
copy_exts="css js map png !ts"
all_exts="$(echo $(find node_modules -type f -path '*/dist/*' | sed -E 's/.*\.//' | sort | uniq))"
if [ "$(sed 's/\!//g' <(echo "$copy_exts"))" != "$all_exts" ]; then
	echo "ERROR: upgrade the list of extensions in the copy command to make sure we're copying all necessary files: $all_exts"
	exit 1
fi

for ext in $copy_exts; do
	if [[ "$ext" =~ "!" ]]; then
		echo "Skipping extension: $ext"
		continue
	else
		echo "Copying files with extensions: $ext"
		while read -r orig_file; do
			new_file=location_field/static/location_field/$(sed -E 's/node_modules\/|dist\///g' <(echo "$orig_file"))
			mkdir -p "$(dirname "$new_file")"
			cp -v "$orig_file" "$new_file"
		done < <(find node_modules -type f -path "*/dist/*.$ext" | grep -v '\.src')
	fi
done
