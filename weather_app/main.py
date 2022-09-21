from flask import Flask, render_template
# from flask_socketio import SocketIO, send

app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")

# @socketio.on("message") # pitää olla message muuten ei toimi
# # vaihtoehdot parametreiksi:
# # message, connect, disconnect, json
# def handle_message(msg):
#     print(msg)
#     if msg != "User connected":
#         send(msg, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather_page():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, host="localhost")