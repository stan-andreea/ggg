import requests

def get_location():
    response = requests.get("https://ipinfo.io/")
    data = response.json()
    location = data['loc']  # This returns a string like "latitude,longitude"
    latitude, longitude = map(float, location.split(','))
    return latitude, longitude

LAT, LON = get_location()

# Get nearest planes from current IP location +/- 2 lat/lon degrees
LAT_MIN = LAT - 2.0
LAT_MAX = LAT + 2.0
LON_MIN = LON - 2.0
LON_MAX = LON + 2.0

print(LAT, LON)
