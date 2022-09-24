function searchWeather(){
    let city_name = document.querySelector("#weather_search_field").value;
    console.log(city_name);

    const res = new XMLHttpRequest();
    res.open("POST", `/weather/${city_name}`);

    res.onload = () => {
        const flaskMessage = res.responseText
        console.log(flaskMessage)
    }
    res.send()
}