try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print(age, "is even.")
    elif age % 2 == 1:
        print(age, "is odd.")
    elif age <= 0:
        print("Age cannot be less than equal to 0.")
    elif age >= 150:
        print("Age cannot be more than 150.")
except ValueError:
    print("Invalid input.\nAge cannot be expressed in letters...")
    pass
except NameError:
    print("Invalid input.")
    pass
except:
    print("Some error occured.")
    pass
print("Please do not enter some other unnessesary inputs...")
try:
    age = int(input("Re-enter your age: "))
    if age % 2 == 0:
        print(age, "is even.")
    elif age % 2 == 1:
        print(age, "is odd.")
    elif age <= 0:
        print("Age cannot be less than equal to 0.")
    elif age >= 150:
        print("Age cannot be more than 150.")
except ValueError:
    print("Invalid input.\nAge cannot be expressed in letters...")
except NameError:
    print("Invalid input.")
except:
    print("Some error occured.")
print("Restart the program please!")
