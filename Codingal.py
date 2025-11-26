class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed_string(self):
        return self.s[::-1]
user_input = input("Enter a string: ")
my_string_reverser = Reverse(user_input)
reversed_string = my_string_reverser.get_reversed_string()
print("Reversed string:", reversed_string)