import requests

# Define the API endpoint and parameters
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Austin,US",
    "appid": "f758054e55f630d1f9bab0ac38cc45e6"  # Replace with your actual API key
}

# Make the request
response = requests.get(url, params=params)
data = response.json()

#print(data)

# Extract relevant data
city_name = data['name']
temperature = data['main']['temp']
weather_description = data['weather'][0]['description']
wind_speed = data['wind']['speed']

# Display the data
print(f"City: {city_name}")
print(f"Temperature: {temperature}°C")
print(f"Weather: {weather_description}")
print(f"Wind Speed: {wind_speed} m/s")
