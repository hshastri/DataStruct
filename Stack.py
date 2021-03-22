from Node import *

class Stack:
	
	def __init__(self):
		self.top : Node = None

	def isEmpty(self):
		return self.top == None

	def peek(self):
		if (self.top != None):
			return self.top.data
		else:
			return None

	def push(self, data):
		node : Node = Node(data)
		if (self.top == None):
			self.top = node
			return None
		node.next = self.top
		self.top = node

	def pop(self):
		if (self.top == None):
			return
		data = self.top.data
		self.top = self.top.next
		return data

def main():
	packets : Stack = Stack()
	print(packets.isEmpty())
	print(packets.peek())
	packets.push("packet1")
	packets.push("packet2")
	packets.push("packet3")
	packets.push("A")
	print(packets.peek())
	print(packets.pop())
	print(packets.peek())
	print(packets.pop())
	print(packets.peek())
	print(packets.pop())
	print(packets.peek())
	print(packets.pop())
	print(packets.peek())
	print(packets.pop())



if __name__ == '__main__':
	main()