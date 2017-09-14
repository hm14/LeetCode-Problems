# Problem prompt:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)-1):
            if nums[i] + nums[j+1] == target:
            	return i, j+1
            j += 1
        i += 1
    return None
numlist = [2,-1, 3, 14,5,5,11, 4, 7, 26]

# test cases
print twoSum(numlist, 1)
print twoSum(numlist, 5)
print twoSum(numlist, 8)
print twoSum(numlist, 10)
print twoSum(numlist, 17)
print twoSum(numlist, 31)
print twoSum(numlist, 100)

