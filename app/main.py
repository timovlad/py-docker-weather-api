import requests
import os

def get_weather(city):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to get weather data")
        return None

def print_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("No weather data available")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    print_weather(weather_data)
