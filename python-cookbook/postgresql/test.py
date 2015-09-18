'''
Created on Oct 28, 2014

@author: rajni
'''
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print(location.latitude, location.longitude)
print(location.raw)
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)

print vincenty(newport_ri, cleveland_oh).miles 