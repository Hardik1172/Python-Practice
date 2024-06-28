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
        self.flight_date = None

    @staticmethod
    def create_flight():
        flight_number = int(input("Enter flight number: "))
        source = input("Enter source of flight: ")
        destination = input("Enter destination of flight: ")
        distance = int(input("Enter the distance covered: "))
        capacity = int(input("Enter the capacity of flight: "))
        return Flight(flight_number, source, destination, distance, capacity)

    def set_flight_date(self):
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        self.flight_date = datetime.date(year, month, day)

    def __str__(self):
        return (f"Flight {self.flight_number}: {self.source} to {self.destination}\n"
                f"Distance: {self.distance} km, Capacity: {self.capacity} passengers\n"
                f"Date: {self.flight_date if self.flight_date else 'Not set'}")


class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.passenger_id = self.generate_id()
        self.seating_class = None
        self.seat_type = None
        self.trip_type = None
        self.food_choice = None

    @staticmethod
    def generate_id():
        return f"{random.choice(string.ascii_uppercase)}{random.randint(1, 50)}"

    def choose_seating_class(self):
        while True:
            choice = input("Enter seating class (eco for economy, busi for business): ").lower()
            if choice in ['eco', 'busi']:
                self.seating_class = "Economy" if choice == 'eco' else "Business"
                break
            print("Invalid choice. Please try again.")

    def choose_seat_type(self):
        while True:
            choice = input("Enter seat type (w for window, m for middle, a for aisle): ").lower()
            if choice in ['w', 'm', 'a']:
                self.seat_type = {"w": "Window", "m": "Middle", "a": "Aisle"}[choice]
                break
            print("Invalid choice. Please try again.")

    def choose_trip_type(self):
        while True:
            choice = input("Enter trip type (Single for one-way, Round for round-trip): ").lower()
            if choice in ['single', 'round']:
                self.trip_type = "One-way" if choice == 'single' else "Round-trip"
                break
            print("Invalid choice. Please try again.")

    def choose_food(self):
        while True:
            choice = input("Enter food choice (1 for veg, 2 for non-veg): ")
            if choice in ['1', '2']:
                self.food_choice = "Vegetarian" if choice == '1' else "Non-vegetarian"
                break
            print("Invalid choice. Please try again.")

    def __str__(self):
        return (f"Passenger: {self.name}, Age: {self.age}, Gender: {self.gender}\n"
                f"ID: {self.passenger_id}, Trip: {self.trip_type}\n"
                f"Class: {self.seating_class}, Seat: {self.seat_type}, Meal: {self.food_choice}")


def add_passenger(flight):
    if len(flight.passengers) < flight.capacity:
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        gender = input("Enter passenger gender: ")
        passenger = Passenger(name, age, gender)
        passenger.choose_seating_class()
        passenger.choose_seat_type()
        passenger.choose_trip_type()
        passenger.choose_food()
        flight.passengers.append(passenger)
        print(f"Passenger {passenger.name} added successfully.")
        return True
    else:
        print("Flight is at full capacity. Cannot add more passengers.")
        return False


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
            flight = Flight.create_flight()
            flight.set_flight_date()
            flights.append(flight)
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
                        print("Invalid flight number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

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
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()