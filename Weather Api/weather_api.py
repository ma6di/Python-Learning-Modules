import requests


def print_weather_info(response, city):
	weather_data = response.json()
	
	# Extract current weather
	current = weather_data['current_condition'][0]
	location = weather_data['nearest_area'][0]
	
	# Extract location info
	city_name = location['areaName'][0]['value']
	country = location['country'][0]['value']
	
	# State/region might not exist for all locations
	try:
		region = location['region'][0]['value']
		if region and region != city_name:  # Only show if different from city
			location_string = f"{city_name}, {region}, {country}"
		else:
			location_string = f"{city_name}, {country}"
	except (KeyError, IndexError):
		location_string = f"{city_name}, {country}"
	
	temperature = current['temp_C']
	description = current['weatherDesc'][0]['value']
	humidity = current['humidity']
	wind_speed = current['windspeedKmph']
	
	# Display nicely with proper location format
	print(f"\nWeather in {location_string}:")
	print(f"Temperature: {temperature}°C")
	print(f"Description: {description}")
	print(f"Humidity: {humidity}%")
	print(f"Wind Speed: {wind_speed} km/h")

def print_error(response, city):
	print(f"Error: {response.status_code}")
	if response.status_code == 404:
		print(f"City '{city}' not found. Check spelling?")
	elif response.status_code == 500:
		print("Weather service temporarily unavailable")
	else:
		print("Something went wrong. Try again later.")

def main():
        # Instead of hardcoded "Berlin"
    city = input("Enter city name: ").strip()
    
    if not city:
        print("Please enter a valid city name")
        return
    
    # Using wttr.in - completely free, no API key needed
    url = f"https://wttr.in/{city}?format=j1"  # j1 = JSON format
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print_weather_info(response, city)
    else:
        print_error(response, city)

if __name__ == "__main__":
    main()