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
win.wm_title("Weather Widget")

# Get current time
current_time = datetime.datetime.now()

# Get Location
place = requests.get('https://ipinfo.io')
data = place.json()
city = data['city']
state = data['region']

# Provide API key, get location and gather weather
owm = pyowm.OWM('FREE OPM API KEY')
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

# list of weather icons
cloudy = "clouds.png"
rainy = "rain.png"
sunny = "sun.png"
snowy = "snow.png"
stormy = "storm.png"
hail = "hail.png"

# assign icon to weather status details:
if "cloud" in details:
    img_path = cloudy
elif "rain" in details:
    img_path = rainy
elif "sun" in details:
    img_path = sunny
elif "snow" in details:
    img_path = snowy
elif "storm" in details:
    img_path = stormy
elif "hail" in details:
    img_path = hail
else:
    print("Error: status did not match icon.")

# Display location
location_label = Label(win, text=str(city) + ', ' + str(state), font=('Arial Black', 12))
location_label.pack(pady=0)

# Display weather details
weather_details = Label(win, text=str(details).title(), font=('Arial Black', 12))
weather_details.pack(pady=0)
weather_temp = Label(win, text=str(round(temp['temp'])) + str(degree_sign) + 'F', font=('Arial Black', 25))
weather_temp.pack(pady=0)

# Display weather icon
weather_icon = ImageTk.PhotoImage(Image.open(str(img_path)))
img_label = Label(image=weather_icon, height=180, width=250)
img_label.pack(pady=0)

# Display last updated time
current_time_label = Label(win, text='Last Updated: ' + current_time.strftime('%m/%d/%Y %I:%M:%S'), font=('Arial', 10))
current_time_label.pack(pady=0)

win.mainloop()
