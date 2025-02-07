import random

#print help(random) to access the rest of attributes available

low=1
high=100

options = ("rock", "paper", "scissors")
cards= ["2","3","4","5","6","7","8","9","10", "J","Q","K","A"]


# number = random.randint(low,high) generates a random integer number
# number = random.random() generates a random floating number
#option = random.choice(options) gives a random choice of option either rock,papers or scissors
#random.shuffle(cards) gives a random card


lowest_num =1
highest_num =100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running = True

print("PYTHON NUMBER GUESSING GAME")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:

    guess=input('Enter your guess: ')

    if guess.isdigit():
        guess=int(guess)
        guesses+= 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
        elif guess < answer:
            print("That number is too low!")
        elif guess > answer:
            print("That number is too high!")
        else:
            print(f"CONGRATULATIONS!! The correct answer is {answer}!")
            print(f'Number of guesses: {guesses}')
            is_running=False
      

    else:
        print("Invalid guess!")
        print(f" Please select a number between {lowest_num} and {highest_num}")
