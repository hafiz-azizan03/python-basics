#--------------------------------------------Object-oriented programming Python--------------------------------------------

# object = A "bundle" of related attributes (variables) and methods (functions)
#           You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

#class Car:
#    def __init__(self, model,year,color,for_sale): # init means initialize #this line of code is called constructor method(function) #self means the class which is car #we need to set the parameters(description of class)
#        self.model = model  #these are all variables that an object has
#       self.year = year
#       self.color = color
#        self.for_sale = for_sale
   
#    def drive(self):
#        print(f"You drive the {self.color} {self.model}")
    
#    def stop(self):
#        print(f"You stop the {self.color} {self.model}")
        
#    def describe(self):
#        print(f"{self.model} {self.color} {self.year}")


#methods are actions that objects can perform
#car1 = Car ("Porsche","2003","green", False)
#car2 = Car("Mustang","2024","blue",True)
#car3= Car("Mustang","2025","yellow", True)

#car1.drive()
#car1.stop()
#results
#You drive the green Porsche
#You stop the green Porsche

#--------------------------------------------Class variables--------------------------------------------

# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class
    
#class Student:

#   class_year = 2024  #this is what considered as class_variable in which both student1 and 2 can use the same variable
#    num_students=0    #this is also class variables which are shared datas

#    def __init__ (self, name, age):
#       self.name = name
#        self.age = age
##        Student.num_students += 1 # this will keep track of the number of students if we keep adding the object

#student1 = Student("Spongebob", 30)
#student2 = Student("Patrick", 35)

#print(student2.name)
#print(student2.age)
#print(student2.class_year)

#Patrick
#35
#2024

#print(student1.name)
#print(student1.age)
#print(student1.class_year)

#Spongebob
#30
#2024  #as we can see here, both of them have the same class_year bcs class year is a class_variable

#print( Student.num_students)

#results
#2 


#--------------------------------------------inheritance--------------------------------------------

# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               example class Child (Parent)


#we will make the parent as Animal, the child are cat,mouse and dog

#class Animal:
#    def __init__(self,name):  #defining a constructor
#        self.name = name
#        self.is_alive = True

#    def eat(self):
#        print(f"{self.name} is eating")
    
#    def sleep(self):
#        print(f"{self.name} is sleeping")

#class Dog(Animal):   # inside the parentheses, this is the parent and the Dog will inherit from Animal)
#        pass

#class Cat(Animal):
#    pass

#class Mouse(Animal):
#    pass                   #these are empty bcs this topic wants to teach how we can shorten the lines of codes

#dog = Dog("Scooby")
#cat= Cat("Garfield")
#mouse = Mouse("Mickey")

#print(mouse.name)
#print(mouse.is_alive)
#mouse.eat()
#mouse.sleep()

#results
#Mickey
#True
#Mickey is eating
#Mickey is sleeping   # as you can see, inheritance shortens the lines of codes and we donrt need to copu all the attributs into every single class,but instead we just invike it at the end


#--------------------------------------------multiple inheritance--------------------------------------------

# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A

#firstly we discuss on multiple inheritance

#class Prey:
#    def flee(self):
#        print("This animal is fleeing")

#class Predator:
#    def hunt(self):
#        print("This animal is hunting")

#class Rabbit(Prey):   # the rabbit will inherit the prey class
#    pass

#class Hawk(Prey):
#    pass

#class Fish(Prey, Predator):
#    pass

#rabbit = Rabbit()

#rabbit.flee()
#result = This animal is fleeing


#next, multilevel inheritance

#class Animal:         #in multilevel inheritance, Parents such as Prey and Predator can inherit from another parent which is the Animal
#    def sleep(self):
#        print("This animal is sleeping")

#class Prey(Animal):  #dont forget to add the (Animal) as parent to the prey and predator class
#    def flee(self):
#        print("This animal is fleeing")

#class Predator(Animal):
#    def hunt(self):
#        print("This animal is hunting")

#class Rabbit(Prey):   # the rabbit will inherit the prey class
#    pass

#class Hawk(Prey):
#    pass

#class Fish(Prey, Predator):
#    pass

#fish= Fish() #make sure to invoke first the fish class before asking it to be printed

