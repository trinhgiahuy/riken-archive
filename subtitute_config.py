import os
import re

home_path = os.path.expanduser("~")
file_path = os.path.join(home_path, "a.sh")

with open(file_path, 'r') as file:
    content = file.read()

# Find the specific elif block
pattern = r'(\s*elif \[\[ "\$1" = \*"\*BBB"\*\ \]\]; then.*?)(\s*fi\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    new_block = match.group(1).replace('BBB', 'CCC')
    content = content.replace(match.group(0), match.group(1) + '\n' + new_block + match.group(2))

with open(file_path, 'w') as file:
    file.write(content)

