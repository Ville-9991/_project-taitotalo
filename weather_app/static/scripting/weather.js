function searchWeather(){
    let city_name = document.querySelector("#weather_search_field").value; // käyttäjän syöttämä kaupungin nimi

    if (String(city_name).length === 0){ // ensimmäisenä katsotaan onko käyttäjän syöte tyhjä, ennen kuin edes tehdään pyyntöä serveriltä
        return;
    }

    else{ // ...ei ollut tyhjä

        const res = new XMLHttpRequest();
        res.open("POST", `/weather/${city_name}`); // valmistellaan säätietojen pyyntöä serveriltä kaupungin nimen mukaan

        res.send(); // laitetaan pyyntö serverille

        res.onload = () => { // pyyntö tuli vastaan, tehdään seuraavaa...
            const received_response = res.responseText; // serveriltä saatu vastaus

            if (!isNaN(received_response)){ // tuliko serveriltä virhe koodia?

                // "tuloksia ei löytynyt" kohta näkyviin
                document.querySelector("#results_not_found_container").style.display = "flex";
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

                    if (id_name == "weather_img"){ // kuvakkeen kohdalla noudetaan datan mukana tulleen lähteen mukainen kuvake
                        document.querySelector("#"+id_name).src = weather_data[index];
                    }
                    else if (id_name == "current_temperature"){
                        document.querySelector("#"+id_name).textContent = weather_data[index] + " °C";
                    }
                    index++;
                }

                // "tuloksia ei löytynyt" kohta piiloon
                document.querySelector("#results_not_found_container").style.display = "none";
            }
        }
    }
}