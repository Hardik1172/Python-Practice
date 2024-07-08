import datetime
import json
def load_flights():
    with open('flights_data.json', 'r') as file:
        data = json.load(file)
    return data['flights_data']

def calculate_duration(departure, arrival)
departure =datetime.strptime(departure, "%Y-%m-%d %H:%M" )
arrival = datetime.strptime(arrival, "%Y-%m-%d %H:%M")
duration = arrival - departure
print(duration)


