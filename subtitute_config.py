import re

def duplicate_and_substitute(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Search for pattern of elif for BBB up until the second last 'fi'
    pattern = re.compile(r'(elif \[\[  "\$1" = \*\\"BBB\\"\* \]\].*?)(?=fi.*fi)', re.DOTALL)
    match = pattern.search(content)

    # If match is found, duplicate and substitute
    if match:
        bbb_section = match.group(1)
        ccc_section = bbb_section.replace('BBB', 'CCC')
        
        new_content = content[:match.end(1)] + '\n' + ccc_section + content[match.end(1):]

        with open(file_path, 'w') as f:
            f.write(new_content)

file_path = "/path/to/your/script.sh"
duplicate_and_substitute(file_path)
