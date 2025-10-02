def due(x, y):
    return y - x
b = int(input("Enter the total amount to be paid: ₹ "))
c = int(input("Enter the amount given: ₹ "))
if b <= 0 and c <= 0 or b <= 0 or c <= 0 or b < c:
    print("Invalid input...")
elif b > 0 and c > 0:
    print("The change to be given is ₹", due(b, c))
else:
    print("Invalid input...")