'''
Created on Feb 16, 2015

@author: rajni
'''

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")