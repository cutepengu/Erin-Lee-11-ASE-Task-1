import requests

api_key = "a57d8a0f5879541e7269eed5af654bfc"

base_url = "https://weatherstack.com/"

def fetch_weather(city_name):
    """
    Fetches the current weather data for a given city using WeatherStack.
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
    if weather_data:
        # Extract relevant data from the API response
        location = weather_data["location"]["name"]  
        region = weather_data["location"]["region"]  
        country = weather_data["location"]["country"]  
        temperature = weather_data["current"]["temp_c"]  
        weather = weather_data["current"]["weather"]["text"]  
        wind = weather_data["current"]["wind"]["__km/h"]
        humidity = weather_data["current"]["humidity"]["__%"]

        print(f"Weather in {location}, {region}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather}")
        print(f"Wind: {wind}km/h")
        print(f"Humidity: {humidity}%")
    else:
        print("Error retrieving weather data.")

def main():
    display_weather_info(fetch_weather('Sydney'))

main()