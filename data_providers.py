import requests
from location import LAT_MIN, LAT_MAX, LON_MIN, LON_MAX

URL = f"https://opensky-network.org/api/states/all?lamin={LAT_MIN}&lomin={LON_MIN}&lamax={LAT_MAX}&lomax={LON_MAX}"

def get_opensky_data():
    r = requests.get(URL).json()
    airplanes_data = [ [s[5], s[6], s[7], s[9]] for s in r['states'] if s[5] and s[6] and s[7] and s[9] ]
    return airplanes_data
