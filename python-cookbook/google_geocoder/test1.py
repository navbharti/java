'''
Created on Nov 9, 2014
http://carsonfarmer.com/2013/07/essential-python-geo-libraries/
@author: rajni
'''
'''
from pygeocoder import Geocoder
results = Geocoder.geocode("pondicherry")
print(results[0].coordinates)
'''


import urllib

response = urllib.urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA').read()

print(response)

'''


from geopy.geocoders import Nominatim

geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
'''