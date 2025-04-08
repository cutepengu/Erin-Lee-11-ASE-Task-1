import requests

api_key = "413330cdc1d441ff8ca222024251803" # My API key

base_url = "http://api.weatherapi.com/v1" # API site I extracted my data from

def fetch_weather(city_name):
    """
    Fetches the current weather data for a given city using WeatherAPI.
    """
    complete_url = f"{base_url}/current.json?key={api_key}&q={city_name}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def display_weather_info(weather_data):
    """
    Displays weather information from the API response.
    """
    if weather_data: # Below are the options users can choose from
        location = weather_data["location"]["name"]  
        region = weather_data["location"]["region"]  
        country = weather_data["location"]["country"]  
        temperature = weather_data["current"]["temp_c"]  
        condition = weather_data["current"]["condition"]["text"]
        humidity = weather_data["current"]["humidity"]
        wind = weather_data["current"]["wind_kph"]
    
        # The code below allows users to enter a number instead of having to type up what they want to see
        option = input("Enter the number for the data required shown below: \n"
                       "1 - Condition\n"
                       "2 - Temperature\n"
                       "3 - Humidity\n"
                       "4 - Wind\n")
        
        if option == '1':
            print(f"Weather in {location}, {region}, {country}:")
            print(f"Condition: {condition}")

        elif option == '2':
            print(f"Weather in {location}, {region}, {country}:")
            print(f"Temperature: {temperature}°C")
        elif option == '3':
            print(f"Weather in {location}, {region}, {country}:")
            print(f"Humidity: {humidity}%")
        elif option == '4':
            print(f"Weather in {location}, {region}, {country}:")
            print(f"Wind: {wind}km/h")
    
    else: # The print statement below allows users to observe that they made an error in their input
        print("Error retrieving weather data. Please check if you made a spelling mistake in your input for location.")

def main():
    city =input("Enter city name: ")

    display_weather_info(fetch_weather(city))

main()

