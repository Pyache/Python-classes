set1 = {1, 2, 3}
print(set1)
set2 = {1.0, 'Hello', (1, 2, 3)}
print(set2)
set3 = {1, 2, 3, 4, 3, 2}
print(set3)
set4 = set([1, 2, 3, 2])
print(set4, "\n")
set5 = set([0, 1, 2, 3, 4, 5])
print("Original set: ")
print(set5)
set5.pop()
print("After removing the first element from the set: ")
print(set5, "\n")


setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements: ")
print(setx)
print(sety)
print("\nIntersection of two sets: ")
setz = setx.intersection(sety)
print(setz)


import array as arr
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: " + str(array_num))
print("Number of occurences of the number 3 in the above array: " + str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))