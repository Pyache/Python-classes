import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
part1a = random.choice(letters)
part1b = random.choice(letters)
part1c = random.choice(letters2)
characters = ['#', '_', '-', '/', '!', '@']
part2a = random.choice(characters)
part2b = random.choice(characters)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
part3a = random.choice(numbers)
part3b = random.choice(numbers)
password_final = str(part1a) + str(part2a) + str(part3a) + str(part1b) + str(part1c) + str(part2b) + str(part3b)
print("The password is: ", password_final)