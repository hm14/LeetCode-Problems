def removeElement(nums, val):
	if nums:
		length = len(nums)
		count = nums.count(val)

		if count <= 0:
			return length
		elif length == count:
			return 0

		i = 0

		while count > 0:
			if nums[i] == val and nums[i] == nums[length-1]:
				temp = nums[i]
				nums[i] = nums[length-2]
				nums[length-2] = temp
				count -= 2
				length -= 2
			elif nums[i] == val:
				temp = nums[i]
				nums[i] = nums[length-1]
				nums[length-1] = temp
				count -= 1
				length -= 1
			i += 1
		return length

	else:
		return 0
