import random
import string
capacity = int(input("enter the amoutn of passengers you want to enter"))
seats_row = list(string.ascii_uppercase)
randomrow = random.choice(seats_row)
seats_number = random.randint(0 , capacity)
allotedseats = str(randomrow) + str(seats_number)
print(f" the alotted seat for the passenger is {allotedseats}")


