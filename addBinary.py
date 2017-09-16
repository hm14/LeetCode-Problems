# Problem prompt
# Given two binary strings, return their sum (also a binary string).

def addBinary(a, b):
	diff = 0
	third = []
	carry = 0
	new_b = ''

	if len(a) >= len(b):
		diff = len(a) - len(b)
	else:
		diff = len(b) - len(a)
		temp = a
		a = b
		b = temp

	for i in range(0, diff):
		new_b += '0'
	b = new_b + b

	for i in range(0, len(a)):
		if a[len(a)-i-1] == b[len(b)-i-1]:
			if a[len(a)-i-1] == '0' and carry == 0:
				third.insert(0, '0')
				carry = 0
			elif a[len(a)-i-1] == '0' and carry == 1:
				third.insert(0, '1')
				carry = 0
			elif a[len(a)-i-1] == '1' and carry == 0:
				third.insert(0, '0')
				carry = 1
			elif a[len(a)-i-1] == '1' and carry == 1:
				third.insert(0, '1')
				carry = 1
		elif a[len(a)-i-1] != b[len(b)-i-1]:
			if carry == 0:
				third.insert(0, '1')
				carry = 0
			elif carry == 1:
				third.insert(0, '0')
				carry = 1

	if carry:
		third.insert(0, '1')

	return ''.join(third)

# test cases
bnums = ['1','0', '100', '111', '1010', '10', '10', '11', '1']
  for n in range(0, len(bnums)):
    print bnums[n] + ' + ' + bnums[len(bnums)-n-1] + ' = ' + addBinary(bnums[n], bnums[len(bnums)-1-n])

