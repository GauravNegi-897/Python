import requests

longitude = 2.35
latitude = 48.85

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"


response = requests.get(url)

data = response.json()

print(type(data))

print(data['current']['temperature_2m'])