class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * 3.14159265359
    def perimeter(self):
        return self.radius * 2 * 3.14159265359
try:
    radius_input = float(input("Enter the radius of the circle: "))
    if radius_input < 0:
        print("Radius cannot be negative. Please enter a positive value.")
    else:
        my_circle = Circle(radius_input)
        print(f"The area of the circle is: {my_circle.area():.2f}")
        print(f"The perimeter of the circle is: {my_circle.perimeter():.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")