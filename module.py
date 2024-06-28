import random
import datetime
import string

class Flight:
    def __init__(self, flight_number, source, destination, capacity, distance):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.distance = distance
        self.passengers = []
        self.date = None

    @staticmethod
    def create_flight():
        flight_number = int(input("Enter flight number: "))
        source = input("Enter source of flight: ")
        destination = input("Enter destination of flight: ")
        distance = int(input("Enter the distance covered: "))
        capacity = int(input("Enter the capacity of flight: "))
        return Flight(flight_number, source, destination, capacity, distance)

    def set_flight_date(self):
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        self.date = datetime.date(year, month, day)

    def __str__(self):
        return (f"Flight {self.flight_number}: {self.source} to {self.destination}, "
                f"Distance: {self.distance} km, Capacity: {self.capacity}, "
                f"Date: {self.date}")

class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.passenger_id = self.generate_id()
        self.seat_type = None
        self.seat_class = None
        self.trip_type = None
        self.food_choice = None

    @staticmethod
    def generate_id():
        return f"{random.choice(string.ascii_uppercase)}{random.randint(1, 50)}"

    def choose_seat_type(self):
        while True:
            seat = input("Enter seat type (w for window, m for middle, a for aisle): ").lower()
            if seat in ['w', 'm', 'a']:
                self.seat_type = {'w': 'window', 'm': 'middle', 'a': 'aisle'}[seat]
                break
            print("Invalid choice. Please try again.")

    def choose_seat_class(self):
        while True:
            category = input("Enter seating class (eco for economy, busi for business): ").lower()
            if category in ['eco', 'busi']:
                self.seat_class = 'economy' if category == 'eco' else 'business'
                break
            print("Invalid choice. Please try again.")

    def choose_trip_type(self):
        while True:
            trip = input("Enter trip type (Single for one-way, Round for round trip): ").capitalize()
            if trip in ['Single', 'Round']:
                self.trip_type = trip
                break
            print("Invalid choice. Please try again.")

    def choose_food(self):
        while True:
            choice = input("Enter food choice (1 for veg, 2 for non-veg): ")
            if choice in ['1', '2']:
                self.food_choice = 'Vegetarian' if choice == '1' else 'Non-vegetarian'
                break
            print("Invalid choice. Please try again.")

    def __str__(self):
        return (f"Passenger {self.passenger_id}: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Seat: {self.seat_type} ({self.seat_class}), Trip: {self.trip_type}, "
                f"Food: {self.food_choice}")

class FlightManagementSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self):
        flight = Flight.create_flight()
        flight.set_flight_date()
        self.flights.append(flight)
        print(f"Flight added successfully: {flight}")

    def book_passenger(self):
        if not self.flights:
            print("No flights available. Please add a flight first.")
            return

        print("Available flights:")
        for i, flight in enumerate(self.flights):
            print(f"{i + 1}. {flight}")

        flight_index = int(input("Enter the number of the flight you want to book: ")) - 1
        if 0 <= flight_index < len(self.flights):
            flight = self.flights[flight_index]
            if len(flight.passengers) < flight.capacity:
                name = input("Enter passenger name: ")
                age = int(input("Enter passenger age: "))
                gender = input("Enter passenger gender: ")
                passenger = Passenger(name, age, gender)
                passenger.choose_seat_type()
                passenger.choose_seat_class()
                passenger.choose_trip_type()
                passenger.choose_food()
                flight.passengers.append(passenger)
                print(f"Booking successful: {passenger}")
            else:
                print("Sorry, this flight is full.")
        else:
            print("Invalid flight number.")

    def display_flight_details(self):
        for flight in self.flights:
            print(f"\n{flight}")
            print("Passengers:")
            for passenger in flight.passengers:
                print(passenger)

def main():
    system = FlightManagementSystem()

    while True:
        print("\nFlight Management System Menu:")
        print("1. Add a new flight")
        print("2. Book a passenger")
        print("3. Display flight details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            system.add_flight()
        elif choice == '2':
            system.book_passenger()
        elif choice == '3':
            system.display_flight_details()
        elif choice == '4':
            print("Thank you for using the Flight Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()