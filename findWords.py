# Problem Prompt
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.

def findWords(words):
	first_row = 'qwertyuiop'
	second_row = 'asdfghjkl'
	third_row = 'zxcvbnm'

	output = []

	for word in words:
		row = 0
		for letter in word:
			letter = letter.lower()
			if first_row.find(letter) != -1 and (row == 0 or row == 1):
				row = 1
			elif second_row.find(letter) != -1 and (row == 0 or row == 2):
				row = 2
			elif third_row.find(letter) != -1 and (row == 0 or row == 3):
				row = 3
			elif row:
				row = 4
		if (row == 1 or row == 2 or row == 3) and row != 4:
			output.append(word)

	return output

# Test cases
Input = ["asdfghjkl","qwertyuiop","zxcvbnm", "12cw 5456", "Hello", "Alaska"\
, "Dad", "Peace", "MBVNC", "yet", "riot", "DaSh"]

print findWords(Input)
