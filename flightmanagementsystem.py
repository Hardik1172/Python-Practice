import random
import datetime
import string
'''
    Flight Model
'''
class Flight:

    def __init__(self, flight_number, source, destination, capacity, distance_covered):
        self.distance_covered = distance_covered
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.passengers = []
        self.flight_type = None
        self.halt_choice = None

        self.flight_date = None
        self.seats = None


    @staticmethod
    def create_flight():
        source = input("Enter source of flight: ")
        destination = input("Enter destination of flight: ")
        airline_types = ["AIRINDIA", "INDIGO", "BRITISHAIRWAYS", "EMIRATES", "DeltaAirLines", "SouthWestAirLines"]
        chosen_airline = random.choice(airline_types)
        random_number = random.randrange(1, 100)
        flight_number = chosen_airline + str(random_number)
        print(f"The flight_number is {flight_number}")
        capacity = int(input("Enter the capacity of flight:"))

        new_flight = Flight(flight_number, source, destination, capacity, distance_covered= None )
        new_flight.seats = Seats(new_flight)
        return new_flight


    def choose_flight_type(self):


        while True:
            choice = input("Enter route type (halt for halting flights, direct for direct flights): ")
            if choice == 'halt':

                while True:
                    halt_choice = input("enter the location for halt like choose 1 for via dubai , 2 for via Malaysia , 3 for via Iraq")
                    if halt_choice == '1':
                        self.halt_choice = "via dubai"
                        distance = random.randrange(5000, 6000)
                        print(f"The distance between source and destination is {distance}")
                        distance_covered = distance
                        break


                    elif halt_choice == '2':
                        self.halt_choice = "via Malaysia"
                        distance = random.randrange(6000, 7500)
                        print(f"The distance between source and destination is {distance}")
                        distance_covered = distance
                        break


                    elif halt_choice == '3':
                        self.halt_choice = "via Iraq"
                        distance = random.randrange(7500, 10000)
                        print(f"The distance between source and destination is {distance}")
                        distance_covered = distance
                        break


                    else:
                        print("enter correct choice plz for halt location")
                break

            elif choice == 'direct':
                self.flight_type = "Direct"
                distance = random.randrange(10000, 11000)
                print(f"The distance between source and destination is {distance}")
                distance_covered = distance
                break
            else:
                print("Wrong choice. Try again.")




    def set_flight_date(self):
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        self.flight_date = datetime.date(year, month, day)


    def __str__(self):
        if self.flight_date:
            date_info = str(self.flight_date)
        else:
            date_info = 'Not set'

        return (f"Flight {self.flight_number}: {self.source} to {self.destination} {self.halt_choice}\n"
                f"Distance {self.distance_covered}\n"
                f"Capacity: {self.capacity} passengers\n"
                f"Date: {date_info}")



class Seats(Flight):
    def __init__(self, flight):
        self.flight = flight


    def assign_seat(self):
        seat_letters = list(string.ascii_uppercase)
        random_letter = random.choice(seat_letters)
        random_number = random.randint(0, self.flight.capacity)
        seat = random_letter + str(random_number)
        print(f"The assigned seat for the passenger is {seat}")
        return seat