#fish.sleep()
#result = This animal is sleeping


#--------------------------------------------super()--------------------------------------------
#super() = Function used in a chil class to call methods from a parent class(superclass)
#            Allows you to extend the functionality  of the inherited methods

#class Shape:
#    def __init__(self,color,is_filled):
#        self.color= color
#        self.is_filled=is_filled

#    def describe(self):
#        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

#class Circle(Shape):
#    def __init__(self,color,is_filled,radius):
#        super().__init__(color,is_filled)     #so what this does is,instead of writing repeated color and is_filled, we use the super function which shortens the codes
#        self.radius =radius

#class Square(Shape):
#     def __init__(self,color,is_filled,width):
#        super().__init__(color,is_filled)
#        self.width =width

#class Triangle(Shape):
#     def __init__(self,color,is_filled,width,height):
#        super().__init__(color,is_filled)
#        self.width =width
#        self.height =height

#circle = Circle(color="red",is_filled= True,radius =5) #we use keyword argumenments such as color, is_filled for the parameters but its not necessary, just for readability

#print(circle.color,circle.radius, sep=" and ") # the sep= wil, help separate the variables
#results = red and 5       

#circle.describe() #the child(circle) uses the parent's(shape) describe function 
#results = It is red and filled


#--------------------------------------------polymorphism--------------------------------------------
# polymorphism = to have many forms
#2 ways to achive polymorhism 
# 1) inheritance = an object that could be treated of the same type as a parent class
# 2) Duck typing = object must have necessary attributes/methods #we'll cover on the next topic

#from abc import ABC, abstractmethod

#class Shape:
    
#    @abstractmethod #this basiclly says that every shape has its own are and can be defined respectively
#    def area(self):
#        pass

#class Circle(Shape):
#    def __init__(self,radius):
#
#        self.radius = radius
#        
#    def area(self):
#        return 3.14 * self.radius ** 2

#class Square(Shape):
#    def __init__(self,side):
#        self.side = side
        
#    def area(self):
#        return self.side **2

#class Triangle(Shape):
#    def __init__(self,base,height):
#        self.base = base
#        self.height = height

#    def area(self):
#        return self.base * self. height * 0.5



#class Pizza(Circle): #eventhough this pizza(child) is super random, we can use it as a child to circle as both of them share the variable if radius
#    def __init__(self,topping,radius):
#        super().__init__(radius)   # instead of using self.radius = radius , we suse the super() function as we can put the parent of pizza as circle 
#        self.topping = topping
        



#shapes = [Circle(4),Square(5),Triangle(6,7), Pizza("pepperoni",15)]  # each of this object has different form or face

#for shape in shapes:
#    print (f"{shape.area()}cm²")
#results
#50.24cm²
#25cm²
#21.0cm²
#706.5cm²



#--------------------------------------------duck typing--------------------------------------------

#"Duck typing" = another way tp achieve polymorphism besides inheritance
#               objects must have the minimum necessary attributes/methods
#               "if it looks like a duck and quacks like a duck,it must be a duck"

#class Animal:
#    alive =True

#class Dog(Animal):
#    def speak(self):
#        print("WOOF!")

#class Cat(Animal):
#    def speak(self):
#        print("MEOW!")

#class Car:
    
#    alive = True

#    def speak(self):
#        print("HONK")

#animals = [Dog(), Cat(), Car()]

#for animal in animals:
#    animal.speak()
#    print(animal.alive)
    
#RESULTS
#WOOF!
#True
#MEOW!
#True
#HONK
#True                     # this seems goofy ik, but what we are trying to understand that if a class(Car) has the bare minimum attributes which are alive and can speak, then it can belong to the same group as Animal




#--------------------------------------------static methods --------------------------------------------

# Static methods =  A method that belong to a class rather tahn any object from that class(instance)
#                   usually used for general utility functions

#instance methods = best for operations on instances of the class(objects)
#static methods = best for utility functions that do not need access to classs data

#class Employee:

#    def __init__(self,name,position):    #this is a constructor method,  (__init__) for initializing new objects of the class.
#        self.name = name
#        self.position=position 

#    def get_info(self):  #instance method of get info and will retunr employee info
#        return f"{self.name} = {self.position} "

