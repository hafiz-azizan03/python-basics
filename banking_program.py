#Python Banking Program

def show_balance(balance):
    print(f"Your amount of balance in your account is RM{balance:.2f}")

def deposit():
    amount = float(input("How much would you like to deposit for today?: "))
    
    if amount < 0 :
        print("Please enter a valid amount of money")
        return 0 # return 0 basically sends 0 data, or basically nothing
    else:
        return amount #if no conditions is met, then the value from the input is returned to the amount
       

def withdraw(balance):
    amount = float(input("How much would you like to withdraw for today?: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0 :
        print("Please enter a valid amount of money")
        return 0
    else:
        return amount

def main():  #this def allows us to import the main codes below

    balance=0
    is_running =True



    while is_running:
        print("********************")
        print("Banking Program")
        print("********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("********************")

        choice= input("Enter your choice 1-4: ")

        if choice == '1':
            show_balance(balance) #this invoked function will refer to the line code 3 where we define the show_balance
        elif choice== '2':
            balance += deposit()
            print("********************")
            print(f" Your balance amount is {balance:.2f} ") 
        elif choice=='3':
            balance -= withdraw(balance)
            print("********************")
            print(f" Your new balance amount is {balance:.2f} ")    
        elif choice=='4':
            is_running=False #bacillay were telling the program to stop working as we set earlier is_running=True, so it will then go to line 64 as the outdented part and print that line
        else:
            print("********************")
            print("Invalid input, please enter either 1-4")


    print("Thank you for using our service, have a nice day!")

if __name__=='__main__':  #not too sure as to what this actually do, will do further research (10 feb 25')
    main() 
