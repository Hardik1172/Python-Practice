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
                flight_index = int(input("Choose a flight (enter number): ")) - 1
                if 0 <= flight_index < len(flights):
                    add_passenger(flights[flight_index])
                else:
                    print("Invalid flight number.")

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