class Passenger:
    def __init__(self,numberofpassenger, name, age, gender, passenger_id):
        self.calculate = None
        self.b = None
        self.object1 = None
        self.numberofpassenger = numberofpassenger
        self.name = name
        self.age = age
        self.gender = gender
        self.passenger_id = passenger_id
        self.seating_class = None
        self.seat_type = None
        self.trip_type = None
        self.food_choice = None




    def choose_seating_class(self):
        while True:
            choice = input("Enter seating class (eco for economy, busi for business): ")
            if choice == 'eco':
                self.seating_class = "Economy"
                break
            elif choice == 'busi':
                self.seating_class = "Business"
                break
            else:
                print("Wrong choice. Try again.")


    def choose_seat_type(self):
        while True:
            choice = input("Enter seat type (w for window, m for middle, a for aisle): ")
            if choice == 'w':
                self.seat_type = "Window"
                break
            elif choice == 'm':
                self.seat_type = "Middle"
                break
            elif choice == 'a':
                self.seat_type = "Aisle"
                break
            else:
                print("Wrong choice. Try again.")

    # Function to choose trip type
    def choose_trip_type(self):
        while True:
            choice = input("Enter trip type (Single for one-way, Round for round-trip): ").lower()
            if choice == 'single':
                self.trip_type = "One way"
                break
            elif choice == 'round':
                self.trip_type = "RoundWay Trip"
                break
            else:
                print("Wrong choice. Try again.")

    # Function to choose food
    def choose_food(self):
        while True:
            choice = input("Enter food choice (Veg for veg, Non-veg for non-veg): ")
            if choice == 'Veg':
                self.food_choice = "Vegetarian"
                break
            elif choice == 'Non-veg':
                self.food_choice = "Non-vegetarian"
                break
            else:
                print("Wrong choice. Try again.")


    def __str__(self):
        return (f"Passenger: {self.name}, Age: {self.age}, Gender: {self.gender}\n"
                f"ID: {self.passenger_id}, Trip: {self.trip_type}\n"
                f"Class: {self.seating_class}, Seat: {self.seat_type}, Meal: {self.food_choice}\n"
                f"Assigned Seat: {self.seat_alloted}")





def add_passenger(flight):
    if len(flight.passengers) < flight.capacity:
        numberofpassenger = int(input("Enter the number the passengers you want to enter"))
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        gender = input("Enter passenger gender: ")


        id = ['AB', 'TQ', 'NK', 'PR', 'AL', 'ZL', 'YU']
        chosen = random.choice(id)
        random_number = random.randrange(1, 100)
        passenger_id = chosen + str(random_number)
        print(f"The automatically generated passenger id is {passenger_id}")

        new_passenger = Passenger(numberofpassenger,name, age, gender, passenger_id)
        new_passenger.choose_seating_class()
        new_passenger.choose_seat_type()
        new_passenger.choose_trip_type()
        new_passenger.choose_food()



        new_passenger.seat_alloted = flight.seats.assign_seat()

        # Calling of Calculate function of Cost class



        flight.passengers.append(new_passenger)
        print(f"Passenger {new_passenger.name} added successfully.")
        return True
    else:
        print("Flight is full. Can't add more passengers.")
        return False


# Main program
def main():
    flights = []
    while True:
        print("\nFlight Management System")
        print("1. Create a new flight")
        print("2. Add a passenger to a flight")
        print("3. Display flight details")
        print("4. Display passenger details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_flight = Flight.create_flight()
            new_flight.choose_flight_type()
            new_flight.set_flight_date()
            flights.append(new_flight)
            print("Flight created successfully.")

        elif choice == '2':
            if not flights:
                print("No flights available. Please create a flight first.")
            else:
                for i, flight in enumerate(flights):
                    print(f"{i + 1}. {flight.flight_number}: {flight.source} to {flight.destination}")
                try:
                    flight_index = int(input("Choose a flight (enter number): ")) - 1
                    if 0 <= flight_index < len(flights):
                        add_passenger(flights[flight_index])
                    else:
                        print("Wrong flight number.")
                except ValueError:
                    print("Wrong input. Please enter a number.")

        elif choice == '3':
            if not flights:
                print("No flights available.")
            else:
                for flight in flights:
                    print(flight)
                    print(f"Passengers: {len(flight.passengers)}/{flight.capacity}")
                    print()

        elif choice == '4':
            if not flights:
                print("No flights available.")
            else:
                for flight in flights:
                    print(f"\nFlight {flight.flight_number} passengers:")
                    if not flight.passengers:
                        print("No passengers on this flight.")
                    else:
                        for passenger in flight.passengers:
                            print(passenger)
                            print()

        elif choice == '5':
            print("Thank you for using the Flight Management System.")
            break

        else:
            print("Wrong choice. Please try again.")



if __name__ == "__main__":
    main()