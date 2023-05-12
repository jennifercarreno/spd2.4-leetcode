"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
EXAMPLE:
input:
head1 > 4 > 8 > 15 > 19 > null
head2 > 7 > 9 > 10 > 16 > null
output:
head > 4 > 7 > 8 > 9 > 10 > 15 > 16 > 19 > null
"""

# create a linked list
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0
		
	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while (last.next):
			last = last.next
		last.next = new_node


def merge_lists(list1, list2):
    # Create a new linked list to store the merged list
    merged_list = LinkedList()
    
    # Initialize two pointers to the heads
    current1 = list1.head
    current2 = list2.head
    
    # Compare the values of the nodes pointed to by current1 and current2
    # Append the smaller value to the result list and move the pointer to the next node in the corresponding list
    while current1 is not None and current2 is not None:
        if current1.val < current2.val:
            merged_list.append(current1.val)
            current1 = current1.next
        else:
            merged_list.append(current2.val)
            current2 = current2.next
        current = current.next
    
    # Append the remaining nodes of the non-exhausted list to the result list
    if current1 is not None:
        current.next = current1
    elif current2 is not None:
        current.next = current2
    
    # Return the head of the result list
    return merged_list
