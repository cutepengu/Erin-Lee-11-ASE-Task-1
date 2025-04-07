import requests
from weather_module import *

def main():
    city =input("Enter city name: ")

    display_weather_info(fetch_weather(city))

main()

 