#Python Slot Machine

import random
import time

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']

#    results = []
#    for symbol in range(3):
#        results.append(random. choice (symbols))
#    return results                                          #this is if you are not using list comprehension

#by using list_comprehension below,it is more concised
    return[random.choice(symbols) for _ in range(3)] # in english: for every iteration(until 3) use the expression(pick a random symbol) #the placeholder(_) is used instead of 'symbol'

def print_row(row):
    print("***************")
    print(" | ".join(row)) # by using the join method, we are joining all the itirables(the three symbols) with a " " or space # we get | from alt+1+2+4
    print("***************")

def get_payout(row,bet):
    if row[0] == row [1] == row [2]:
        if row [0] == '🍒':
            return bet * 2
        elif row[0] ==  '🍉':
            return bet * 4
        elif row[0] ==  '🍋':
            return bet * 10
        elif row[0] ==  '🔔':
            return bet * 25
        elif row[0] ==  '⭐':
            return bet * 50
    return 0

def main():
    balance=100

    print("**********************************")
    print("Welcoe to My Casino Slot Machine")
    print("The fruits(multiplier):🍒(x2) 🍉(x4) 🍋(x10) 🔔(x25) ⭐(x50) ")
    print("**********************************")

    while balance > 0:
        print(f" Your current balance is RM{balance}")

        bet = input("Enter the amount of bet you would like to place: ")

        if not bet.isdigit():
            print("Please enter a valid amount!")
            continue

        bet= int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <=0:
            print("The amount should be more than zero")
            continue

        balance -= bet

        row = spin_row() #row is a list
        print("Spinng.....\n")   #\n makes space after the word spinning
        for x in range(3, 0, -1):  # Countdown from 3 to 1
            print(x)
            time.sleep(1)  # Wait for 1 second
        print_row(row)

        payout= get_payout(row,bet)

        if payout > 0:
            print(f" Congratulations! You won RM{payout}")
        else:
            print("Wom womp, you lost")

        balance += payout

        play_again= input("Do you want to spin again? (y/n): ").lower()

        if play_again != 'y':
            break

    print("**********************************")
    print(f"Thanks for playing! Your final balance is RM{balance}")
    print("**********************************")

if __name__== '__main__':
    main()
