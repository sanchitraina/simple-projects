import re
def find_pattern(test):
	if test != None:
	print('Pattern match found: ' + mo.group())
	elif test == None:
		print('No match found.')
# re.compile(\d\d\d\d\d\d) creates a pattern object that can be used to match patterns
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# can be modified to enter a file object also
test1 = input('Enter the test string: ')
mo = phoneNumRegex.search(test)
find_pattern(mo)

# Creating groups using ()

newNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d\d)')
# Group 1 = (\d\d\d)
# Group 2 = (\d\d\d\d) and so on...
# Use groups() to return all the groups that were found. Returns a tule of multiple values
test2 = input('Enter the string again: ')
mo2 = newNumberRegex.search(test2)
find_pattern(mo2)

# Matching multiple groups with the pipe '|'

heroRegex = re.compile(r'Batman|Tina Fey')
test3 = 'Batman and Tina Fey'
heroMo = heroRegex.search(test3)
find_pattern(heroMo)

# Matching of several patterns with the same prefix

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
test4 = 'Batmobile lost a wheel'
batMo = batRegex.search(test4)
batMo.group() # Groups will be divided based on the options in the paranthesis. group(1) is 'man'

# Optional matching with ? (means 0 or 1 group with the same prefix)

batRegex2 = re.compile(r'Bat(wo)?man')
test5 = 'The adventures of Batman and Batwoman'
batMo2 = batRegex2.search(test5)

# Optional matching with * (means 0 or more instances)

batRegex3 = re.compile(r'Bat(wo)*man')
batMo3 = batRegex3.search('The adventures of Batwowowowowowowowoman')
batMo3.group()

# Optional matching with + (means 1 or more instances)

batRegex4 = re.compile(r'Bat(wo)+man')
batMo4 = batRegex4.search('The adventures of Batwoman')
batMo4.group()
batMo4 = batRegex4.search('The adventures of Batman')
if batMo4.group() == None:
	print("No match found")

# Matching specific repetitions with {} (means minimum, maximum)

haRegex = re.compile(r'(Ha){3}')
haMo = haRegex.search('HaHaHa')
haMo.group()

haRegex2 = re.compile(r'(Ha){3,5}')
haMo2 = haRegex2.search('HaHaHaHaHa')
haMo2.group()

# Greedy and nongreedy expressions
# Greedy
# regex = re.compile(r'(test_expression){3,5}')
# Non Greedy
# regex = re.compile(r'(test_expression){3,5}?')

# Returning all occourances with findall()

# has no groups
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # returns ['415-555-9999', '212-555-0000']

# has groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # returns [('415', '555', '1122'), ('212', '555', '0000')]

# CHARACTER CLASSES

# ^ and $ characters
# ^ tells that the regex should start with a particular character
beginsWithHello = re.compile(r'^Hello')
# $ tells that the regex should end with a particular character
endsWithNumber = re.compile(r'\d$')

# Wildcard character

# . character matches any character except a newline
atRegex = re.compile(r'(.){0,5}at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# Case insensitive Matching

# Pass re.I as the second argument to re.compile()
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.')

# Substitute matched patterns using sub(replacement string, file in which replacement is to be done)
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
