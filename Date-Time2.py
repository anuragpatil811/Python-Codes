from datetime import *
import pytz
newtz = pytz.timezone("Australia/Canberra")
x = datetime.now(newtz)
#print(datetime.now(pytz.utc))
print(x)
#print(newtz)

#Timezones of all countries and regions
#for key, val in pytz.country_timezones.items():
#    print(key, "=", val)