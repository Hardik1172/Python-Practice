import datetime
class Flights:
    def __init__(self):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.number = number

    def flight_details (self):
        self.flight_number = int(input("flight number"))
        self.source = str(input("source of flight"))
        self.destination = str(input("destination of flight"))
        self.distance = int(input("enter the distance covered"))
        self.capacity = int(input("enter the capacity of flight"))

    @staticmethod
    def trip_choice():
        print("enter the flight type according to 'Single' for single way trip ,'Round' for round way trip ")
        trip_choice = str(input("enter trip choice"))
        while True:
            if trip_choice == "Single":
                print("its a single way trip")
            elif trip_choice == "Round":
                print("its a round trip")
            else:
                print("plz enter valid choices")
    @staticmethod
    def seat_choice():
        print("enter the seat choice type , eco for economic class , busi for business class")
    seat_choice = str(input("enter the seat choice"))
    while True:
        if seat_choice == "eco":
            print("you have choose economic class")
        elif seat_choice == "busi":
            print("you have choose business class")
        else:
            print("invalid choice")

    def flight_date (self):
        self.year = int(input("enter the year"))
        self.month = int(input("enter the month"))
        self.date = int(input("enter the date"))
        self.date = datetime.date(self.year, self.month,self.date)

    def passenger(self):
        self.number = int(input("enter number of passenger for you want to book"))
        if self.number < self.capacity:
            for i in self.number:
                self.name = str(input("enter the name of passenger"))
                self.age = int(input("enter the age of passenger"))
                self.gender = str(input('enter the gender of passenger whether male,female'))


    def food_choice(self):
        print("enter the food choices , 1 for veg and 2 for non veg")
        while True:
            food_choice = int(input("enter the choice"))
            if food_choice == 1:
                print("VEG")
            elif food_choice == 2:(
                    print("non veg"))
            else:
                print("invalid")
        else:
            print("entered passenger exceed the limit")

obj = Flights
def main():

    print("this is menu driven program for flight management system")
    print("enter the choice for performing various operations in this program")
    choice = int(input("enter the choice "))
    while True:
        if choice == 1:
            obj.flightdetails()
        elif choice == 2:



if __name__ == "__main__"
 main()