#    @staticmethod #decorator of static method
#    def is_valid_postion(position):  #since we're not working with object created in the class above, we dont need to put "self" in the parameter
#        valid_positions = ["Manager","Cashier","Cook","Janitor"]  #we make a list of valid positions
#        return position in valid_positions #we'll check if the postion is a valid position

#print(Employee.is_valid_postion("Cook"))  #this checks if the (job) i a valid postion
#print(Employee.is_valid_postion("rocket scientist"))

#results
#True
#False

#--------------------------------------------class methods --------------------------------------------

#class methods = allow operations related to the class itself
#               take (cls) as rhe first parameter,which represents the class itself

#class Student:

#    count=0 #dont forget to place the initial value of count

#    def __init__(self,name,gpa):
#        self.name= name
#        self.gpa = gpa
#        Student.count +=1 # firstly name of class which is Student followed with . and the what instruction
        
#    #instance method
#    def get_info(self):
#        return f"{self.name} : {self.gpa}"
    
#    @classmethod #to work with class data
#    def get_count(cls): # use cls as parameter bcs we are using the class data
#        return f"Total of students {cls.count}"

#student1 = Student("Ali",4.0)

#print(Student.get_count())  #result : 1



#--------------------------------------------magic methods --------------------------------------------

# Magic methods = Dunder methods (double underscore) _init_, __str__,__eq__(equality, to check if two of them are equal),__lt__(lessthan, to chek if lesser),__gt__(greater than, to check if greater), __add__(to add two values),__contains__(to search for a key values in an object), __getitem__ (to obtain the value of key stated within the parentheses after the self value in the object itself)
#                   They are automatically called by many of Python's built-in operations.
#                   They allow developers to define or customize the behavior of objects


#class Book:
    
#    def __init__ (self,title,author,num_pages) :
#        self.title = title
#        self.author = author
#        self.num_pages = num_pages

#    def __str__(self): #the __str__ method tells Python how to represent an object of your class as a string(on line 394)
#        return f"'{self.title}' written by {self.author} "

    #print(book1) #output : 'The Hobbit' written by J.R.R. Tolkien ,

#    def __eq__(self, other):  #other means that we are comparing two objects, which os this case is book1 and other books #(equality, to check if two of them are equal)
#        return self.title == other.title and self.author == other.author

    #print(book1 == book2) output: False(bcs both values are different)

#    def __lt__(self, other) :  #(lessthan, to chek if lesser)
#        return self.num_pages < other.num_pages

        #print(book1 < book3) output :False

    
#    def __gt__(self, other) :       #(greater than, to check if greater)
#        return self.num_pages > other.num_pages

#        #print(book1 > book3) output :True


#    def __add__(self, other) :
#        return f"{self. num_pages + other. num_pages} pages"

        #print(book1 + book3) output: 482 pages


#    def __contains__(self, keyword) :     #(to search for a key values in an object)
#        return keyword in self.title or keyword in self.author

    #print("Lion" in book3) output: True

#    def __getitem__(self, key):    #(to obtain the value of key stated within the parentheses after the self value in the object itself)
#        if key == "title":
#            return self.title
#        elif key == "author":
#            return self.author
#        elif key == "num_pages" :
#            return self.num_pages
#        else:
#            return f"Key {key} was not found"

    #print(book1["title"]) output: The Hobbit

#book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
#book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
#book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)                ##make sure to print the command below the data to make sure the data is read

#--------------------------------------------property decorator method --------------------------------------------
# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add additional logic when read(gets a value), write(sets a value), or delete(dekletes a value) attributes
#               Gives you getter, setter, and deleter method

#class Rectangle:
#    def _init_(self, width, height):
#        self ._ width = width
#        self ._ height = height

#   @property
#   def width(self):
#       return f"{self ._ width :. 1f}cm"

#   @property
#   def height(self):
#       return f"{self ._ height :. 1f}cm"

#   @width.setter
#   def width(self, new_width):
#       if new_width > 0:
#           self ._ width = new_width
#       else:
#    print("Width must be greater than zero")

#   @height. setter
#   def height(self, new_height):
#       if new_height > 0:
#           self ._ height = new_height
#       else:
    #print("Height must be greater than zero")
