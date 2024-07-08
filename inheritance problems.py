import json
import random
from datetime import datetime


def print_boxed(message, width=70):
    print("*" * width)
    print(f"*{message.center(width - 2)}*")
    print("*" * width)


def print_separator(width=70):
    print("*" * width)


def load_flights():
    with open('flights.json', 'r') as file:
        data = json.load(file)
    return data['flights']


def get_available_routes(flights):
    routes = set()
    for flight in flights:
        routes.add((flight['origin'], flight['destination']))
    return routes


def display_available_routes(routes):
    print("\nAvailable routes:")
    for origin, destination in routes:
        print(f" {origin} to {destination}")


def search_flights(flights, origin, destination):
    return [flight for flight in flights if
            flight['origin'].lower() == origin.lower() and flight['destination'].lower() == destination.lower()]


def calculate_duration(departure, arrival):
    dep = datetime.strptime(departure, "%Y-%m-%d %H:%M")
    arr = datetime.strptime(arrival, "%Y-%m-%d %H:%M")
    duration = arr - dep
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{duration.days * 24 + hours}h {minutes}m"


def display_flights(flights):
    if not flights:
        print("No flights found for the given route.")
        return False

    print("\nAvailable Flights:")
    print(
        f"{'ID':<6} {'From':<12} {'To':<12} {'Departure':<16} {'Arrival':<16} {'Duration':<10} {'Type':<15} {'Distance (km)':<15} {'Price':<8}")
    print("-" * 110)
    for flight in flights:
        duration = calculate_duration(flight['departure'], flight['arrival'])
        print(
            f"{flight['id']:<6} {flight['origin']:<12} {flight['destination']:<12} {flight['departure']:<16} {flight['arrival']:<16} {duration:<10} {flight['type']:<15} {flight['distance']:<15} ${flight['price']:<8}")
    return True


def get_passenger_details():
    name = input("Enter passenger name: ")
    gender = input("Enter gender (M/F/Other): ")
    age = int(input("Enter age: "))
    seat_choice = input("Enter seat preference (Window/Aisle/Middle): ")
    trip_type = input("Enter trip type (Round/Single): ")
    food_preference = input("Enter food preference (Vegetarian/Non-vegetarian/Vegan): ")
    insurance = input("Do you want travel insurance? (Yes/No): ").lower() == 'yes'

    return {
        "name": name,
        "gender": gender,
        "age": age,
        "seat_choice": seat_choice,
        "trip_type": trip_type,
        "food_preference": food_preference,
        "insurance": insurance
    }


def assign_seat(seat_choice):
    row = random.randint(1, 30)
    if seat_choice.lower() == 'window':
        column = random.choice(['A', 'F'])
    elif seat_choice.lower() == 'aisle':
        column = random.choice(['C', 'D'])
    else:  # Middle
        column = random.choice(['B', 'E'])
    return f"{row}{column}"


def calculate_total_cost(base_price, passenger):
    total_cost = base_price
    if passenger['trip_type'].lower() == 'round':
        total_cost *= 2
    if passenger['insurance']:
        total_cost += 50
    return total_cost


def main():
    print_boxed("WELCOME TO FLIGHT MANAGEMENT SYSTEM")

    flights = load_flights()
    available_routes = get_available_routes(flights)

    display_available_routes(available_routes)

    while True:
        print_separator()
        origin = input("\nEnter origin city: ")
        destination = input("Enter destination city: ")

        if (origin, destination) in available_routes:
            break
        else:
            print("Sorry, we don't have flights for this route. Please choose from the available routes.")

    matching_flights = search_flights(flights, origin, destination)

    print_separator()
    if display_flights(matching_flights):
        book_flight = input("\nDo you want to book a flight? (Yes/No): ").lower()

        if book_flight == 'yes':
            print_separator()
            flight_id = input("Enter the Flight ID you want to book: ")
            selected_flight = next((flight for flight in matching_flights if flight['id'] == flight_id), None)

            if selected_flight:
                print_separator()
                passenger = get_passenger_details()
                seat_number = assign_seat(passenger['seat_choice'])
                total_cost = calculate_total_cost(selected_flight['price'], passenger)

                print_separator()
                print("\nBooking Summary:")
                print(
                    f"Flight: {selected_flight['id']} - {selected_flight['origin']} to {selected_flight['destination']}")
                print(f"Type: {selected_flight['type']}")
                print(f"Departure: {selected_flight['departure']}")
                print(f"Arrival: {selected_flight['arrival']}")
                print(f"Duration: {calculate_duration(selected_flight['departure'], selected_flight['arrival'])}")
                print(f"Distance: {selected_flight['distance']} km")
                print(f"Passenger: {passenger['name']}")
                print(f"Seat: {passenger['seat_choice']} (Seat Number: {seat_number})")
                print(f"Trip Type: {passenger['trip_type']}")
                print(f"Food Preference: {passenger['food_preference']}")
                print(f"Insurance: {'Yes' if passenger['insurance'] else 'No'}")
                print(f"Total Cost: ${total_cost}")

                print_separator()
                confirm = input("\nConfirm booking? (Yes/No): ").lower()
                if confirm == 'yes':
                    booking_id = f"BK{random.randint(1000, 9999)}"
                    print(f"\nBooking confirmed! Your booking ID is {booking_id}")
                    print(f"Your seat number is: {seat_number}")
                    print("Passenger added successfully.")
                else:
                    print("Booking cancelled.")
            else:
                print("Invalid Flight ID. Booking cancelled.")
        else:
            print("Thank you for using our flight management system.")
    else:
        print("No flights available for the given route. Please try a different search.")

    print_separator()
    print_boxed("THANK YOU FOR USING FLIGHT MANAGEMENT SYSTEM")


if __name__ == "__main__":
    main()