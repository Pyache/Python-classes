import random
number = str(random.randint(0, 9))
print("I will generate a number from 0 to 9, and you have to guess the number at a time.")
print("The game ends when you guess the number!")
while True:
    guess = input("Give me your best guess!: ")
    if number == guess:
        print("\nYou get one point!\nYou win the game!")
        print("The nunber was", number)
        break
    else:
        print("Your guess was incorrect...\nTry again!")

import random 
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors!\nYou WIN!")
        else:
            print("Paper covers rock!\nYou LOSE!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock!\nYou WIN!")
        else:
            print("Paper covers rock!\nYou LOSE!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cut paper!\nYou WIN!")
        else:
            print("Rock smashes scissors!\nYou LOSE!")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break


import math
print("The Floor and Ceiling value of 23.56 are: " + str(math.ceil(23.56)) + ", " + str(math.floor(25.56)))
x = 10
y = -15
print("The value of x after copying the sign form y is: " + str(math.copysign(x, y)))
print("Absolute values of -96 and 56 are: " + str(math.fabs(-96)) + ", " + str(math.fabs(56)))
print("The GCD of 24 and 56: " + str(math.gcd(24, 56)))
