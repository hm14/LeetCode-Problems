# Problem prompt
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

def lengthOfLastWord(s):
	length = 0;
	for i in range(0, len(s)):
		if s[len(s)-1-i] != ' ':
			length += 1
		else:
			if length != 0:
				return length
	return length

# test cases
strings = ['','         ', ' p     ', 'ppp     ', 'hello o', 'I am typing', 'ends with a space ', 'last word here', 'last word', 'length']
for s in strings:
	print 'Length of last word for "' + s + '" is ' + str(lengthOfLastWord(s))
