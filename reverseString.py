# Problem prompt:
# Write a function that takes a string as input and returns the string reversed.

# this solution timed out
# def reverseString(s):
# 	new_s = ''
# 	if s:
# 		for i in range(0, len(s)):
# 			new_s += s[len(s)-i-1]
# 		return new_s
# 	return s 

def reverseString(s):
	s = list(s)
	for i in range(0, len(s)/2):
		temp = s[i]
		s[i] = s[len(s)-1-i]
		s[len(s)-1-i] = temp
	return str(''.join(s))

# test cases
print 'hello' + ' reversed is ' + reverseString('hello')
print '' + ' reversed is ' + reverseString('')
print 'hel lo' + ' reversed is ' + reverseString('hel lo')
print 'this string will end up getting reversed' + ' reversed is ' + reverseString('this string will end up getting reversed')
