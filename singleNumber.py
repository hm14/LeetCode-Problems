# Problem Prompt
# Given an array of integers, every element appears twice except for one. 
# Find that single one.

def singleNumber(nums):
	output = 2*sum(set(nums)) - sum(nums)
	return output

# test cases
numbers = [[1,2,3,1,4,2,3],
	[99,99,0,7,6,4,3,4,3,7,6],
	[0,0,1]]

for i in range(len(numbers)):
	print singleNumber(numbers[i])
