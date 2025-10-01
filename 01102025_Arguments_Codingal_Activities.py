x = int(input("Enter the total amount: "))
y = int(input("Enter the percentage of the tip you want to give: "))
def total_calc(bill_amount, tip_perc=y):
    total = bill_amount*(1 + 0.01*tip_perc)
    print(f"Please pay {total}")
total_calc(x)


def cube(number):
    return number**3
def by_three(number):
    if number % 3== 0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))


def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The factorial of 4 :", factorial(4))
print("The factorial of 3 :", factorial(3))
print("The factorial of 7 :", factorial(7))
print("The factorial of 2 :", factorial(2))
print("The factorial of 5 :", factorial(5))
print("The factorial of 9 :", factorial(9))