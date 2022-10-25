import requests
import json

class Weather:
    """
    Käytää OpenWeatherMap:n tarjoamaa sää API:a

    Ottaa vastaan kaupungin nimen -> 
    palauttaa json-muotoon muunnetun tuple:n, jonka arvot ovat: nimi (kaupungin), iconi (noudetun tiedoston nimi), 
    lämpötila (celsius), säätiedon kuvaus, tuulennoepus, ilmankosteus, liukuvärit.

    HTTP-virheen ilmeentyessä paluttaa virhekoodin.
    """

    # open weather api docs: https://openweathermap.org/current

    def __init__(self, city):
        self.city = city

    def fetchWeather(self):

        unit = "metric" # halutaan hakea mieluiten celsius-asteita, tyhjä tuo kelviniä

        try:
            api_key = open("..\key.txt", "r") # api-avain on pakollinen. avain haetaan erillisestä tiedostosta
        except IOError:
            print("API key file is missing or the file path is incorrect")
            return "500"

        URL = "https://api.openweathermap.org/data/2.5/weather"
        lang = "fi"

        keys = { # param keys
            "q": self.city,
            "units": unit,
            "appid": api_key.read(),
            "lang": lang
        }

        try:
            res = requests.get(url=URL, params=keys) # yhdistää url:n ja parametrit yhdeksi url:ksi ja tekee pyynnön
        except:
            print("Something went wrong with making an API call")
            api_key.close()
            return "500"

        api_key.close() # tiedosto on suljettava, kun ei ole käytölle enää tarvetta

        if res.status_code != 200:
            return res.status_code

        fetched_data = res.json() # data on muotoa dictionary
        
        if "name" not in fetched_data: # varmuuden vuoksi myös tarkastetaan että löytyykö "name" keytä oikeasti (eli onko käyttäjän syöttämä kaupunki saatavana)
            return res.status_code
        
        else:
            name = fetched_data["name"] # koska data on dict, itemit on haettava key:n mukaan 
            icon = fetched_data["weather"][0]["icon"] # noudetussa dictissiä on myös joukossa lista, joka on huomioitava erikseen 0:nnella indexillä
            temperature = round(fetched_data["main"]["temp"]) # api antaa lukuja desimaaleina, halutaan näyttää ne mieluiten kokonaislukuina
            main_waether_type = fetched_data["weather"][0]["main"]
            description = fetched_data["weather"][0]["description"]
            wind_speed = fetched_data["wind"]["speed"]
            humidity = fetched_data["main"]["humidity"]

            img_source = f"../static/img/wth/{icon}.png" # sään pikkukuvake
            bg_img_source = f"../static/img/wth/bg/{main_waether_type}_{icon}.png" # sään taustakuva datasta saadun "main" ja "icon" arvojen perusteella

            def getColorBasedOnWeather(): # funktio joka noutaa datasta saadun sää tyypin (main) ja palauttaa sen mukaan määritetyn värin hexadesimaali muodossa listana
                # myöhemmin käytettävään tupleen, joka sitten lopuksi käytetään javascriptissä

                # kaikki mahdolliset säätyypit, mitä openweathermap.org voi antaa: https://openweathermap.org/weather-conditions
                # possible_weather_types = ("Thunderstorm", "Drizzle", "Rain", "Snow", "Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado", "Clear", "Clouds")

                if main_waether_type == "Thunderstorm": # Thunderstorm
                    colors = ("#72b6e3", "#103569")
                    return colors

                elif main_waether_type == "Drizzle": # Drizzle
                    colors = ("#99c8e7", "#256acb")
                    return colors
                    
                elif main_waether_type == "Rain": # Rain
                    colors = ("#5e7f95", "#204579")
                    return colors
                    
                elif main_waether_type == "Snow": # Snow
                    colors = ("#0533d6", "#f2f3f5")
                    return colors
                    
                elif main_waether_type == "Mist": # Mist
                    colors = ("#d0d2d4", "#93a6c1")
                    return colors
                    
                elif main_waether_type == "Smoke": # Smoke
                    colors = ("#898a8b", "#c9b082")
                    return colors
                    
                elif main_waether_type == "Haze": # Haze
                    colors = ("#898a8b", "#7e7461")
                    return colors
                    
                elif main_waether_type == "Dust": # Dust
                    colors = ("#ccaf5f", "#cfb37f")
                    return colors
                    
                elif main_waether_type == "Fog": # Fog
                    colors = ("#6c7b91", "#a7aaad")
                    return colors
                    
                elif main_waether_type == "Sand": # Sand
                    colors = ("#cfb37f", "#ccaf5f")
                    return colors
                    
                elif main_waether_type == "Ash": # Ash
                    colors = ("#525050", "#342524")
                    return colors
                    
                elif main_waether_type == "Squall": # Squall
                    colors = ("#212749", "#606778")
                    return colors
                    
                elif main_waether_type == "Tornado": # Tornado
                    colors = ("#484a82", "#c2c3c6")
                    return colors
                    
                elif main_waether_type == "Clear": # Clear
                    colors = ("#1a3cdb", "#51b5e8")
                    return colors
                    
                elif main_waether_type == "Clouds": # Clouds
                    colors = ("#27367d", "#4491b8")
                    return colors
            
            required_data = (name, img_source, bg_img_source, temperature, description, wind_speed, humidity, getColorBasedOnWeather())

            return json.dumps(required_data)