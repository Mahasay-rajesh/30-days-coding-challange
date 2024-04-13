import phonenumbers
from phonenumbers import geocoder,carrier
import opencage
from opencage.geocoder import OpenCageGeocode

number ="+919693631293"
phno = phonenumbers.parse(number)
country = geocoder.description_for_number(phno,"en")
print(country)
print(carrier.name_for_number(phno,"en"))
key ="41950aea49f54a8aa2ca92ec14a8e805"
geo = OpenCageGeocode(key)
result = geo.geocode(country)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)