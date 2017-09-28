# Problem Prompt
# Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	
	if head:
		previous = head
		current = head
		while current.next:
			current = current.next
			if previous.val == current.val:
				if current.next:
					previous.next = current.next
				else:
					previous.next = None
			else:
				previous = current
	
	return head
