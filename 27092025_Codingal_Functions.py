def well_wishes():
    print("Hello, how are you?")
well_wishes()


spring = "autumn"
autumn = spring

def weather_condition():
    print("The weather is pleasant in:",spring)
    print("The weather is also the same in", autumn)
weather_condition()

def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print("Please select  the operation: ")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice = input("Please enter your choice: ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter your second number: "))
if choice == "a":
    print(add(num_1,num_2))
elif choice == "b":
    print(subtract(num_1,num_2))
elif choice == "c":
    print(multiply(num_1,num_2))
elif choice == "d":
    print(divide(num_1,num_2))
else:
    print("This is an invalid input.")
 
