# Problem Prompt
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s):
	word = ''
	reversed_words = ''
	for i in s:
		if i != ' ':
			word += i
		else:
			reversed_words += word[::-1]
			reversed_words += ' '
			word = ''
	if word:
		reversed_words += word[::-1]

	return reversed_words

# Test cases

strings = ['Hello, how are you?',
			'Hello',
			'h',
			'he',
			'Level',
			'',
			'ki lo']

for s in strings:
	print reverseWords(s)
