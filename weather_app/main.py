from flask import Flask, render_template
# from weather_handler import Weather # oma file, joka hakee tarvittavat sää tiedot käyttäjän syötteen mukaan

# fetched_weather = Weather("Hyvinkää").fetchWeather()
# print(fetched_weather)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather_page():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(debug=True)