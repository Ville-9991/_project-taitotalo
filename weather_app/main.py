from flask import Flask, render_template
from weather_handler import Weather # oma file, joka hakee tarvittavat sää tiedot käyttäjän syötteen mukaan

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather_page():
    return render_template("weather.html")

@app.route("/weather/<string:city_name>", methods=["POST"])
def process_weather(city_name):
    name = city_name # js:sstä saatu kaupungin nimi

    # täällä hetkellä ei tiedetä parempaa keinoa välittää tuple:a js:lle kuin
    # sen muunttaminen stringiksi ja palauttaminen flaksin avulla (hyväksyy vain str)
    fetched_weather = " ".join(map(str, Weather(name).fetchWeather()))
    # TODO vielä ottaa vastaan mitä vain käyttäjä syöttää, mikä voi aihettaa ongelmia API:lta noudetaessa
    # luo virheen hallinta siltä varalta

    return fetched_weather

if __name__ == "__main__":
    app.run(debug=True)