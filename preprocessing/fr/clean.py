import re
# Define regex patterns for checking capital letters, numerals, and non-ASCII letters
capital_pattern = re.compile(r'[A-Z]')
numeral_pattern = re.compile(r'\d')
misc_pattern = re.compile(r'[\'|-|+|&|\.]')

pronounciations = set()
# Open the file for reading
with open('fr.csv', 'r', encoding='utf-8') as f:
		# Read each line of the file
		lines = f.readlines()
		
		# Create an empty list to store the lines that pass the check
		filtered_lines = []
		
		# Iterate over the lines and check for the presence of capital letters, numerals, and non-ASCII letters
		for i, line in enumerate(lines):
				try:
					headword, pronounciation = line.strip().split(',')
					phonemes = pronounciation.split(' ')
					# print(phonemes)
					pronounciations = pronounciations.union(set(phonemes))
					if not capital_pattern.search(headword) and not numeral_pattern.search(headword) and not misc_pattern.search(headword):
							# If the line doesn't contain any of these characters, add it to the list of filtered lines
							filtered_lines.append(line)
				except:
					print(i+1)
		
# Open the file for writing
with open('fr.csv', 'w', encoding='utf-8') as f:
		# Write the filtered lines to the file
		for line in filtered_lines:
				f.write(line)

print(pronounciations)
with open('phonemes.txt', 'w', encoding='utf-8') as f:
		for phone in list(pronounciations):
				f.write(phone)