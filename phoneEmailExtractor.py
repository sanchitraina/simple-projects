import re, pyperclip

# TODO: Create Phone regex
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? 				# area code
	(\s|-|\.)? 						# separator
	(\d{3}) 						# first 3 numbers
	(\s|-|\.) 						# separator
	(\d{4}) 						# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))? 	# extension
	)''', re.VERBOSE)

# TODO: Create Email regex

emailRegex = re.compile(r'''
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	''', re.VERBOSE)
# TODO: Find matches and format the results

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

# TODO: Copy the final result in the clipboard.

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))