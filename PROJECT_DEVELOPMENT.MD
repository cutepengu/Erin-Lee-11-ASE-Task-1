# 11 ASE Task 1 2025- Fundamentals of programming
#### By Erin Lee

# Reqirements Definition

### Functional Requirements
* Provide users with accurate weather condition, temperature, wind, and humidity
* Application should detect a problem if user makes a mistake and should suggest a correction
* Application should be able to do simple stuff such as accepting all capital and lower case letters

### Non-Functional Requirements
* Allow clear visualisation of the application
* Display the output clear and fast for enhanced convenience in users
* Make it easier for users to use by making inputs easier to understand

# Determining Specfications
### Functional Specifications
* Successfully take the input of users' (location), and provide them with the data collected near the area
* Make sure the application provides users with accurate data with the right format for display
* If user makes a mistake like getting mixed up with lower and uppercase letters etc. accept the error and provide users with the data they require
* If user makes a spelling mistake etc. alert them that there is an error in the users' input and offer a suggestion such as checking for a spelling mistake

### Non-Functional Specifications
* Provide users with a clearly visible output with the consideration of fonts, formatting, and sizes
* Use clear fonts in order to allow users to easily type in their input


# Design
## Data Dictionary
![Data Dictionary](/images/datadictionary.png "Data Dictionary")
## Structure Chart
![Structure Chart](/images/structurechart.png "Structure Chart")
## Flowchart
![FlowChart](/images/flowchart.png "Flowchart")
## Pseudocode
![Pseudocode](/images/pseudocode.png "Pseudocode")
## Gantt Chart
![Gantt Chart](/images/ganttchart.png "Gantt Chart")
# Development
import requests

api_key = "413330cdc1d441ff8ca222024251803"

base_url = "http://api.weatherapi.com/v1"

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
    if weather_data:
        location = weather_data["location"]["name"]  
        region = weather_data["location"]["region"]  
        country = weather_data["location"]["country"]  
        temperature = weather_data["current"]["temp_c"]  
        condition = weather_data["current"]["condition"]["text"]
        humidity = weather_data["current"]["humidity"]
        wind = weather_data["current"]["wind_kph"]
    
    data = input("Enter data you require from either temperature, condition, wind, or humidity: ")
     print(f"Weather in {location}, {region}, {country}:")
    if data == condition:
     print(f"Condition: {condition}")
    elif data == temperature:
     print(f"Temperature: {temperature}°C")
    elif data == wind:
     print(f"Wind: {wind}km/h")
    elif data == humidity:
     print(f"Humidity: {humidity}%")
    else:
     print("Error retrieving weather data. Please check if you made a spelling mistake in your input.")

def main():
    city =input("Enter city name: ")

    display_weather_info(fetch_weather(city))

main()
# Integration
in the code file main.py
# Testing and Debugging
#### This is the Testing and Debugging steps I took to successfully create my project.
https://github.com/cutepengu/Erin-Lee-11-ASE-Task-1
### Peer Feedback (Maksim):
This program runs very efficiently and provides the user with satisfactory results considering what they are trying to search up. The program is very easy to understand and can be very informative if you need the weather in a certain city. To improve, the results could be displayed better to give the user a better experience.

### Peer Feedback (Ario):
It displayed the necessary information for users to visualise with a quick response and was able to correct errors and provide a suggestion for users. However I could not enter another city after the program displayed data for a city I previously wanted which made me have to rerun the program. For an area of improvement, I would suggest working on allowing users to ask for 2 or more cities without having to run it again.

# Installation
## READ ME:
![Installation](/images/readme.png "README")

## Requirements:
![Installation](/images/requirements.png "README")
# Maintenance
## Maintenance Questions:
### 1. Explain how you would handle issues caused by changes to the weather API over time.
If the weather API I am currently using creates a change, I will first see if they have eliminated the functions that I have already defined such as temperature, condition etc. If they have, I will have to see if there are any other options to choose from such as converting my previous temperature from being formatted as celsius such as "28°" to being formatted in a wordly format such as "twenty-eight degrees celsius". Though this can be frustrating for users as it is of less convienence, this will reduce the risk of having to construct a code from a different API. If all the functions have been taken down, I will unfortunately have no other choice than to take the program down as my program heavily relies on the functions the API provides. 

### 2. Explain how you would ensure the program remains compatible with new versions of Python and libraries like requests and matplotlib.
My program does not require matplotlib so any forms of those won't be an issue. However I do need requests as I have to import requests for my main.py so to eliminate the risks of being outdated to the new Python and library versions, I will update the program frequently. If Python and/or library has already created a new version/s, simply updating Python will fix the error.

### 3. Describe the steps you would take to fix a bug found in the program after deployment.
After a deployment in the system, I will first have to look at my code to see if anything is missing. If nothing is missing, I will check the weather API i used as there could potentially be an unknown issue such as a change in the API. If no errors are found, I will have to check if an update is required for Python as newer versions of Python and/or library could have been made. By checking these elements, I will be able to fix a bug or an error. 

### 4. Outline how you would maintain clear documentation and ensure the program remains easy to update in the future.
To be able to make it easier for the system to update, all the coding will be done under one file to minimise complexity. I will also do regular check-ups and updates as well as using automated tools for maintenance. A collaborative editing process could also help as getting feedback from others can provide more effective solutions as well as other ideas for an easier update in the future. 


## Final Evaluation:
### 1. Evaluate the current functionality of the program in terms of how well it addresses the functional and non-functional requirements.
I believe that my program in terms of the functional and non-functional requirements guideline I made at the start of this assessment task was successful as I was able to cover most guideline without a mistake or error. Although I could not change the font for a clearer visualisation, the default font is already clear. As I was able to cover all my functional requirements like the functions for my program e.g. temperature, condition, humidity, and wind. Overall, the program does everything I wanted it to do so I am very satisfied and I think my program is good at addressing the functional and non-functional requirements. 

### 2. Discuss areas for improvement or new features that could be added.
I previously thought that providing users with data in a worded format was the best but after creating my program, I think my program could be better if I could include an optional graph/s. This is because it can be easier for some users to receive both worded and graphical data of weather at a certain location. For an area of improvement, I believe that I could allow users to request which function they require as my program when a user inputs their location provides them with all the functions in the system which could be more harder to visualise as there are a lot of things. To be able to make it easier for users to visualise, I think by allowing them to input what they only need e.g. just temperature as all the other data will be unnecessary to them.

### 3. Evaluate how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.
All throughout the development of my project, I believe that I did well at updating the project on Github each time I worked on it as I could go back to my summary and see what I worked up to. The coding part made it especially useful as I faced hardships in the coding part of the project and I have always mentioned an error so it was way faster for me to get a recap of what I was struggling with the last lesson or the last time I worked on for the project. I constantly updated my gantt chart and this was able to help me from having to rush certain things as I could plan the whole project as I went. 


