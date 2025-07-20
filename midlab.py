import random

random.randint(1, 10)
secret_number = 4

guess = int(input("Guess a number between 1 and 10: "))

match guess:
    case int(): 