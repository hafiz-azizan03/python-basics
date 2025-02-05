#collection = single "variable" used to store multiple values
#  List = [begin:end:step] ordered and changeable. Duplicates OK
#  Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#  Tuples = () ordered and unchangeable. Duplicates OK. FASTER

# print(dir(collection)) to know all avaible attributes
# print(help(collection)) to know the description of each attribute

# fruits[0] = "pineapple" insert value at designated index
#fruits.append("pineapple") adds a value at the end of a collection
#fruits.remove("apple") removes a value
#fruits.insert(0, "pineapple") insert value at designated index
#fruits.sort() sorts the value alphabetically
#fruits.reverse() reverses the values
#fruits.clear() clears a value from a collection
#(fruits.index("apple")) inidciates the value at which set



# SHOPPING CART PROGRAM 

#no tuples bcs they're unchangeable and no set bcs they're unordered
foods=[]
prices=[]
total= 0

while True:
    food= input(" What would you like to add to your shopping cart?(press q to quit): ")
    if food.lower() == "q": #we use food.lower in case of accidental uppercase Q
        break
    else:
        price=float(input(f"How much does the item cost?:RM "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART-----")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is RM{total}")
