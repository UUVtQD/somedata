#!/usr/bin/env python3
from os import getenv
from os import environ
#import os
import pyowm

try:
    environ["CITY_NAME"]
except KeyError:
    print("Please set environment variable \"CITY_NAME\"")
    exit(1)
try:
    environ["OPENWEATHER_API_KEY"]
except KeyError:
    print("Please set environment variable \"OPENWEATHER_API_KEY\"")
    exit(1)

city = getenv("CITY_NAME")
owm = pyowm.OWM(getenv("OPENWEATHER_API_KEY"))


# print(f"{owm}")
place = owm.weather_at_place(city)
w = place.get_weather()
print(f"source=openweathermap, city=\"{city}\", description=\"{w.get_detailed_status()}\", temp={w.get_temperature('fahrenheit')['temp']}, humidity={w.get_humidity()} \n")
