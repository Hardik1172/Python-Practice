import json
import random
import datetime
import string

class Flight:
    def __init__(self, flight_number, source, destination, capacity, distance_covered, flight_type, flight_date, halt_choice=None):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.distance_covered = distance_covered
        self.flight_type = flight_type
        self.halt_choice = halt_choice
        self.flight_date = datetime.datetime.strptime(flight_date, "%Y-%m-%d").date()
        self.flight_time = datetime.datetime.strptime(flight_time, "%H:%M-%S").date()
        self.passengers = []
        self.seats = Seats(self)

    @classmethod
    def from_json(cls, data):
        return cls(
            flight_number=data['flight_number'],
            source=data['source'],
            destination=data['destination'],
            capacity=data['capacity'],
            distance_covered=data['distance_covered'],
            flight_type=data['flight_type'],
            flight_date=data['flight_date'],
            halt_choice=data.get('halt_choice')
        )

    def __str__(self):
        halt_info = f" {self.halt_choice}" if self.halt_choice else ""
        return (f"Flight {self.flight_number}: {self.source} to {self.destination}{halt_info}\n"
                f"Distance: {self.distance_covered} km\n"
                f"Capacity: {self.capacity} passengers\n"
                f"Date: {self.flight_date}\n"
                f"Type: {self.flight_type}")

def load_flights_from_json(filename="flights_data.json"):
    with open(filename, 'r') as f:
        data = json.load(f)
    return [Flight.from_json(flight_data) for flight_data in data['flights']]

# The rest of your classes (Seats, Passenger) remain the same

def add_passenger(flight):
# This function remains mostly the same, just remove the part where it asks for flight details

def main():
    flights = load_flights_from_json()
    while True:
        print("\nFlight Management System")
        print("1. Display available flights")
        print("2. Add a passenger to a flight")
        print("3. Display flight details")
        print("4. Display passenger details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for i, flight in enumerate(flights):
                print(f"{i + 1}. {flight.flight_number}: {flight.source} to {flight.destination} on {flight.flight_date}")

        elif choice == '2':
            if not flights:
                print("No flights available.")
            else:
                for i, flight in enumerate(flights):
                    print(f"{i + 1}. {flight.flight_number}: {flight.source} to {flight.destination} on {flight.flight_date}")
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