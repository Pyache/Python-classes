"""print("Mirrored triangle (*)\nDesign- ◢")
while True:
    n = int(input("Enter the number of rows: "))
    count = n - 1
    counter = 0
    while counter != n:
        s = "  " * count
        b = "* " * (n-count)
        print(s,b)
        count -= 1
        counter += 1
    else:
        break"""

"""print("Mirrored triangle (*)\nDesign- ◢")
while True:
    n = int(input("Enter the number of rows: "))
    count = n - 1
    while count >= 0:
        s = "  " * count
        b = "* " * (n-count)
        print(s,b)
        count -= 1
    else:
        break"""

print("Mirrored triangle (*)\n\nDesign ==> ◢\n")
while True:
    n = int(input("Enter the number of rows: "))
    a = n
    while n > 0:
        s = "  " * (n-1)
        b = "* " * (a-(n-1))
        print(s,b)
        n -= 1
    else:
        break