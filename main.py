import requests # Imported the code in weather_module.py
from weather_module import *

def main():
    city =input("Enter city name: ")

    display_weather_info(fetch_weather(city))

main()

 