import os
import re

# Global replacements dictionary for the 'llvmarm' block
REPLACEMENTS = {
    '-mcpu=a64fx': '-mcpu=native',
    'mtune=a64fx': 'mtune=native'
    # Add more replacements as needed
}

home_path = os.path.expanduser("~")
file_path = os.path.join(home_path, "a.sh")

with open(file_path, 'r') as file:
    content = file.read()

# Find the specific elif block for 'llvm12'
# pattern = r'(\s*elif \[\[ "\$1" = \*"llvm12"\* \]\]; then[\s\S]*?\n\s*fi)(?=\s*elif|\s*fi|$)'
# pattern = r'(\s*elif \[\[ "\$1" = \*"llvm12"\* \]\]; then[\s\S]*?\n\tfi)'
pattern = r'(\s*elif \[\[ "\$1" = \*"llvm12"\* \]\]; then[\s\S]*?)(?=\n\tfi)'
match = re.search(pattern, content, re.DOTALL)

if match:
	# print(match)
	# print(match.group(0))
	# print(match.group(1))
	# print(match.group(2))
	# Create a replica for 'llvmarm' and perform initial replacements
	llvmarm_block = match.group(1).replace('llvm12', 'llvmarm')
	
	# Perform the specific replacements for 'llvmarm' block
	for old_str, new_str in REPLACEMENTS.items():
		llvmarm_block = llvmarm_block.replace(old_str, new_str)
	# Insert the modified llvmarm block after the original 'llvm12' block
	new_content = content.replace(match.group(0), match.group(0) + '\n' + llvmarm_block)

	with open(file_path, 'w') as file:
		file.write(new_content)
else:
	print("Pattern for 'llvm12' not found!")

