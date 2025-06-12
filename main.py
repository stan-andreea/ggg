import requests
import math
from data_providers import get_opensky_data
from conversion_intf import get_voltages

opensky_data = get_opensky_data()
voltages = get_voltages(opensky_data)
print(voltages)

