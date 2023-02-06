from tkinter import *
from PIL import ImageTk, Image
import sv_ttk
import pyowm
import requests
import datetime

# GUI Properties
win = Tk()
win.iconbitmap('weather.ico')
sv_ttk.set_theme("light")
win.minsize(400, 310)
win.maxsize(400, 310)
win.geometry("400x310")
win.eval('tk::PlaceWindow . center')
win.wm_title("Weather App")

# Get current time
current_time = datetime.datetime.now()

# Get Location
place = requests.get('https://ipinfo.io')
data = place.json()
city = data['city']
state = data['region']

# Provide API key, get location and gather weather
owm = pyowm.OWM('FREE OWM API KEY')
weather_mgr = owm.weather_manager()
observation = weather_mgr.weather_at_place(city)
weather = observation.weather
degree_sign = u"\N{DEGREE SIGN}"

# Gather current weather information
wind = weather.wind()
humidity = weather.humidity
rain = weather.rain
heat = weather.heat_index
clouds = weather.clouds
temp = weather.temperature('fahrenheit')
details = weather.detailed_status

# --Determine icon forloop:
# Have list of weather icons to choose from
# Get icons from here: https://iconarchive.com/tag/weather
# Check for keywords in the details variable to determine which icon to use
# IE: if the details contain clouds, display the clouds icon etc.
# Then display the appropriate icon below the weather details and temp

# --printable items for testing
# print(temp)
# print(wind)
# print(humidity)
# print(rain)
# print(heat)
# print(clouds)
# print(details)
# print(city)
# print(state)

# display location
location_label = Label(win, text=str(city) + ', ' + str(state), font=('Arial Black', 12))
location_label.pack(pady=0)

# display weather details
weather_details = Label(win, text=str(details).title(), font=('Arial Black', 12))
weather_details.pack(pady=0)
weather_temp = Label(win, text=str(round(temp['temp'])) + str(degree_sign) + 'F', font=('Arial Black', 25))
weather_temp.pack(pady=0)

# display weather icon
weather_icon = ImageTk.PhotoImage(Image.open("clouds.png"))
img_label = Label(image=weather_icon, height=180, width=250)
img_label.pack(pady=0)

# Show last updated time
current_time_label = Label(win, text='Last Updated: ' + current_time.strftime('%m/%d/%Y %I:%M:%S'), font=('Arial', 10))
current_time_label.pack(pady=0)

win.mainloop()
