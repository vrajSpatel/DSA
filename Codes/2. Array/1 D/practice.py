from array import *

#1. Create an array and traverse.
arr = array('i', [1,1,2,3,4,5])
print('answer 1')
for i in arr :
    print(i)

#2. Access individual elements through indexes.
print('answer 2')
print(arr[3])

#3. Append any value to the array using append() method.
print('answer 3')
arr.append(6)
print(arr)

#4. Insert value in an array using insert() method.
print('answer 4')
arr.insert(3,9)
print(arr)

#5. Extend python array using extend() method.
print('answer 5')
arr2 = array('i',[10,11,12])
arr.extend(arr2)
print(arr)

#6. Add items from list into array using fromlist() method.
print('answer 6')
demolist = [20,21,22]
arr.fromlist(demolist)  # add items to last just like extend
print(arr)

#7. Remove any array element using remove() method.
print('answer 7')
arr.remove(21)
print(arr)

#8. Remove last array element using pop() method.
print('answer 8')
arr.pop()
print(arr)

#9. Fetch any element through its index using index() method.
print('answer 9')
print(arr[4])
print(arr.index(4))

#10. Reverse a python array using reverse() method.
print('answer 10')
arr.reverse()
print(arr)

#11. Get array buffer information through buffer_info() method.
print('answer 11')
print(arr.buffer_info())

#12. Check for number of occurrences of an element using count() method.
print('answer 12')
print(arr.count(1))

#13. Convert array to string using tobytes() method.
print('answer 13')
str2 = arr.tobytes()
print(str2)
#15. Append a string to char array using fromString() method.
ints = array('i')
ints.frombytes(str2)
print(ints)

#14. Convert array to a python list with same elements using tolist() method.
print('answer 14')
print(arr.tolist())

#16. Slice Elements from an array.
print('answer 16')
print(arr[1:5])
print(arr)
print(arr[0:5:2]) # start : end : step


