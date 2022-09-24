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

        # TODO poikkeuksen hallinta, mikäli pyyntö palauttaa muuta kuin code: 200
        # print(res.status_code)

        fetched_data = res.json() # data on muotoa dictionary

        name = fetched_data["name"] # koska data on dict, itemit on haettava key:n mukaan 
        icon = fetched_data["weather"][0]["icon"] # noudetussa dictissiä on myös joukossa lista, joka on huomioitava erikseen 0:nnella indexillä
        temperature = fetched_data["main"]["temp"]
        description = fetched_data["weather"][0]["description"]
        wind_speed = fetched_data["wind"]["speed"]
        humidity = fetched_data["main"]["humidity"]

        # koska noudettu "description" voi sisältää myös useampaa kuin yhtä stringiä, 
        # jonka javascript sitten tulkitsee erillisinä listoina (kun tuple:a viedessään muutetaan stringiksi js:lle, jonka js muuttaa listaksi)
        # js siis yrittää sijoittaa tiedot väärille paikoille muuten (js:n saaman listan alkioiden mukaan)

        # tämä hirvitys muuttaa descriptionista saadut stringit listaksi, erottaen välilyönnit pois,
        # ja samalla pistää sanojen (alkioiden) perään "-" -merkin, joka erotta visuaalisesti sanat toisistaan,
        # lopulta se yhdistää kaikki merkit toisiinsa, jättäen yhden "-" -merkin pois perältä ([:-1]) ja tallentuu muuttujana
        description_seperator = "".join(map((lambda word: word + "-"), description.split(" ")))[:-1]
        # välimerkit poistetaan myöhemmin javascriptissa
        # TODO koita keksiä parempi keino...

        return name, icon, temperature,  description_seperator, wind_speed, humidity