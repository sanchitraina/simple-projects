import re
# re.compile(\d\d\d\d\d\d) creates a pattern object that can be used to match patterns
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# can be modified to enter a file object also
test = input('Enter the test string: ')
mo = phoneNumRegex.search(test)
if mo != None:
	print('Phone number found: ' + mo.group())
elif mo == None:
	print('No match found.')