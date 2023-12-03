# Online resources used:
# - OpenWeather API One Call API 3.0    https://openweathermap.org/api/one-call-3
# - Python Tutorial                     https://www.w3schools.com/python/default.asp
# - Python 3 HTTP protocol client       https://docs.python.org/3/library/http.client.html


# This built-in Python 3 library will be used to send HTTPS requests
import http.client
site = "api.openweathermap.org"
cnct = http.client.HTTPSConnection(site)

# Latitude and longitude inputs (corresponds to upper Manhattan)
lat = 40.8240
lon = -73.9448

# Very simple API request, response is printed to console
req = "/data/3.0/onecall?lat=" + str(lat) + "&lon=" + str(lon) + "&exclude=minutely,hourly,daily,alerts&appid=51e128ed396b2562a2351dcfe06eb7a5"
cnct.request("GET", req)
res = cnct.getresponse()
print(res.read())