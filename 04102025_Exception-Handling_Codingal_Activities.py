try:
    num = int(input("Enter your number: "))
    print(num)
except ValueError as ex:
    print("Exception: ", ex)


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ", result)
    print("Result is : ", result1)
except ZeroDivisionError:
    print("Division by 0 is not possible!")
except ValueError:
    print("Please enter a numerical value!")
except NameError as ex:
    print("The exception is ", ex)
except:
    print("Some error occured.")
finally:
    print("I will execute no matter what happens!")

valid = False
while not valid:
    try:
        x = int(input("Enter your number: "))
        while x % 2 == 0:
            print("Bye!")
        valid = True
    except ValueError:
        print("Invalid!")