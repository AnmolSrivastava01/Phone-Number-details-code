import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("Enter your phone number +__:")#example +919876543210
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(time)
print(phone)
print(car)
print(reg)
