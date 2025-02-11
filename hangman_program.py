#Hangman in python
import random

words = ('apple', 'banana', 'orange', 'grape', 'strawberry', 'blueberry', 'raspberry', 'watermelon', 'mango', 'kiwi', 'pineapple', 'peach', 'plum', 'cherry', 'pear', 'lemon', 'lime', 'avocado', 'coconut', 'durian')
#set of words to be chosen at random

#dictionary of key:()
hangman_art =               {0: ("   ",                     #ascii art, 0-6 represents the # of guesses
                                 "   ",
                                 "   "),
                             1: (" o ",
                                 "   ",
                                 "   "),
                             2: (" o ",
                                 " | ",
                                 "   "),
                             3: (" o ",
                                 "/| ",
                                 "   "),
                             4: (" o ",
                                 "/|\\",
                                 "   "),
                              5: (" o ",
                                  "/|\\", #to print the right hand or backslash \, you need to put two \\ because singular \ is the exit command in python
                                  "/  "),
                              6: (" o ",
                                  "/|\\", 
                                  "/ \\")}

def display_man(wrong_guesses):  #when we diplay man. we need to know the number of wrong guesses(parameter)
    print("*******************************")
    for line in hangman_art[wrong_guesses]:  #for every wrong guess,display the corresponding line in the hangman_art set
        print(line)
    print("*******************************")

def display_hint(hint):        # hint will be a list of _ characters
    print(" ".join(hint))

def display_answer(answer):     #displayed when win or lose the game
    print(" ".join(answer))     #prints the letters of the answer joined by a space"_"

def main():
    answer = random.choice(words) #gives the random choice from set of words
    hint = ["_"] * len(answer) #this will place _ in the terminal and will be multiplied by the len which is the number of charcters in the word
    wrong_guesses= 0
    guessed_letters = set() #we want an empty set at the intial phae of the game bcs we're just starting, however we cannot put an empty set (), so instead we use set()
    is_running =True # put False if we want to end the game

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess= input("Enter your guess of letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input,only guess a letter!: ")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter {guess}")
            continue

        guessed_letters.add(guess)




        if guess in answer:                #If the player's guess is correct (the letter is in the word), the code iterates through the secret word, and for every position where the letter matches the guess, it updates the "hint" list to reveal that letter to the player.
            for i in range(len(answer)):   # in the reange of letters (lets say  6 for banana), and letter b is in the first index(i)
                if answer[i] == guess:     #if the letter guessed is the same as answer, as well revealing the inde of the letter in the answer...
                    hint[i] = guess        #then replace the guessed letter into the hint(which are underscores) 


        else:
            wrong_guesses +=1

        if "_" not in hint:                #this means that all letters have been guessed
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        
        elif wrong_guesses >= len(hangman_art) - 1:   #7-1 bcs in the acsii art we have 7 different key values and on the 6th is the art where we lose the game
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False  

            


if __name__=="__main__":
    main()
