from Node import *

class MyQueue:

	def __init__(self):
		self.head : Node = None
		self.tail : Node = None

	def isEmpty(self):
		return self.head == None

	def peek(self):
		#return self.head.data
		if (self.head != None):
			return self.head.data
		else:
			return None
		
	def add(self, data):
		node : Node = Node(data)

		if (self.tail != None):
			self.tail.next = node
			#print("got added to the tail")
		
		self.tail = node

		if (self.head == None):
			self.head = node

		#print(self.head)

	
	def remove(self):
		data = self.head.data
		self.head = self.head.next
		if (self.head == None):
			self.tail = None
		return data


def main():
	
	lineOfPackets : MyQueue = MyQueue()
	print(lineOfPackets.isEmpty())
	print(lineOfPackets.peek())
	lineOfPackets.add("Packet1")
	lineOfPackets.add("Packet2")
	lineOfPackets.add("Packet3")
	lineOfPackets.add("Packet4")
	print(lineOfPackets.isEmpty())
	print(lineOfPackets.peek())
	print(lineOfPackets.remove())
	print(lineOfPackets.peek())
	print(lineOfPackets.remove())
	print(lineOfPackets.peek())
	print(lineOfPackets.remove())
	print(lineOfPackets.peek())
	print(lineOfPackets.remove())
	print(lineOfPackets.isEmpty())

if __name__ == '__main__':
	main()