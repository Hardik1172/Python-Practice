class Cost(Passenger):
    def __init__(self, final_cost):
        self.final_cost = final_cost

    def calculate(self):

        if Passenger.choose_food(self) == "Vegetarian" and Passenger.choose_trip_type(self) == "One Way" and Passenger.choose_seating_class(self) == "Economy":
           self.costing = (self.numberofpassenger * 1000) + 300 + 500 + 250
           print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self) == "Vegetarian" and Passenger.choose_trip_type(self) == "One Way" and Passenger.choose_seating_class(self) == "Business":
             self.costing = (self.numberofpassenger * 1000) + 300 + 500 + 500
             print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self) == "Vegetarian" and Passenger.choose_trip_type(self) == "Round" and Passenger.choose_seating_class(self) == "Economy":
            self.costing = (self.numberofpassenger * 1000) + 300 + 1000 + 250
            print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self) == "Vegetarian" and Passenger.choose_trip_type(self) == "Round" and Passenger.choose_seating_class(self) == "Business":
            self.costing = (self.numberofpassenger * 1000) + 300 + 1000 + 500
            print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self) == "Non-Veg" and Passenger.choose_trip_type(self) == "One Way" and Passenger.choose_seating_class(self) == "Economy":
            self.costing = (self.numberofpassenger * 1000) + 500 + 500 + 250
            print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self) == "Non-Veg" and Passenger.choose_trip_type(self) == "One Way" and Passenger.choose_seating_class(self) == "Business":
            self.costing = (self.numberofpassenger * 1000) + 500 + 500 + 500
            print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self) == "Non-Veg" and Passenger.choose_trip_type(self) == "Round" and Passenger.choose_seating_class(self) == "Economy":
            self.costing = (self.numberofpassenger * 1000) + 500 + 1000 + 250
            print(f" the final ticket price is {self.costing}")
        elif Passenger.choose_food(self)== "Non-Veg" and Passenger.choose_trip_type(self) == "Round" and Passenger.choose_seating_class(self) == "Business":
            self.costing = (self.numberofpassenger * 1000) + 500 + 1000 + 500
            print(f" the final ticket price is {self.costing}")
        else:
            print("enter valid choices")

