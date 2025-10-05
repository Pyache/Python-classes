x = 1000000000
for d in range(x):
    try:
        age = float(input("Enter your age: "))
        d = round(age)
        if age >= 150:
            print("Invalid Input...\nAge cannot be more than 150.\nPlease enter a proper age.")   
        elif age <= 0:
            print("Invalid Input...\nAge cannot be less than equal to 0.\nPlease enter a proper age.")
        elif age != d:
            print("Invalid Input...\nPlease enter a proper age.")
        elif age % 2 == 0:
            print(age, "is even.")
            break
        elif age % 2 == 1:
            print(age, "is odd.")
            break
    except ValueError:
        print("Invalid Input...\nAge cannot be expressed in letters or characters\nPlease enter a proper age.")
    except NameError:
        print("Invalid age...\nPlease enter a proper age.")
    except:
        print("Some error occured...\nPlease enter a proper age.")