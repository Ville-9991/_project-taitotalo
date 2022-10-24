function searchWeather(city_name){
    city_name = document.querySelector("#weather_search_field").value; // käyttäjän syöttämä kaupungin nimi

    if (String(city_name).length === 0){ // ensimmäisenä katsotaan onko käyttäjän syöte tyhjä, ennen kuin edes tehdään pyyntöä serveriltä
        return;
    }

    else{ // ...ei ollut tyhjä

        const res = new XMLHttpRequest();
        res.open("POST", `/weather/${city_name}`); // valmistellaan säätietojen pyyntöä serveriltä kaupungin nimen mukaan

        res.send(); // laitetaan pyyntö serverille

        res.onload = () => { // pyyntö sai vastauksen, tehdään seuraavaa...
            const received_response = res.responseText; // serveriltä saatu vastaus

            if (!isNaN(received_response)){ // tuliko serveriltä virhe koodia?

                // "tuloksia ei löytynyt" kohta näkyviin
                document.querySelector("#results_not_found_container").style.display = "flex";
            }

            else{ // ei tullut, joten voidaan tuoda säätiedot näkyviin

                // serveri palauttaa noudetun sää-datan json-muodossa,
                // joka sitten muunnetaan listaksi
                const weather_data = JSON.parse(received_response);

                const weather_color = weather_data.slice(-1); // datasta saatu sää tyyppin väri (listan viimeinen index)

                document.querySelector("#weather_root").style.background = `linear-gradient(${weather_color})`; // likuväri tausta

                // weather-widget kehyksen css tyylittely
                let widget_container = document.querySelector("#weather_summary_field_container").style;
                widget_container.border = "solid transparent";
                widget_container.borderImage = `linear-gradient(145deg, ${weather_color})`; // kehyksen liukuväri
                widget_container.borderImageSlice = "1";

                // hakukentän kehys
                // document.querySelector("#weather_search_root input[type='text']").style = `3px solid (${weather_color[0][1]})`; // värit on tuplena, joten ne on yksilöitävä (tässä käytetään jälkimmäistä väriä)

                // weather.html id nimiä
                const IDs = ["city_name", "weather_img", "weather_bg_img", "current_temperature", "current_weather_name", "current_wind", "current_humidity"];
                let data_index = 0; // index, jolla tullaan viitataamaan weather_data:n alkioita
                for (let id_name of IDs){ // noutaa tagin id:n ja korvaa html -tagien arvot weather_datan mukaan

                    document.querySelector("#"+id_name).textContent = weather_data[data_index];

                    if (id_name == "weather_img"){ // kuvakkeen kohdalla noudetaan datan mukana tulleen lähteen mukainen kuvake
                        document.querySelector("#"+id_name).src = weather_data[data_index];
                    }
                    else if (id_name == "weather_bg_img"){ // widgeting taustakuvalle tehdään sama homma
                        document.querySelector("#"+id_name).src = weather_data[data_index]; // (alkiossa on taustakuvalle eri lähdepolku kuin pikkukuvalle)
                    }
                    else if (id_name == "current_temperature"){
                        document.querySelector("#"+id_name).textContent = weather_data[data_index] + " °C";
                    }
                    data_index++;
                }

                // "tuloksia ei löytynyt" kohta piiloon
                document.querySelector("#results_not_found_container").style.display = "none";
            }
        }
    }
}

const load_default_city = document.addEventListener("DOMContentLoaded", () => { // kun DOM on latautunut
    let default_city = document.querySelector("#weather_search_field").value = "Suomi"; // annetaan oletus sijainniksi "Suomi" (TODO koita saada käyttäjän sijainit...)
    searchWeather(default_city);
});

const search_with_enter_key = document.addEventListener("keyup", () => {
    if(event.key === "Enter"){ // kaupungin haku enterin paianlluksella
        searchWeather();
    }
});