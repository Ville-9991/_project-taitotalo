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
def process_weather(city_name): # js:stä saatu kaupungin nimi

    if str(city_name).isnumeric(): # client voi antaa numeron, jota ei voida käsitellä, 
        return "400"               # joten palautetaan heti bad request 400

    response_to_client = Weather(city_name).fetchWeather()
    
    if not str(response_to_client).isnumeric(): # normaalisti pitäisi tulla json-muotoon muunnettu tuple, 
        return response_to_client               # jossa on noudetut säätiedot, jotka sitten palautetaan
         
    else:
        # voi kuitenkin olla että Weather.fetchWeather() palauttaa HTTP-virhekoodia
        return str(response_to_client)

if __name__ == "__main__":
    app.run(debug=True)