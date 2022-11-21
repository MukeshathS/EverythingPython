# A simple Python program to introduce a linked list
from LinkedList import LinkedList
from Node import Node

# Code execution starts here
if __name__ == '__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second  # Link first node with second

	second.next = third  # Link second node with the third node

	llist.printLinkedList()

