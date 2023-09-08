import re
import os

def duplicate_and_substitute(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Search for pattern of elif for BBB
    pattern = re.compile(r'(elif \[ "\$arg" == "BBB" \].*?fi)', re.DOTALL)
    match = pattern.search(content)
    
    # If match is found, duplicate and substitute
    if match:
        bbb_section = match.group(1)
        ccc_section = bbb_section.replace('BBB', 'CCC')
        
        # Place the ccc_section right after the bbb_section
        new_content = content[:match.end()] + '\n' + ccc_section + content[match.end():]

        # Write modified content back to file
        with open(file_path, 'w') as f:
            f.write(new_content)
    else:
        print(f"No 'elif' section for 'BBB' found in {file_path}")

# Usage
home_directory = os.environ['HOME']
file_path = os.path.join(home_directory, 'a.sh')
duplicate_and_substitute(file_path)
