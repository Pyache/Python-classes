r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(r)
x1 = int(input("Print the first code number. of range: "))
x2 = int(input("Print the last code number of range: "))
while x1 <= x2:
    if x1 % 2 == 0:
        print("The square is even:", r[x1-1] ** 2)
    else:
        print("The square is odd:", r[x1-1] ** 2)
    x1 += 1