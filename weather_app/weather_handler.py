import requests
import json

class Weather:
    """
    Käytää OpenWeatherMap:n tarjoamaa sää API:a

    Ottaa vastaan kaupungin nimen -> 
    palauttaa json-muotoon muunnetun tuple:n, jonka arvot ovat: nimi (kaupungin), iconi (noudetun tiedoston nimi), 
    lämpötila (celsius), säätiedon kuvaus, tuulennoepus, ilmankosteus.

    HTTP-virheen ilmeentyessä paluttaa virhekoodin.
    """

    # open weather api docs: https://openweathermap.org/current

    def __init__(self, city):
        self.city = city

    def fetchWeather(self):

        unit = "metric" # halutaan hakea mieluiten celsius-asteita, tyhjä tuo kelviniä
        api_key = "44f84fe26e6724a76dc61a818494e3c5" # api-avain on pakollinen (TODO nouda erillisestä tiedostosta)
        URL = "https://api.openweathermap.org/data/2.5/weather"
        lang = "fi"

        keys = { # param keys
            "q": self.city,
            "units": unit,
            "appid": api_key,
            "lang": lang
        }

        res = requests.get(url=URL, params=keys) # yhdistää url:n ja parametrit yhdeksi url:ksi ja tekee pyynnön

        if res.status_code != 200:
            return res.status_code

        fetched_data = res.json() # data on muotoa dictionary
        
        if "name" not in fetched_data:
            return res.status_code
        
        else:
            name = fetched_data["name"] # koska data on dict, itemit on haettava key:n mukaan 
            icon = fetched_data["weather"][0]["icon"] # noudetussa dictissiä on myös joukossa lista, joka on huomioitava erikseen 0:nnella indexillä
            temperature = fetched_data["main"]["temp"]
            description = fetched_data["weather"][0]["description"]
            wind_speed = fetched_data["wind"]["speed"]
            humidity = fetched_data["main"]["humidity"]

            required_data = (name, icon, temperature, description, wind_speed, humidity)

            return json.dumps(required_data)