import random
import datetime



class Flights:
    def __init__(self, flight_number, source, destination, randomdistance, capacity):

        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.randomdistance = randomdistance
        self.capacity = capacity

    @staticmethod
    def flightid():
        import random
        list1 = ["AIRINDIA", "INDIGO", "BRITISHAIRWAYS", "EMIRATES"]
        flightid1 = random.choice(list1)
        randomid = random.randrange(1, 100)
        return f"the flightid  is {flightid1}{randomid}"

    @staticmethod

    def flight_details():
        source = input("source of flight")
        destination = input("destination of flight")
        randomdistance = random.randrange(5000, 7000)
        capacity = int(input("enter the capacity of flight"))
        return Flights(flight_number, source, destination,randomdistance ,capacity)


    @staticmethod
    def flight_date(self):
        year = int(input("enter the year"))
        month = int(input("enter the month"))
        date = int(input("enter the date"))
        datetime.date(year, month, date)
        return datetime.date
    def __str__(self):
        return f'The entered flight details are in such way flightnumber- {self.flight_number} , source - {self.source}, destination - {self.destination}, distance between origin and destination - {self.distance}, the capacity of flight is - {self.capacity}'


class Passenger:

    def __init__(self, passenger_number, name, age, gender,passenger_id ):


        self.name = name
        self.age = age
        self.passenger_number = passenger_number
        self.gender = gender
        self.passenger_id = passenger_id



    @staticmethod
    def passengeradd(self):
        passenger_number = int(input("enter the number of passenger for whom you want the ticket"))
        if passenger_number < self.capacity:
            passenger_number.append()
            return True
        return False

    def generate(self):
        self.string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.randomletter = random.choice(self.string)
        self.randomid = random.randrange(1, 50)
        return f"the passenger id is : {self.randomletter}{self.randomid}"

    def passenger(self):
        for i in self.passenger_number:
            self.name = input("enter the name of passenger")
            self.age = int(input("enter the age of passenger"))
            self.gender = input('enter the gender of passenger whether male,female')
            return Passenger(self.name, self.age, self.gender)

    def seatingchoice(self):
        print("enter the seating type choice  , eco for economic class , busi for business class")
        category = input("enter the seating type choice")
        while True:
            if category == "eco":
                print("you have choose economic class")
            elif category == "busi":

                    print("you have choose business class")
            else:
                print("invalid choice")

    print("enter the seat type you want for example w for window , m for middle and a for aisle side")
    seat = input("enter the seat you want")
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
        trip = input("enter trip choice")
        while True:
            if trip == "Single":
                print("its a single way trip")
            elif trip == "Round":
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
        def __str__(self):
            return f'the passenger name is - {self.name}, age is - {self.age}, gender is - {self.gender}, passenger id is {self.randomletter}{self.randomid}, their choice for trip type is {self.trip}, their choice for class of flight for journey is {self.category}, their choice for seat choice is {self.seat}, their choice for food is {self.food_choice}   '


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
            obj1.__str__()
        elif choice == 2:
            obj2 = Passenger
            obj2.__str__()
        else:
            print("you quit the program")

if __name__ == "__main__":
 main()