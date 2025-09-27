x = int(input("Enter the radius of the circle (in cm): "))
def circumpherence(R):
    return R * 3.1428576 * 2
if x > 0:
    print("The circumpherence of the circle is approximately",circumpherence(x),"cm.")
else:
    print("The radius you gave,", x, ",is invalid")

