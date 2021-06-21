#TP CHALLENGE_CLIMA_API
import requests
from tkinter import *
import math

city = "Argentine Republic, AR"
api_key = "ffde051916754056a29a02f25368dcf1"


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    humidity = response['main']['humidity']
    
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }

weather = get_weather(api_key, city)

root = Tk()
root.geometry("300x300")
root.title(f'{city[:-3]} Weather')

def display_city_name(city):
    city_label = Label(root, text=f"{city[:-3]}")
    city_label.config(font=("Consolas", 28))
    city_label.pack(side='top')

def display_stats(weather):
    temp = Label(root, text=f"Temperatura: {weather['temp']} F")
    feels_like = Label(root, text=f"Sensacion Termica: {weather['feels_like']} F")
    humidity = Label(root, text=f"Humedad: {weather['humidity']} %")

    temp.config(font=("Consolas", 22))
    feels_like.config(font=("Consolas", 16))
    humidity.config(font=("Consolas", 16))

    temp.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')


display_city_name(city)
display_stats(weather)

mainloop()

#alumnos :
#Gonzalo Medina
#Ezequiel Delaloye