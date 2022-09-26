function searchWeather(){
    let city_name = document.querySelector("#weather_search_field").value; // käyttäjän syöttämä kaupungin nimi

    const res = new XMLHttpRequest();
    res.open("POST", `/weather/${city_name}`); // valmistellaan säätietojen pyyntöä serveriltä kaupungin nimen mukaan

    res.send(); // laitetaan pyyntö serverille

    res.onload = () => { // pyyntö tuli vastaan, tehdään seuraavaa...
        const received_response = res.responseText; // serveriltä saatu vastaus

        if (!isNaN(received_response)){ // tuliko serveriltä virhe koodia?
            console.log(received_response);
        }

        else{ // ei tullut, joten voidaan tuoda säätiedot näkyviin

            // serveri palauttaa noudetun sää-datan json-muodossa,
            // joka sitten muunnetaan listaksi
            let weather_data = JSON.parse(received_response);

            // weather.html id nimiä
            const IDs = ["city_name", "weather_img", "current_temperature", "current_weather_name", "current_wind", "current_humidity"];
            let index = 0;
            for (let id_name of IDs){ // noutaa tagin id:n ja korvaa html -tagien arvot weather_datan mukaan

                document.querySelector("#"+id_name).textContent = weather_data[index];

                if (id_name == "weather_img"){
                    document.querySelector("#"+id_name).src = `http://openweathermap.org/img/wn/${weather_data[index]}@2x.png`;
                }
                else if (id_name == "current_temperature"){
                    document.querySelector("#"+id_name).textContent = weather_data[index] + " °C";
                }
                index++;
            }

        }

    }
}