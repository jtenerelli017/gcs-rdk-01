# Online resources used:
# - OpenWeatherMap One Call API 3.0     https://openweathermap.org/api/one-call-3
# - OpenWeatherMap Geocoding API        https://openweathermap.org/api/geocoding-api
# - Python Tutorial                     https://www.w3schools.com/python/default.asp
# - Python 3 HTTP protocol client       https://docs.python.org/3/library/http.client.html

# This is for parsing the HTTPS response bodies
import json

# This built-in Python 3 library will be used to send HTTPS requests
import http.client
site = "api.openweathermap.org"
cnct = http.client.HTTPSConnection(site)

# User inputs
secret = input("Enter the secret: ")
is_usa = input("Enter 1 if the country is USA, enter anything else if not: ")
if is_usa == "1":
    state = input("Enter the state name: ").replace(" ", "%20")
else:
    country = input("Enter the country name: ").replace(" ", "%20")
city = input("Enter the city name: ").replace(" ", "%20")

# Geocoding API request
if is_usa == "1":
    req = "/geo/1.0/direct?q=" + str(city) + "," + str(state) + ",US&appid=" + str(secret)
else:
    req = "/geo/1.0/direct?q=" + str(city) + "," + str(country) + "&appid=" + str(secret)
cnct.request("GET", req)
res = cnct.getresponse()
if res.status != 200:
    print("Geocoding API Error")
    exit()
body = res.read()
dec = body.decode()
obj = json.loads(dec)
if len(obj) == 0:
    print("Empty response from the server")
    exit()
print("City found:",obj[0]["name"])
print("State found:",obj[0]["state"])
print("Country found:",obj[0]["country"])
lat = obj[0]["lat"]
lon = obj[0]["lon"]

# Weather API request
req = "/data/3.0/onecall?lat=" + str(lat) + "&lon=" + str(lon) + "&exclude=minutely,hourly,daily,alerts&appid=" + str(secret)
cnct.request("GET", req)
res = cnct.getresponse()
if res.status != 200:
    print("One Call API Error")
    exit()
body = res.read()
dec = body.decode()
obj = json.loads(dec)
if len(obj) == 0:
    print("Empty response from the server")
    exit()
print("Temp:",obj["current"]["temp"])
print("Feels like:",obj["current"]["feels_like"])
print("Pressure:",obj["current"]["pressure"])
print("Humidity:",obj["current"]["humidity"])
print("Wind speed:",obj["current"]["wind_speed"])
print("Weather:",obj["current"]["weather"][0]["main"])