class Node():
	
	def __init__(self, data):
		self.data = data
		self.left: Node = None
		self.right: Node = None

	def insert(self, data):
		if (data <= self.data):
			#print("the data {} is inserted to the left".format(data))
			if (self.left == None):
				self.left = Node(data)
			else:
				self.left.insert(data)
		else:
			#print("the data {} is inserted to the right".format(data))
			if (self.right == None):
				self.right = Node(data)
			else:
				self.right.insert(data)

	def contains(self, data):
		if (self.data == data):
			return True
		elif (data < self.data):
			if (self.left == None):
				return False
			else:
				return self.left.contains(data)
		else:
			if (self.right == None):
				return False
			else:
				return self.right.contains(data)

	def printInOrder(self):
		if (self.left != None):
			self.left.printInOrder()
		print(str(self.data))
		if (self.right != None):
			self.right.printInOrder()

def main():
	tree : Node = Node(10)
	tree.insert(5)
	tree.insert(15)
	tree.insert(8)
	tree.insert(4)
	print(tree.contains(10))
	print(tree.contains(5))
	print(tree.contains(15))
	print(tree.contains(8))
	print(tree.contains(69))
	print(tree.contains(4))
	tree.printInOrder()


if __name__ == '__main__':
	main()