# Import needed modules
import random
import datetime
import string


class Flight:
    def __init__(self, flight_number, source, destination, distance, capacity):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.distance = distance
        self.capacity = capacity
        self.passengers = []
        self.flight_type = None
        self.flight_date = None
        self.Seats = None


    def create_flight(self):
        source = input("Enter source of flight: ")
        destination = input("Enter destination of flight: ")

        # Make a random flight number
        airline_types = ["AIRINDIA", "INDIGO", "BRITISHAIRWAYS", "EMIRATES", "DeltaAirLines", "SouthWestAirLines"]
        chosen_airline = random.choice(airline_types)
        random_number = random.randrange(1, 100)
        flight_number = chosen_airline + str(random_number)
        print(f"The flight_number is {flight_number}")

        # Make a random distance
        distance = random.randrange(5000, 7000)
        print(f"The distance between two countries is {distance}")

        capacity = int(input("Enter the capacity of flight: "))

        return Flight(flight_number, source, destination, distance, capacity)

    # Function to choose flight type
    def choose_flight_type(self):
        while True:
            choice = input("Enter route type (halt for halting flights, direct for direct flights): ")
            if choice == 'halt':
                self.flight_type = "Halt"
                break
            elif choice == 'direct':
                self.flight_type = "Direct"
                break
            else:
                print("Wrong choice. Try again.")

    # Function to set flight date
    def set_flight_date(self):
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        self.flight_date = datetime.date(year, month, day)

    # Function to assign seats
    def Seats(self):
        capacity = int(input("Enter the capacity of flight you earlier entered: "))
        seat_letters = list(string.ascii_uppercase)
        random_letter = random.choice(seat_letters)
        random_number = random.randint(0, capacity)
        seat = random_letter + str(random_number)
        print(f"The assigned seat for the passenger is {seat}")
        return seat

    # Function to print flight info
    def __str__(self):
        if self.flight_date:
            date_info = str(self.flight_date)
        else:
            date_info = 'Not set'

        return (f"Flight {self.flight_number}: {self.source} to {self.destination}\n"
                f"Distance: {self.distance} km, Capacity: {self.capacity} passengers\n"
                f"Date: {date_info}")


# Make a Passenger class
class Passenger:
    def __init__(self, name, age, gender, passenger_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.passenger_id = passenger_id
        self.seating_class = None
        self.seat_type = None
        self.trip_type = None
        self.food_choice = None
        self.seat_alloted = None

    # Function to choose seating class
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

    # Function to choose seat type
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

    # Function to print passenger info
    def __str__(self):
        return (f"Passenger: {self.name}, Age: {self.age}, Gender: {self.gender}\n"
                f"ID: {self.passenger_id}, Trip: {self.trip_type}\n"
                f"Class: {self.seating_class}, Seat: {self.seat_type}, Meal: {self.food_choice}")


# Function to add a passenger to a flight
def add_passenger(flight):
    if len(flight.passengers) < flight.capacity:
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        gender = input("Enter passenger gender: ")

        # Make a random passenger ID
        id_prefixes = ['AB', 'TQ', 'NK', 'PR', 'AL', 'ZL', 'YU']
        chosen_prefix = random.choice(id_prefixes)
        random_number = random.randrange(1, 100)
        passenger_id = chosen_prefix + str(random_number)
        print(f"The automatically generated passenger id is {passenger_id}")

        new_passenger = Passenger(name, age, gender, passenger_id)
        new_passenger.choose_seating_class()
        new_passenger.choose_seat_type()
        new_passenger.choose_trip_type()
        new_passenger.choose_food()

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
            new_flight.Seats()
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


# Run the main program
if __name__ == "__main__":
    main()