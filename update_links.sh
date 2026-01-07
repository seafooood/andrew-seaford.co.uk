#!/bin/bash
find docs -name "*.md" -print0 | while IFS= read -r -d $'\0' file; do
  if ! grep -q "## Related Files" "$file"; then
    dir_path=$(dirname "$file")
    github_link="https://github.com/seafooood/andrew-seaford.co.uk/tree/main/$dir_path"
    github_link=${github_link// /%20}
    echo -e "\n\n## Related Files\n\n-   [$github_link]($github_link)" >> "$file"
  fi
  sed -i 's#http://andrew-seaford.co.uk/code/#https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/#g' "$file"
done
