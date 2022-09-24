import requests

class Weather:
    """
    Käytää OpenWeatherMap:n tarjoamaa sää API:a

    Ottaa vastaan kaupungin nimen -> 
    palauttaa tuple:n, jonka arvot ovat: nimi (kaupungin), iconi (noudetun tiedoston nimi), 
    lämpötila (celsius), säätiedon kuvaus, tuulennoepus, ilmankosteus
    """

    # open weather api docs: https://openweathermap.org/current

    def __init__(self, city):
        self.city = city

    def fetchWeather(self):

        unit = "metric" # halutaan hakea mieluiten celcius-asteita, tyhjä tuo kelviniä
        api_key = "44f84fe26e6724a76dc61a818494e3c5" # api-avain on pakollinen (TODO nouda erillisestä tiedostosta)
        URL = "https://api.openweathermap.org/data/2.5/weather"

        keys = { # param keys
            "q": self.city,
            "units": unit,
            "appid": api_key,
        }

        res = requests.get(url=URL, params=keys) # yhdistää url:n ja parametrit yhdeksi url:ksi ja tekee pyynnön

        # TODO poikkeuksen hallinta, mikäli pyyntö palauttaa muuta kuin code: 200
        # print(res.status_code)

        fetched_data = res.json() # data on muotoa dictionary

        name = fetched_data["name"] # koska data on dict, itemit on haettava key:n mukaan 
        icon = fetched_data["weather"][0]["icon"] # noudetussa dictissiä on myös joukossa lista, joka on huomioitava erikseen 0:nnella indexillä
        temperature = fetched_data["main"]["temp"]
        description = fetched_data["weather"][0]["description"]
        wind_speed = fetched_data["wind"]["speed"]
        humidity = fetched_data["main"]["humidity"]

        required_data = (name, icon, temperature, description, wind_speed, humidity)

        return required_data
