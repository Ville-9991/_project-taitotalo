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
    name = city_name
    print(type(name))

    # fetched_weather = Weather(name).fetchWeather()
    return "City Name Received Successfully"

if __name__ == "__main__":
    app.run(debug=True)