#   @width.deleter
#   def width(self):
        #del self ._ width
#       print("Width has been deleted")

#   @height.deleter
#   def height(self):
#       del self ._ height
#       print("Height has been deleted")


#rectangle = Rectangle(3, 4)
#rectangle.width = 5
#rectangle.height = 6

#del rectangle.width
#del rectangle.height


#-------------------------------------------- decorator method --------------------------------------------

## Decorator = A function that extends the behavior of another function
#               w/o modifying the base function
#               Pass the base function as an argument to the decorator



#               @add_sprinkles           #we are adding decorations to thebase function without changing the base function, bcs somtimes ppl dont like sprinkles to their vailla ice cream
#               get_ice_cream("vanilla") #this is the base function


#def add_sprinkles(func): #decorator function
#        def wrapper(*args,**kwargs):
#            print("*You add sprinkles🎊*")
#            func()
#        return wrapper

#def add_fudge(func):  #another decorator
#    def wrapper(*args,**kwargs):
#        print("*You add fudge 🍫*")
#        func()
#    return wrapper

#@add_sprinkles
#@add_fudge           #decorator
#def get_ice_cream():   #this is the base function
#    print("Here is your ice cream 🍦")

#get_ice_cream()

#results:
#*You add sprinkles🎊*
#*You add fudge 🍫*
#Here is your ice cream 🍦     

#So what happens here is you can print the get_ice_cream without the decorators, on line 516, remove the previous decorators 
#but in this case, you put decorators for both fudge and sprinkles so thats why you got both decorators and ice cream


#-------------------------------------------- exception handling --------------------------------------------

# exception = An event that interrupts the flow of a program
#            (ZeroDivisionError(ex: 1/0), TypeError(ex: 1+"1"), ValueError(ex: int("pizza")))
#             1. try, 2.except, 3. finally

#example
#try:
# # Try some code
#except Exception :
## Handle an Exception
#finally:
### Do some clean up

#try:
#    number = int(input("Enter a number: "))
#    print(1 / number)
#except ZeroDivisionError:
#    print("You can't divide by zero IDIOT!")
#except ValueError:
#    print("Enter only numbers please!")
#except Exception:
#    print("Something went wrong!")
#finally:
#    print ("Do some cleanup here")

# so what this actually does is we are intentionally casuingan error event such as ZeroDivisionError, ValueError and so on but we are expecting it. So we want to accpet thos errors gracefully and return that with a message to the user.The finally part basically sends a message regardless if the exception condition is met or not.



#-------------------------------------------- file detection --------------------------------------------

#import os  #os means operating system,provides a way for a python to interact with the os 

#file_path =  "test.txt" 

#file path can either be relative or absolute
#Relative = folder/test.txt
#Absolute = C:/Users/BroCode/Desktop/test.txt

#if os.path.exists(file_path): #in english: by accessing the os module,access the path and using a built in method of exists, see if a file exists
#    print(f"The location '{file_path}' exists")

#if os.path.isfile(file_path): #check if the file is a file
#    print(f"That is indeed a file")

#if os.path.isdir(file_path): #check if the stated path is indeed a directory
#    print(f"That is indeed a directory")

#else:
#    print("This file doesn't exists")

#result: The location 'test.txt' exists

# we can also rewrite the file path by copying the directory of path and pasrting it in the built in exists method





#-------------------------------------------- writing files --------------------------------------------

# Python writing files (.txt, . json, .csv(comma separated values))

# these are using txt files

#txt_data = "I like pizza" #text data we would like to output

#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.txt"  #when we generate this file, t will be withon the same file as our main python file project

#with open(file=file_path,mode="w") as file: #'with' is a statement will open and close a file, 'open' will return a file object, "w" is write, ("x" is write but will only write if there is no path file(existing file), "a" is append and "r" is for read)  and 'as' will rename the file object so it will be renamed as file in our case
#    file.write(txt_data)
#    print(f"txt file '{file_path}' was created") 

#result: txt file 'output.txt' was created


#and in the directory of C:\\Users\\justi\\OneDrive\\Desktop\\output.txt, you can see a txt file with the content of i like pizza

#smth more complex

