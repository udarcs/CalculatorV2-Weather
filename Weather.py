import pyowm

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM("6312812b9c1f8a9288a12b2c62ef54da", config_dict)
mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature ('celsius')['temp']

print("В городе " + place + " сейчас: " + str(w.detailed_status))
print("Температура в цельсиях сейчас: " + str(temp))

if temp < 5:
	print( "Сейчас холодно, накинь куртку." )
elif temp < 10:
	print( "Сейчас прохладно, накинь худи." )
else:
	print( "Температура норм, одевай шорты." )
	
input()