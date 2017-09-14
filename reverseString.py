# Problem prompt:
# Write a function that takes a string as input and returns the string reversed.
def reverseString(s):
 	new_s = ''
 	if s:
 		for i in range(0, len(s)):
 			new_s += s[len(s)-i-1]
 		return new_s
 	return s 
