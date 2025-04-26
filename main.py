import requests

api_key = "7b02c95094fdcae3e6d7635235371510"
user_input = input("Enter the city name: ").lower()
weather_api = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric").json()

weatherData = {
    "City": weather_api["name"],
    "Temperature": weather_api["main"]["temp"],
    "Feels Like": weather_api["main"]["feels_like"],
    "Humidity": weather_api["main"]["humidity"],
    "Pressure": weather_api["main"]["pressure"],
    "Wind Speed": weather_api["wind"]["speed"],
    "Wind Direction": weather_api["wind"]["deg"],
    "Weather": weather_api["weather"][0]["description"],
}

for key, value in weatherData.items():
    print(f"{key}: {value}")
