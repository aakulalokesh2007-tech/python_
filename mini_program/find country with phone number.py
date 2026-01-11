import phonenumbers
from phonenumbers import geocoder

ph=phonenumbers.parse("+917397430285")

print(geocoder.description_for_number(ph,"en"))
