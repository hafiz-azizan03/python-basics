#dictionary = a collection of {key:value} pairs ordered and changeable.NO Duplicates

# print(dir(capitals)) list of all attributes available
#print(help(capitals)) indepth descriptions

capitals ={"USA":"Washington DC" ,
          "India":"New Delhi",
          "Malaysia":"Kuala Lumpur",
          "Russia": "Moscow"}

#print(capitals.get("USA")) - we will get the value from the key
#capitals.popitem() clear the latest item *moscow
#capitals.pop("India") removes the key
#capitals.keys() returns all the keys within a dictionary
#capitals.values() returns all the values within a dcitionary
#capitals.items() returns a dictionary in the form of 2D tuples

menu = {"Nasi Lemak(NL)": 2.00,
        "Cekodok(CK)": 0.80,
        "Karipap(KR)": 0.60,
        "Donut(DN)": 1.50,
        "Popia(PP)": 1.20,
        "Keropok Lekor(KL)": 0.50}

code_to_item = {
    "nl": "Nasi Lemak(NL)",
    "ck": "Cekodok(CK)",
    "kr": "Karipap(KR)",
    "dn": "Donut(DN)",
    "pp": "Popia(PP)",
    "kl": "Keropok Lekor(KL)"
}
#make codes to ease the users when placing orders

cart = []
total=0

print("----------MENU----------")
print("Key in the code in the brackets when placing the order")
print()
for key,value in menu.items():
    print(f"{key:10} : RM{value:.2f}") #:10 is the spacing, :2f is the decimal places which is two
print("------------------------")

while True:
    food_code = input("Select an item (code, q to quit): ").lower()

    if food_code == "q":
        break

   
    if food_code in code_to_item: #""If the code the user entered (which we're calling food_code) is one of the valid short codes we have listed in our special code book (called code_to_item)"
        food_name = code_to_item[food_code] #"...then look up what that short code means in our code book and remember the full name of the food it represents (we'll call that the food_name)."
        cart.append(food_name) #"...take the full name of the food and put it into our shopping cart (which we're calling cart)."
        print(f"{food_name} added to cart.")
    elif menu.get(food) is not None:
        cart.append(food_code)
        print(f"{food_code} added to cart")
    else:
        print("Invalid item code.")

print("Cart:", cart)

print("----------TOTAL----------")
for food_name in cart:
    price = menu.get(food_name)
    if price is not None:  # Check if the price is not None
        total += price
        print(food_name, end=" ")
    else:
        print(f"Warning: Price not found for {food_name}")

print()
print(f"Total is: RM{total:.2f}")
