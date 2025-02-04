weight=float(input("Enter your weight(only digits):"))
unit= input("K(Kg) or L(Lbs)?")

if unit== "K":
    weight= weight * 2.205
    unit= "Lbs"
    print(f"You are {round(weight,1)}{unit}")
elif unit == "L":
    weight= weight / 2.205
    unit= "Kg"
    print(f"You are {round(weight,1)}{unit}")

else:
    print(f"{unit} is not a valid unit!")


