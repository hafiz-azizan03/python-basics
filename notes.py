#------------------------------------function------------------------------------
# function= A block of reusable code
#           place () after the function name to invoke it

#def happy_birthday():
#    print("Happy birthday to you!")
#    print("You are old!")

#happy_birthday() # this will be defined as a function and the happy_birthday will have the line 5 and 6 stored in it

# def happy_birthday(name,old): # what would happen here is the name adnd age will be substituted into the argument which is Pijan and 22
#    print(f"Happy birthday to {name}!")
#    print("You are {age} years old!")

#happy_birthday("Pijan",22) # in this scenario,the data Pijan is sent to the function of happy_birthday and this Pijan data is called an argument(positional argument) since it is stored in between ""

#------------------------------------return------------------------------------

#return= statement used to end a function and send a result back to the caller

#def add(x,y):
#    z=x+y
#    return z

#def subtract(x,y):
#    z=x-y
#    return z

#def multiply(x,y):
#    z=x*y
#    return z
#def divide(x,y):
#    z=x/y
#    return z

#print(add(1,2))
#print(subtract(1,2))
#print(multiply(1,2))
#print(divide(1,2))


#------------------------------------default_argument------------------------------------

#

#default arguments = A default value for certain parameters
#                      default is used when that argument is omitted make your functions more flexible, reduces # of arguments
#                      1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

#import time

#def count(start, end=10): # the =0 will indicate the data as a constant or other words default, which why we call it a default
#    for x in range(start, end+1): # +1 because the last value is exlusive so by +1 we will ahve the number 10
#        print(x)
#        time.sleep(1) #delays each count by 1 secondd

#print("DONE!")

#count(1) #as seen here, we only have the data for start but no end becasue end data is already a constant or default

#------------------------------------keyword_argument------------------------------------

#keyword arguments = An argument preceded ny an idnetifier
#                    helps with readability
#                    order of arguments doesn't matter
#                      1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

#def get_phone(country,telco,first,last):
#    return f"{country}-{telco}-{first}-{last}"

#phone_num = get_phone(country=60,first=323,telco=18,last=8526) #as we can see here, the order doesnt matter and the telco and first has switched places, ultimately it will follow the initial defintion so everything will end up in order

#print(phone_num)



#------------------------------------arbitary_argument------------------------------------

# *args = allows you to pass multiple non-key arguments args=arguments ,args are considered as tuples
# **kwargs = allows you to pass multiple keyword-arguments kwargs=key word arguments, kwargs are considered as dictionary
#            * unpacking operator
# arbitary actually means varying or in this case varying arguments

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg, end=" ")
#    print()

#    if "apt" in kwargs:
#        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#    elif "pobox" in kwargs:
#        print(f"{kwargs.get('street')}")
#        print(f"{kwargs.get('pobox')}")
#    else:
#        print(f"{kwargs.get('street')}")

#    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

#shipping_label("Dr.", "Spongebob", "Squarepants",
#                street="123 Fake St.", 
#                pobox="PO box #1001",
#                city="Detroit",
#                state="MI",
#                zip="54321")



#------------------------------------iterables------------------------------------

#Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop
#             list,tuples,sets are considered as iterables

#------------------------------------Membership operators------------------------------------

# Membership operators = used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in


#------------------------------------List comprehension------------------------------------

#List comprehension =   A concise way to create lists in Python 
#                      Compact and easier to read than traditional loops 
#                      [expression for value in iterable if condition]

# below is a traditional loop to create double figures of a set
#doubles = []
#for x in range(1,11):
#    doubles.append(x *2)
#print(doubles)

#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# below is a list comprehension,much shorter version than above

# doubles = [expression for value in iterable]
#doubles=[x*2 for x in range(1,11)]
# print(doubles)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# we can even use it for list of strings using the same formula [expression for value in iterable]


#------------------------------------Match-case statement------------------------------------
# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

#this is a standard loop using elifs statements, too many elifs if you ask me

#def day_of_week(day):
#    if day == 1:
#        return "It is Sunday"
#    elif day == 2:
#        return "It is Monday"
#   elif day == 3:
#        return "It is Tuesday"
#    elif day == 4:
#        return "It is Wednesday"
#    elif day == 5:
#        return "It is Thursday"
#    elif day == 6:
#        return "It is Friday"
#    elif day == 7:
#        return "It is Saturday"
#    else:
#        return "Not a valid"
#print (day_of_week(1))

#this the same thing but using match case statement

#def is_weekend (day):
#    match day:
#        case "Saturday" | "Sunday":
#            return True
#        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#            return False
#        case _:
#            return False

#print(is_weekend("Friday"))

#------------------------------------modules------------------------------------

# module = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program reusable separate files


# import math
#import math as m #using aliases can shorten the module
#print(m.pi)

#print(help("modules")) # to obtain list


#------------------------------------scope resolution------------------------------------

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

#local
#def func1(): #When Python encounters a function definition (using the def keyword), it reads and stores the function's code. However, it does not execute the code inside the function at that point. It essentially remembers the instructions within the function for later use.
#    a = 1 #in this case a=1, this is value is stored locally and and python will serarch for local first
#    print(a)

#def func2():
#    b = 2
#    print(b)

#func1()
#func2() # Nothing happens until we call the functions


#enclosed
#def func1():
#    x = 1
#    
#    def func2():
#        print(x)
#    func2()
#func1()

#in this case, the value x=1 is enclosed and no local value so if we have the value x=2 below the line def func 2, it will use that value of x=2 because by order, python will find local first and the enclosed. i

#global
#def func1():
#    print(x)
#def func2():
#    print(x)
#x = 3        #this value is considered global, so the results will end up having two values of 3 from each func
#func1()
#func2() 

#Built-in
#from math import e # this value of e is considered built in since we imported this value
#def func1():
#    print(e)
#e = 3     #however upon running this script, it will use this value bcs this value is global and by the order, global comes first before built in
#func1() 




#------------------------------------if __name__ == '__main__':------------------------------------

# if name main_ : (this script can be imported OR run standalone)
#                   Functions and classes in this module can be reused
#                    without the main block of code executing
#def main():
        #  Your program goes here

#if __name__ ==  '_main__':
#   main()
