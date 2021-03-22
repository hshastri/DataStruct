from Node import *

class LinkedList:

	def __init__(self):
		self.head : Node = None

	def append(self, data):
		if (self.head == None):
			self.head = Node(data)
			return

		current = self.head
		while (current.next != None):
			current = current.next
		current.next = Node(data)

	def prepend(self, data):
		if (self.head == None):
			self.head = Node(data)
			return

		newHead = Node(data)
		newHead.next = self.head
		self.head = newHead

	def deleteWithValue(self, data):

		if (self.head == None):
			return None

		if (self.head.data == data):
			self.head = self.head.next
			return

		current = self.head
		while (current.next != None):
			if (current.next.data == data):
				current.next = current.next.next
				return
			current = current.next


	def printLinkedList(self):

		arrayOfNodes = []

		arrayOfNodes.append(str(self.head))

		current = self.head
		while (current.next != None):
			current = current.next
			arrayOfNodes.append(str(current))

		print(arrayOfNodes)

def main():
	lan : LinkedList = LinkedList()
	lan.append("network1")
	lan.append("network2")
	lan.append("network3")
	lan.printLinkedList()
	lan.prepend("network0")
	lan.printLinkedList()
	lan.deleteWithValue("network2")
	lan.printLinkedList()

if __name__ == '__main__':
	main()