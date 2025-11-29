class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if (self.a < other.a):
            return "Ob1 is less than Ob2."
        else:
            return "Ob2 is less than Ob1."
    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal."
        else:
            return "Not equal."
ob1 = A(2)
ob2 = A(3)
print("Passed Values: ", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values: ", ob3.a, ob4.a)
print(ob3 == ob4)


class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '(' + self.meaning + ')'
flash = []
print("Welcome to the Flashcard Application.")
while(True):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to add an "
    "another flashcard, otherwise enter 1: "))
    if (option):
        break
print("\nYour flashcards: ")
for i in flash:
    print("»", i)


import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {"apple":"red",
                       "orange":"orange",
                       "watermelon":"green",
                       "banana":"yellow"}
# Function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option = int(input("enter 0, if you want to play again otherwise enter 1: "))

            if (option):
                break

print("welcome to fruit quiz ")
fq = FruitQuiz()
fq.quiz()