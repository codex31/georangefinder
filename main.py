import math

def haversine(lat1, lon1, lat2, lon2):

    radius_earth = 6471.0

    # Lat 1
    lat1_radians = math.radians(lat1)
    lon1_radians = math.radians(lon1)

    # Lat 2
    lat2_radians = math.radians(lat2)
    lon2_radians = math.radians(lon2)

    # Difference between lat & lon
    dlat = lat2_radians - lat1_radians
    dlon = lon2_radians - lon1_radians

    # Haversine Formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_radians) * math.cos(lat2_radians) * math.sin(dlon /2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = radius_earth * c

    return math.floor(distance)

lat1 = -0.02252300
lon1 = 109.33030700

lat2 = 0.90879500
lon2 = 108.98459600

x = haversine(lat1, lon1, lat2, lon2)

print(x)
