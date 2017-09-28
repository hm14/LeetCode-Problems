# Problem Prompt
# Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(head):
	if head:
		current = head	
		while current.next:
			temp = current
			current = current.next
			if(temp.val == current.val):
				if current.next:
					temp.next = current.next
				else:
					temp.next = None
	return head
