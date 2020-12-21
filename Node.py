class Node:

	def __init__(self, data):
		self.data = data
		self.next : Node = None

	def __str__(self):
		
		#return "Data contained is: %s and next Node is: %s" % (str(self.data), str(self.next.data))
		
		if (self.next != None):
			return "Data contained is: %s and next Node is: %s" % (str(self.data), str(self.next.data))
		elif (self.next == None):
			return "Data contained is: %s and next Node is: None" % str(self.data)


	def __repr__(self):
		return "Node('%s')" % str(self.data)

def main():

	computer1 = Node("A")
	computer1.next = Node("B")
	print(str(computer1))
	print(repr(computer1))
	print(str(computer1.next))
	print(repr(computer1.next))
	ran1 = Node("C")
	ran2 = ran1
	ran2.next = Node("D")
	print(str(ran1))
	print(str(ran2))


if __name__ == '__main__':
	main()