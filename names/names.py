import time
from binary_search_tree import BinarySearchTree
from max_heap import Heap

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1: O(n)
#     for name_2 in names_2: O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1)

# bst = BinarySearchTree("Brian")

# for i in names_1:
#     bst.insert(i)

# for i in names_2:
#     if bst.contains(i):
#         duplicates.append(i)


def shellSort(arr):

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2


shellSort(names_1)
shellSort(names_2)


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low+high)//2
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle

    return -1  # not found


for i in names_1:
    if binary_search(names_2, i) != -1:
        duplicates.append(i)

end_time = time.time()
print(len(duplicates), ', '.join(duplicates))
print({end_time - start_time})
