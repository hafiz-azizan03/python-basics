#PYTHON Quiz game

#() - tuples  ,ordered and unchangeable. Duplicates OK. FASTER
#[] - sets unordered and immutable, but Add/Remove OK. NO Duplicates
questions=(" What is the chemical symbol for gold?: ",
          " What is the world's largest ocean?: ",
          " What is the capital of Australia?: ",
          " What is the name of the longest river in the world?: ",
          " What is the capital city of Brazil? :")

#2D tuple
options = ((("A. Ag ","B. Em ","C. Au ","D. Gd ")),
           (("A. Atlantic Ocean ","B. Indian Ocean ","C. Artic Ocean ","D. Pacific Ocean ")),
           (("A. Sydney ","B. Melbourne ","C. Canberra ","D. Perth ")),
           (("A. Nile River ","B. Amazon River ","C. Yangtze River ","D. Mississippi River ")),
           (("A. Eio de Janeiro ","B. Sao Paulo ","C. Brasillia ","D. Buenos Aires "))) 

answers=("C","D","C","A","C") #tuple bcs we will be appending guesses, Mmake sure that we use tuples as the answers should be in order and unchangeable
guesses= [] #make sure we sets as the guesses would be unordered and immutable(NO Duplicates)
score=0
question_num=0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+= 1
        print("CORRECT!")
    else:
        print('INCORRECT!')
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("---------------------------------")
print(f"You got {score} questions correct!")
score = int(score / len(questions) *100)
print(f"Your score is {score}%")
print("---------------------------------")
