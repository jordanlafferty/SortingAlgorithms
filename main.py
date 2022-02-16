import random
import timeit


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


def generateArray(lower, upper, size):
    arr = []

    for i in range(size):
        arr.append(lower + i)
        if i != 0:
            arr = randomize(arr)
    return arr


def randomize(theList):
    i = len(theList)
    i = i - 1
    j = random.randrange(i)  # 0 <= j <= i-1

    theList[j], theList[i] = theList[i], theList[j]
    return theList


# smallest to largest
arr1 = generateArray(0, 10, 10)
print(arr1)
arr2 = generateArray(0, 1000, 100)
print(arr2)
arr3 = generateArray(0, 100000, 100000)
print(arr3)

x1 = selectionSort(arr1)
y1 = insertionSort(arr1)
z1 = bubbleSort(arr1)
print("0-10 Selection Sort")
print(x1)
print(timeit.timeit('selectionSort(arr1)', setup='from __main__ import selectionSort, arr1', number=1))
print("0-10 Insertion Sort")
print(y1)
print(timeit.timeit('insertionSort(arr1)', setup='from __main__ import insertionSort, arr1', number=1))
print("0-10 Bubble Sort")
print(z1)
print(timeit.timeit('bubbleSort(arr1)', setup='from __main__ import bubbleSort, arr1', number=1))

x2 = selectionSort(arr2)
y2 = insertionSort(arr2)
z2 = bubbleSort(arr2)
print("0-1000 Selection Sort")
print(x2)
print(timeit.timeit('selectionSort(arr2)', setup='from __main__ import selectionSort, arr2', number=1))
print("0-1000 Insertion Sort")
print(y2)
print(timeit.timeit('insertionSort(arr2)', setup='from __main__ import insertionSort, arr2', number=1))
print("0-1000 Bubble Sort")
print(z2)
print(timeit.timeit('bubbleSort(arr2)', setup='from __main__ import bubbleSort, arr2', number=1))

x3 = selectionSort(arr3)
y3 = insertionSort(arr3)
z3 = bubbleSort(arr3)
print("0-100000 Selection Sort")
print(x3)
print(timeit.timeit('selectionSort(arr3)', setup='from __main__ import selectionSort, arr3', number=1))
print("0-100000 Insertion Sort")
print(y3)
print(timeit.timeit('insertionSort(arr3)', setup='from __main__ import insertionSort, arr3', number=1))
print("0-100000 Bubble Sort")
print(z3)
print(timeit.timeit('bubbleSort(arr3)', setup='from __main__ import bubbleSort, arr3', number=1))