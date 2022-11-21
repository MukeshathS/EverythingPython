
# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def printLinkedList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
