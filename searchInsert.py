# Problem Prompt
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 gives 2
# [1,3,5,6], 2 gives 1
# [1,3,5,6], 7 gives 4
# [1,3,5,6], 0 gives 0



def searchInsert(nums, target):
	if nums:
		if target < nums[0]:
			return 0
		elif target > nums[len(nums)-1]:
			return len(nums)
		else:
			for i in range(len(nums)):
				if target == nums[i]:
					return i
				elif target > nums[i] and target < nums[i+1]:
					return i+1
	else:
		return -1

# test cases
# empty array
# array with only 1 number
# target outside array range
# target within array ranage
