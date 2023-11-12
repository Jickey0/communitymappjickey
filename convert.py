# ADD THIS TO EXISTING PYTHON FUNCTION
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="find my location")

address = str(event['address'])

loc = geolocator.geocode(address)

data = (location.latitude, location.longitude)

# table.put_item into our database