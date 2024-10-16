import random
import requests
from datetime import datetime

# Function to simulate getting temperature from a wearable device
def get_temperature():
    # Simulate a temperature reading between 35.0 and 40.0 degrees Celsius
    return round(random.uniform(35.0, 40.0), 2)

# Function to get COVID-19 data from a public API
def get_covid_data():
    # Example API endpoint (replace with a valid one)
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        global_data = data['Global']
        return global_data['TotalConfirmed'], global_data['TotalDeaths']
    else:
        return None, None

# Main function to track health data and COVID-19 data
def track_covid():
    print("Starting COVID-19 Tracking...\n")
    
    while True:
        # Get temperature reading
        temperature = get_temperature()
        print(f"Temperature: {temperature} °C")
        
        # Get COVID-19 data
        confirmed, deaths = get_covid_data()
        if confirmed is not None:
            print(f"COVID-19 Total Confirmed Cases: {confirmed}
