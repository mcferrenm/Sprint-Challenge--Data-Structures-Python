import time
from binary_search_tree import BinarySearchTree

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

bst = BinarySearchTree("Brian")

for i in names_1:
    bst.insert(i)

for i in names_2:
    if bst.contains(i):
        duplicates.append(i)

end_time = time.time()
print(len(duplicates), ', '.join(duplicates))
print({end_time - start_time})
