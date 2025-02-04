#BMI CALCULATOR

weight=float(input("Enter your weight: "))
unit= input("K(Kg) or L(Lbs)?")
height= int(input("What is your height?(in cm): "))
height= height/100

if  unit == "L":
    weight= round(weight / 2.205,1)
    unit= "Kg"
elif unit=="K":
     unit="Kg"
else:
    print(f"{unit} is not a valid unit")

   

if height<=0.3:
    print(f"Make sure that {height}(which is your height) is in cm!")
else:
    BMI= round(weight/height**2,1)

if BMI <= 18.4:
    status="Underweight"
elif  18.4 <= BMI <=24.9 :
    status="Normal"
elif  25.0 <= BMI <=39.9 :
    status="Overweight"
elif BMI >= 40.0:
    status="Obese"
    
    
print(f"Your Body Mass Index(BMI) is {BMI} and according the standardised BMI table, you are {status}!")
