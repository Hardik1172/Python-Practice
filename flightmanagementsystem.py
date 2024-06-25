import datetime


def flightdetails (self):

    self.flight_number = int(input("flight number"))
    self.source = str(input("source of flight"))
    self.destination = str(input("destination of flight"))
    self.distance = int(input("enter the distance covered"))

def flightdate (self):
    self.year = int(input("enter the year"))
    self.month = int(input("enter the month"))
    self.date = int(input("enter the date"))
    self.date = datetime.date(self.year, self.month,self.date)

def flighttime (self):
    self.hour = int(input("enter the hour"))
    self.minute = int(input("enter the minute"))

def passengers(self):
    self.number = int(input("enter number of passenger"))
    for i in self.number:
        self.name = str(input("enter the name of passenger"))
        self.age = int(input("enter the age of passenger"))
        self.gender = str(input('enter the gender of passenger whether male,female'))
        while True:
            print("enter the food choices , 1 for veg and 2 for non veg")
            choice = int(input("enter the choice"))
            if choice == 1:
                print("VEG")
            elif choice == 2:
                print("non veg")
            else:
                print("invalid")

def main():
    while True:
