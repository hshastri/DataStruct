class Heap:

    def __init__(self):
        self.heapItems = []

    def getLeftChildIndex(self, parentIndex : int) -> int:
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex : int) -> int:
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex : int) -> int:
        return (childIndex - 1) // 2

    def hasLeftChild(self, index : int) -> bool:
        return self.getLeftChildIndex(index) < len(self.heapItems)

    def hasRightChild(self, index : int) -> bool:
        return self.getRightChildIndex(index) < len(self.heapItems)

    def hasParent(self, index : int) -> bool:
        return self.getParentIndex(index) >= 0

    def leftChild(self, index : int):
        return self.heapItems[self.getLeftChildIndex(index)]

    def rightChild(self, index : int):
        return self.heapItems[self.getRightChildIndex(index)]

    def parent(self, index: int):
        return self.heapItems[self.getParentIndex(index)]

    def peek(self):
        if len(self.heapItems == 0):
            raise Exception("Empty Heap")
        return self.heapItems[0]

    def poll(self):
        if len(self.heapItems) == 0:
            raise Exception("Empty Heap")
        currentPeak = self.heapItems[0]
        """currentPeak = self.heapItems[0]
        self.heapItems[0] = self.heapItems[len(self.heapItems) - 1]
        self.heapifyDown()"""
        self.swap(self.heapItems, 0, len(self.heapItems) - 1)
        self.heapItems.remove(currentPeak)
        self.heapifyDown()
        return currentPeak


    def add(self, item):
        self.heapItems.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heapItems) - 1
        while (self.hasParent(index) and self.parent(index) > self.heapItems[index]):
            self.swap(self.heapItems, self.getParentIndex(index), index)
            index = self.getParentIndex(index)


    def heapifyDown(self):
        index = 0
        while (self.hasLeftChild(index)):
            smallerChild = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChild = self.getRightChildIndex(index)

            if self.heapItems[index] < self.heapItems[smallerChild]:
                break
            else:
                self.swap(self.heapItems, index, smallerChild)
            index = smallerChild

    def printHeap(self):
        print(self.heapItems)
    @staticmethod
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

def main():
    heap : Heap = Heap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(25)
    heap.add(17)
    heap.add(8)
    heap.printHeap()
if __name__ == '__main__':
	main()