import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") #7 different Unicode respectively
#● ┌ ─ ┐ │ └ ┘ this is needed to produce ACSII art (American Standard Code for Information Interchange)

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: ")) #make sure it is an integer

for die in range(num_of_dice): #For each die we want to roll (up to the total number of dice we specified) *die is singular noun for dice 
    dice.append(random.randint(1, 6)) # 1)generate a num from 1-6,add that value into the dice

#for die in range(num_of_dice): #this outer loop will be in chaerged for num of dice
#    for line in dice_art.get(dice[die]): #this inner for loop will be in charged for printing tuple. 1) die value is taken from user input(example 3) 2) dice_art.get(3) will get the 3rd dice art and stores it in line
#       print(line)

for line in range(5): #For each line (from 0 to 4) of the ASCII art representation of the dice
    for die in dice: #for each die roll in our dice list(lets say we have 3 die roll with values 3,5,1)
        print(dice_art.get(die)[line], end="") #.get the ASCII art for that die value, then get the specific line of that art which are 3,5 and 1 (based on the outer loop), and print that line without adding a newline character.
    print()


for die in dice:
    total += die
print(f"Total: {total}")
