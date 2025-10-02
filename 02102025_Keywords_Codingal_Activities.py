x = input("Enter your word: ")
for i in (x):
    if i == "a":
        print(i,"-A is present in the word!")
        break
    else:
        print(i,"-A is not present in the word!")

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

x = int(input("Enter your number: "))
if x % 20 == 0:
    print("twist.")
elif x % 15 == 0:
    pass
elif x % 5 == 0:
    print("fizz.")
elif x % 3 == 0:
    print("buzz.")
else:
    print(x)