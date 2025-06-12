import math
from location import LAT, LON

EARTH_RADIUS = 6371.2
#Distance on globe from location to another airplane
def haversine(lat1, lon1, lat2, lon2):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    hav = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return EARTH_RADIUS * 2 * math.atan2(math.sqrt(hav), math.sqrt(1 - hav))

#Returns the altitudes for the nearest n planes (for now, n = 4)
#Input: data - array, containing:
# data[0] - longitude
# data[1] - latitude
# data[2] - barometric altitude (meters)
# data[3] - geometric altitude (meters)
# Took them in order from https://openskynetwork.github.io/opensky-api/rest.html#all-state-vectors
def get_nearest_planes_altitudes(airplanes_data):
    nearest_altitudes = sorted(
        [data for data in airplanes_data if data[3] > 0]
        ,key=lambda data: haversine(LAT, LON, data[1], data[0])
    )[:4]
    return [data[3] for data in nearest_altitudes] # Altitudes

def altitude_to_voltage(altitude_ft, max_alt=12192.6, max_v=3.3):
    return min(max((altitude_ft / max_alt) * max_v, 0), max_v)

#Returns the voltages by providing the planes data as described in get_nearest_planes_altitudes
def get_voltages(airplanes_data):
    altitudes = get_nearest_planes_altitudes(airplanes_data)
    return [altitude_to_voltage(altitude) for altitude in altitudes]
import math
from location import LAT, LON

EARTH_RADIUS = 6371.2 #km
#Distance on globe from location to another airplane
def haversine(lat1, lon1, lat2, lon2):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    hav = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return EARTH_RADIUS * 2 * math.atan2(math.sqrt(hav), math.sqrt(1 - hav))

#Returns the voltage data for the nearest n planes (for now, n = 4)
#Input: data - array, containing:
# data[0] - longitude
# data[1] - latitude
# data[2] - barometric altitude (meters)
# data[3] - velocity (m/s)
# Outputs baro altitude (first), velocity(second) and distance(third) for the nearest planes.
# Assumes all elements are != null.
# Took them in order from https://openskynetwork.github.io/opensky-api/rest.html#all-state-vectors
def get_nearest_planes_altitudes_velocities_distances(airplanes_data):
    nearest_data = sorted(
        [data for data in airplanes_data]
        ,key=lambda data: haversine(LAT, LON, data[1], data[0])
    )[:4]
    return [ [data[2], data[3], haversine(LAT, LON, data[1], data[0]) ] for data in nearest_data] # Altitudes

max_alt = 13500 #meters
max_vel = 300     #m/s
max_dist = 300    #km
def value_to_voltage(val, max_val, max_v = 3.3):
    return min(max((val / max_val) * max_v, 0), max_val) 

#Returns the voltages by providing the planes data as described in get_nearest_planes_altitudes
def get_voltages(airplanes_data):
    nearest_data = get_nearest_planes_altitudes_velocities_distances(airplanes_data)
    print(nearest_data)
    alt_voltages = [ value_to_voltage(entry[0], max_alt) for entry in nearest_data ]
    vel_voltages = [ value_to_voltage(entry[1], max_vel) for entry in nearest_data ]
    dist_voltages = [ value_to_voltage(entry[2], max_dist) for entry in nearest_data ]
    print(f"altitudes:{alt_voltages}\nvel_voltages:{vel_voltages}\ndist_voltages:{dist_voltages}")
    return [alt_voltages, vel_voltages, dist_voltages]