#employees = ["Eugene", "Squidward", "Spongebob", "Patrick"] #we have a list f employees to put in a text file

#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.txt"

#try:    #by using a try block and catching any exceptions, we can expect errors and program is not interrupted
#    with open(file_path, "w") as file:    "w" is write, ("x" is write but will only write if there is no path file(existing file), "a" is append and "r" is for read)
#        for employee in employees :
#            file. write(employee + "\n")  #\n creates a new line
#        print(f"txt file '{file_path}' was created")

#except FileExistsError:
#    print("That file already exists!")


# now a list of employees in a text data is made

#results:
#Eugene
#Squidward
#Spongebob
#Patrick

# now using json files

#import json  #make sure to use the json module

#employee = {           # a dictionary with keys and values
#"name": "Spongebob",
#"age": 30,
#"job": "cook"
#}

#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.json"
#try:
#    with open(file_path, "w") as file:
#        json.dump(employee, file, indent=4)  #dump mehtod converts our dictionary to a json string, indentation separates the key value pair by 4
#    print(f"json file '{file_path}' was created")
#except FileExistsError:
#    print("That file already exists!")

#results:
#{
#    "name": "Spongebob",
#    "age": 30,
#    "job": "cook"
#}


#now using csv file

#import csv  #dont forget to import the module beforehand

#employees = [ [ "Name", "Age", "Job"],  #this is a 2d strcuture, similar to a row collumn sysytem 
#["Spongebob", 30, "Cook"],
#["Patrick", 37, "Unemployed"],
#["Sandy", 27, "Scientist"]]

#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.csv"

#try:
#    with open(file_path, "w", newline="") as file:  #
#        writer = csv.writer(file)      #writer object to write to a file, then we access the csv module use the write method of the module inside the file
#        for row in employees :         #we need to itirate over every row by using this line of code
#            writer.writerow(row)
#        print(f"csv file '{file_path}' was created")
#except FileExistsError:
#    print("That file already exists!")


#-------------------------------------------- reading files --------------------------------------------

#   HOW TO READ A TXT FILE

#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.txt"

#try:
#    with open(file_path, "r") as file:
#        content = file. read ()
#        print(content)
#except FileNotFoundError :
#    print ("That file was not found")
#except PermissionError :
#    print("You do not have permission to read that file")

#RESULTS I like pizza

#HOW TO READ JSON FILE

#import json
#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.json"

#try :
#    with open(file_path, "r") as file:
#        content = json. load(file) #BY ACCESSING THE JSON MODULE, use the load method and load our file
#        print (content)
#except FileNotFoundError :
#    print ("That file was not found")
#except PermissionError:
#    print("You do not have permission to read that file")

#RESULTS: {'name': 'Spongebob', 'age': 30, 'job': 'cook'}

# HOW TO READ CSV FILE

#import csv
#file_path = "C:\\Users\\justi\\OneDrive\\Desktop\\output.csv"

#try:
#    with open(file_path, "r") as file:
#        content = csv.reader(file)  #access csv module,access reader method and pass the file
#        for line in content:  #you need this line of code to reiterate every line
#            print(line)
#except FileNotFoundError :
#    print("That file was not found")
#except PermissionError:
#    print("You do not have permission to read that file")

#results 
#['Name', 'Age', 'Job']
#['Spongebob', '30', 'Cook']
#['Patrick', '37', 'Unemployed']
#['Sandy', '27', 'Scientist']

#results:
#Name,Age,Job
#Spongebob,30,Cook
#Patrick,37,Unemployed
#Sandy,27,Scientist

#-------------------------------------------- dates and time --------------------------------------------

import datetime

date = datetime.date(2025, 1, 2)  #access the datetime module and use date method
today = datetime.date(2025,2,18)
time = datetime.time(12,30,0)
now = datetime.datetime.now()  #access the datetime module, datetime class adn the now method, this will read what the system's time now 

now = now.strftime("%H:%M:%S %d %m %y")    #strftime - string format time #the percent specifiers helps the appearanceof the time and date

target_datetime = datetime.datetime(2030,1,2 ,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime<current_datetime:
    print("The target date has passed")

else:
    print("The target date hasn't passed")











