x = float(input("Enter the radius of the circle (in cm): "))
def circumference(R):
    return R * 3.1428576 * 2
if x > 0:
    print("The circumference of the circle is approximately",circumference(x),"cm.")
else:
    print("The radius you gave,", x, ",is invalid")

