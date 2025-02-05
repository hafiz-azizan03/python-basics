#nested loop = a loop within another loop
#              outer loop:
#                   inner loop:

rows=int(input("Enter the # of rows: "))
collumns=int(input("Enter the # of collumns: "))
symbols=(input("Enter the # of symbols: "))

for x in range(rows):
    for y in range(collumns):
        print(symbols, end="")
    print()
