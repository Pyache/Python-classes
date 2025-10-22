tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

d = -1
l = 1
for i in range(6):
   l = tup1[d] * l
   d = d - 1
print("The product of the values in tup1 is: \n", l, "\n\n")

d2 = - 1
l2 = 1
for i in range(7):
   l2 = tup2[d2] * l2
   d2 = d2 - 1
print("The product of the values in tup2 is: \n", l2, "\n\n")

p = l * l2
print("The product of all values in tup1 and tup2 is: \n", p, "\n\n")