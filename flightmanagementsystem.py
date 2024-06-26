import random
import datetime
import string


class Flights:
    def __init__(self):

        flight_number = self.flight_number
        source = self.source
        destination = self.destination
        capacity = self.capacity

    @staticmethod

    def flight_details(finalbooking=[]):
        flight_number = int(input("flight number"))
        source = str(input("source of flight"))
        destination = str(input("destination of flight"))
        distance = int(input("enter the distance covered"))
        capacity = int(input("enter the capacity of flight"))
        finalbooking.append(flight_number,source, destination, distance, capacity)

    @staticmethod
    def flight_date(self):
        year = int(input("enter the year"))
        month = int(input("enter the month"))
        date = int(input("enter the date"))
        datetime.date(year, month, date)
        return datetime.date


class Passenger:

    def __init__(self):

        self.passenger_number = None
        name = self.name
        age = self.age
        passenger_number = self.passenger_number
        gender = self.gender
        seatingtype_choice = self.seatingtype_choice
        tripchoice = self.tripchoice



    @staticmethod
    def passengeradd(self):
        passenger_number = int(input("enter the number of passenger for whom you want the ticket"))
        if passenger_number < self.capacity:
            passenger_number.append()
            return True
        return False

    def generate(self):
        self.randomletter = random.randrange(string.ascii_uppercase)
        self.randomid = random.randrange(1,50)
        print(f"the passenger id is {self.randomletter}{self.randomid}")

    def passenger(self):
        for i in self.passenger_number:
            self.name = str(input("enter the name of passenger"))
            self.age = int(input("enter the age of passenger"))
            self.gender = str(input('enter the gender of passenger whether male,female'))

    def seatingchoice(self):
        print("enter the seating type choice  , eco for economic class , busi for business class")
        seatingtype_choice = str(input("enter the seating type choice"))
        while True:
            if seatingtype_choice == "eco":
                print("you have choose economic class")
            elif seatingtype_choice == "busi":
                (
                    print("you have choose business class"))
            else:
                print("invalid choice")

    print("enter the seat type you want for example w for window , m for middle and a for aisle side")
    seat = str(input("enter the seat you want"))
    while True:
        if seat == "w":
            print("you have selected window seat")
        elif seat == "m":
            print("you have selected middle seat")
        elif seat == "a":
            print("you have selected aile seat")
        else:
            print("invalid choice")

        def trip_choice(self):
            print("enter the flight type according to 'Single' for single way trip ,'Round' for round way trip ")
        tripchoice = str(input("enter trip choice"))
        while True:
            if tripchoice == "Single":
                print("its a single way trip")
            elif tripchoice == "Round":
                print("its a round trip")
            else:
                print("plz enter valid choices")

        def foodchoice(self):
            print("enter the food choices , 1 for veg and 2 for non veg")
            while True:
                food_choice = int(input("enter the choice"))
                if food_choice == 1:
                    print("VEG")
                elif food_choice == 2:
                    print("non veg")
                else:
                    print("invalid")
def main():


    print("this is menu driven program for flight management system")
    print("enter the choice for performing various operations in this program")
    print("enter 1 if you want top use the program")
    print("enter 2 if you want to use the program again")
    print("enter 3 if you want to exit the program")
    choice = int(input("enter the choice "))
    while True:
        if choice == 1:
            obj1 = Flights
        elif choice == 2:
            obj2 = Passenger
        else:
            print("you quit the program")






if __name__ == "__main__":
 main()