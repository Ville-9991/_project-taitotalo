# Weather Web Application

## Description

Verkkosivu, jolla voi hakea säätiedotteita kaupungin nimen mukaan

Sivu käyttää OpenWeatherMap.org:n tarjoamaa API:ta

Sivu antaa tämän hetkisen säätyypin, lämpötilan, tuulennopeuden ja ilmankosteuden, sekä myös muuttaa kuvia että taustavärejä sään mukaan

## Setup and requirements

Backend vaatii Python-ympäristön. Sen voi ladata tietokoneelle sivulta: https://www.python.org/

- Kun Python on asennettu, on hyvä käyttää Python virtuaaliympäristöä. 
- Tämän repository:n ladattua tietokoneelle, joukossa on "weather app" niminen kansio.
- Avaa kyseinen kansio (windows file explorer/resurssien hallinta tai mikä tahansa file manager)
- Kansion sisä näkymässä, avataan komentorivi (CMD/powershell/bash/mikä tahansa...)
- komento riviin kirjoitetaan "python -m venv env" (ilman lainausmerkkejä) ja painetaan enter. (Olettaen että Python on asennettu)
- Python luo "env" nimisen kansion "weather app" kansion sisälle. (Tässä voi kestää hetki)
- Kun kansio on luotu, aktivoidaan virtuaaliympäristö. 
- Kirjoita komentoriviin "env\scripts\active" (tai $env/scripts/activate jos muu kuin windows)
- komentorivin alkuun pitäisi nyt tulla nälyviin "(env)". Tämä tarkoittaa että käytössä on virtuaali ympäristö.
- Nyt kirjoitetaan "pip install -r requirements.txt". Tämän asentaa tarvittavat python-kirjastot ohjelman suorittamiseksi.
- Kun tämä on tehty, kirjoitetaan vielä "env\scripts\python main.py".
- Nyt tietokone ajaa main.py nimisen tiedoston ja avaa portin, jossa sivua voi katsella
- Viimeisenä avaa internetselain ja kirjoita hakukenttään localhost:5000 (tai paina komentorivissä näkyvää ip-osoitetta käyttämällä ctrl + hiiren oikea) 
