import time

my_time=int(input("Enter your time in seconds: "))

# we put -1 in the "step" so that the number would go in reverse order and counts down from my_time to 0
for x in range(my_time,0,-1):
    seconds= x % 60 # By using x % 60, you effectively extract the remaining seconds after accounting for whole minutes. This allows you to display the countdown in a standard format of "minutes:seconds".
    minutes= int(x /60) % 60
    hours= int(x/3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # prints the time 00:00:00 format
    time.sleep(1) # Pauses for 1 seconds


print("TIME'S UP LIL BRO")
       


