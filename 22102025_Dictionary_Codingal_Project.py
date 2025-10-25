test = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print(test)
val = input("Enter the value you want to check the frequency for: ")
f = 0
for key, value in test.items():
    if str(key) == val:
        f += 1
    if str(value) == val:
        f += 1
print("The frequency of ", val, " in the dictionary is: ", f)