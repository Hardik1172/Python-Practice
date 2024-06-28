import random


class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []
        self.seats = {f"{row}{col}": None for row in "ABCDEF" for col in range(1, 31)}
        self.food_options = ["Vegetarian", "Non-vegetarian", "Vegan", "Kosher", "Halal"]

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def assign_seat(self, passenger, seat):
        if seat in self.seats and self.seats[seat] is None:
            self.seats[seat] = passenger
            passenger.assign_seat(seat)
            return True
        return False


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number
        self.seat = None
        self.food_choice = None

    def assign_seat(self, seat):
        self.seat = seat

    def choose_food(self, food):
        self.food_choice = food


class FlightManager:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def book_passenger(self, flight_number, passenger):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            if flight.add_passenger(passenger):
                return True
        return False

    def assign_seat(self, flight_number, passenger, seat):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            return flight.assign_seat(passenger, seat)
        return False

    def choose_food(self, flight_number, passenger, food):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            if food in flight.food_options:
                passenger.choose_food(food)
                return True
        return False


def main_menu():
    manager = FlightManager()

    # Add some sample flights
    manager.add_flight(Flight("FL001", "New York", "London", 180))
    manager.add_flight(Flight("FL002", "Paris", "Tokyo", 200))

    while True:
        print("\n--- Flight Management System ---")
        print("1. Book a flight")
        print("2. Choose a seat")
        print("3. Select food option")
        print("4. View flight details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter flight number: ")
            name = input("Enter passenger name: ")
            passport = input("Enter passport number: ")
            passenger = Passenger(name, passport)
            if manager.book_passenger(flight_number, passenger):
                print("Booking successful!")
            else:
                print("Booking failed. Flight might be full or not exist.")

        elif choice == '2':
            flight_number = input("Enter flight number: ")
            name = input("Enter passenger name: ")
            seat = input("Enter desired seat (e.g., A1, B2): ")
            passenger = next((p for p in manager.flights[flight_number].passengers if p.name == name), None)
            if passenger and manager.assign_seat(flight_number, passenger, seat):
                print(f"Seat {seat} assigned successfully!")
            else:
                print("Seat assignment failed. Seat might be taken or invalid.")

        elif choice == '3':
            flight_number = input("Enter flight number: ")
            name = input("Enter passenger name: ")
            print("Food options:", manager.flights[flight_number].food_options)
            food = input("Enter food choice: ")
            passenger = next((p for p in manager.flights[flight_number].passengers if p.name == name), None)
            if passenger and manager.choose_food(flight_number, passenger, food):
                print("Food choice recorded successfully!")
            else:
                print("Food selection failed. Invalid option or passenger not found.")

        elif choice == '4':
            flight_number = input("Enter flight number: ")
            if flight_number in manager.flights:
                flight = manager.flights[flight_number]
                print(f"\nFlight {flight_number}: {flight.origin} to {flight.destination}")
                print(f"Passengers: {len(flight.passengers)}/{flight.capacity}")
                for passenger in flight.passengers:
                    print(f"- {passenger.name}: Seat {passenger.seat}, Food: {passenger.food_choice}")
            else:
                print("Flight not found.")

        elif choice == '5':
            print("Thank you for using the Flight Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()