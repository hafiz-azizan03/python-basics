import random

options = ("rock","paper","scisssors")
running=True

while running: # we make a while loop with running set as true so that the game can keep going on until it stops by a specific command 

    player = None
    computer = random.choice(options)

    while player not in options: #this is refeering to when the players picks an invalid option
        print("Choose only either rock,paper or scissors!")
        player= input("Enter a choice (rock,paper,scissors): ").lower()

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("It's a tie!")
    elif player =="rock" and computer == "scissors":
        print("You win!")
    elif player=="paper"and computer== "rock":
        print("You win!")
    elif player=="scissors"and computer== "paper":
        print("You win!") 
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y": #in english, if users input does not equalts to y, then running is false and the game ends
     running = False

print("Thanks for playing the game!")
