import random
import timeit


def getParentPos(pos):
    pos = pos // 2
    return pos


class minHeap:
    arr = []
    count = 0

    def __init__(self):
        self.arr.append({
            "value": 0,
            "index": 0,
            "connect": 0
        })

    def Heap_Push(self, value, index, connect):
        self.arr.append({
            "value": value,
            "index": index,
            "connect": connect
        })
        self.count += 1
        self.Heapify_Up(self.size())

    def Heapify_Up(self, pos):
        if pos <= 1:
            return

        parentPos = getParentPos(pos)
        parentNode = self.getNode(parentPos)

        leftPos = parentPos * 2
        leftNode = self.getNode(leftPos)
        rightPos = parentPos * 2 + 1
        rightNode = self.getNode(rightPos)

        node = 0  # node = 1, means the leftNode is the smallest, and node = 2 means the rightNode is the smallest
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (
                node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2
        if node == 1:
            self.arr[leftPos], self.arr[parentPos] = self.arr[parentPos], self.arr[leftPos]
        elif node == 2:
            self.arr[rightPos], self.arr[parentPos] = self.arr[parentPos], self.arr[rightPos]

        if node != 0:
            self.Heapify_Up(parentPos)

    def Heapify_Down(self, pos):
        parentPos = pos
        parentNode = self.getNode(parentPos)

        rightPos = parentPos * 2 + 1
        leftPos = parentPos * 2
        rightNode = self.getNode(rightPos)
        leftNode = self.getNode(leftPos)

        node = 0
        if leftNode is not None and parentNode["value"] > leftNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2
        if node == 1:
            self.arr[leftPos], self.arr[parentPos] = self.arr[parentPos], self.arr[leftPos]
        elif node == 2:
            self.arr[rightPos], self.arr[parentPos] = self.arr[parentPos], self.arr[rightPos]

        if node != 0:
            self.Heapify_Up(parentPos)

    def ExtrudeMin(self):  # take out the root and rebalance the tree
        returnNode = self.getNode(1)
        lastNode = self.arr.pop()
        self.count -= 1
        if self.count > 0:
            self.arr[1] = lastNode
        self.Heapify_Down(1)
        return returnNode

    def size(self):
        return self.count

    def decreaseValue(self, value, index, connect):
        pass

    def getNode(self, pos):
        if pos > self.count:
            return None
        else:
            return self.arr[pos]


def selectionSort(a):
    for i in range(len(a)):
        k = i
        j = i + 1
        for j in range(len(a)):
            if a[k] < a[j]:
                temp = a[k]
                a[k] = a[j]
                a[j] = temp

    return a


def insertionSort(a):
    for i in range(len(a)):
        temp = a[i]
        k = i
        while temp < a[k - 1] & k > 0:
            temp = a[k]
            a[k] = a[k - 1]
            a[k - 1] = temp

    return a


def bubbleSort(a):
    for i in range(len(a)):
        j = 0
        while j < len(a) - i - 1:
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            j += 1
    return a


def heapSort(a):
    heap = minHeap()
    for i in a:
        heap.Heap_Push(i, i, i)
    counter = 0
    while heap.size() > 0:
        a[counter] = heap.ExtrudeMin()["value"]
        counter += 1

    return a


def generateArray(size):
    array = []
    for i in range(size):
        array.append(i)
    random.shuffle(array)
    return array


def randomize(theList):
    i = len(theList)
    i = i - 1
    j = random.randrange(i)  # 0 <= j <= i-1

    theList[j], theList[i] = theList[i], theList[j]
    return theList


# smallest to largest
arr = generateArray(100000)

w = heapSort(arr)
#x = selectionSort(arr)
#y = insertionSort(arr)
#z = bubbleSort(arr)

print("0-100000 Heap Sort")
print(w)
print(timeit.timeit('heapSort(arr)', setup='from __main__ import heapSort, arr', number=1))
print("0-100000 Selection Sort")
#print(x)
#print(timeit.timeit('selectionSort(arr)', setup='from __main__ import selectionSort, arr', number=1))
#print("0-100000 Insertion Sort")
#print(y)
#print(timeit.timeit('insertionSort(arr)', setup='from __main__ import insertionSort, arr', number=1))
#print("0-100000 Bubble Sort")
#print(z)
#print(timeit.timeit('bubbleSort(arr)', setup='from __main__ import bubbleSort, arr3', number=1))
