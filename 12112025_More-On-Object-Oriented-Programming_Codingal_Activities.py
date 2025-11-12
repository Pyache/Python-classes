class IOString:
    def __init__(self):
        self.str1 = ''
    def get_String(self):
        self.str1 = input("Enter a string: ")
    def printstring(self):
        print("The original value was: ", self.str1)
        print("The result is: ", self.str1.upper())
str1 = IOString()
str1.get_String()
str1.printstring()


class Employee:
    def __init__(self):
        print("Employee Created.")
    def __del__(self):
        print("Destructor Called.")
def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function End...")
    return obj
print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End...")


class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target- num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
value = int(input("Enter the sum for which you want to make this search: "))
print("index1 = %d, index2 = %d" % pair_elements().twoSum((10, 20, 30, 40, 50 ,60, 70), value))
