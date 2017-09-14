# Problem promt:
# Reverse the digits of an integer

def reverse(num):
	sign = 1
	if num < 0:
		sign = -1
	num = str(abs(num))
	num = num[::-1]
	num = sign * int(num)

	if num > 2147483647 or num < -2147483647:
		return 0

	return num

# test cases
print reverse(0)
print reverse(-63482)
print reverse(112345123452345)
print reverse(-2147483648)
