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