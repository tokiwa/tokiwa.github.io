const showStationsLength = 10;

let nearbyStations = {};
let stations = {};

const xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    switch (xhr.readyState) {
        case 4: {
            if(xhr.status == 200 || xhr.status == 304) {
                stations = JSON.parse(xhr.responseText);
            } else {
                console.log('Failed. HttpStatus: ' + xhr.statusText);
            }
            break;
        }
    }
};
 

let userPosition = {
    latitude: null,
    longitude: null
}
function updateUserPosition() {
    if (!navigator.geolocation){
        window.alert("Geolocation is not supported.");
        toggleRunning();
    }

    navigator.geolocation.getCurrentPosition(
        position => {
            userPosition.latitude = position.coords.latitude;
            userPosition.longitude = position.coords.longitude;
            deriveNearbyStations();

            console.log(userPosition.latitude, userPosition.longitude);
            console.log(nearbyStations);
            displayNearbyStations();
        },
        error => {
            window.alert("Unable to retrieve your location.");
            toggleRunning();
        }
    );
}
function deriveNearbyStations() {
    const stationsArray = Object.values(stations);
    stationsArray.sort((a, b) => {
        const aDistance = getDistance(userPosition.latitude, userPosition.longitude, a.lat, a.lon);
        const bDistance = getDistance(userPosition.latitude, userPosition.longitude, b.lat, b.lon);
        if (aDistance < bDistance) return -1;
        if (aDistance > bDistance) return 1;
        return 0;
    });

    const addedStation = [];
    for (let i = 0; i < 256; i++) {
        if (!addedStation.includes(stationsArray[i].name)) {
            nearbyStations[addedStation.length] = stationsArray[i];
            addedStation.push(stationsArray[i].name);
        }

        if (addedStation.length >= showStationsLength) break;
    }
}
function getDistance(lat1, lon1, lat2, lon2) {
    lat1 *= Math.PI / 180;
    lon1 *= Math.PI / 180;
    lat2 *= Math.PI / 180;
    lon2 *= Math.PI / 180;
    return 6371 * Math.acos(Math.cos(lat1) * Math.cos(lat2) * Math.cos(lon2 - lon1) + Math.sin(lat1) * Math.sin(lat2));
}


function displayNearbyStations() {
    const disp = document.getElementById("resultDisp");
    disp.innerHTML = null;

    for (let key of Object.keys(nearbyStations)) {
        const station = nearbyStations[key];
        const distance = getDistance(userPosition.latitude, userPosition.longitude, station.lat, station.lon);
        let cardHTML = "";
        cardHTML += '<div class="card grey lighten-5">';
        cardHTML += '<div class="card-content">';
        cardHTML += '<span class="card-title">#' + (Number(key) + 1) + ' ' + station.name + '</span>';
        cardHTML += '<p>距離: ' + getOptimizedDistance(distance) + '</p>';
        cardHTML += '<ul>';
        cardHTML += '</ul>';
        cardHTML += '</div>';
        cardHTML += '<div class="card-action">';
        cardHTML += '<a href="https://www.google.com/search?q=' + station.name + '駅" target="_blank" rel=""noopener"">Googleで検索</a>';
        cardHTML += '</div>';
        cardHTML += '</div>';

        disp.innerHTML += cardHTML;
    }
}
function getOptimizedDistance(distance) {
    const roundedDist = Math.round(distance * 1000) / 1000;
    if (roundedDist < 1) {
        return "約" + (roundedDist * 1000) + "m";
    } else {
        return "約" + roundedDist + "km";
    }
}


function doRequest(method, url) {
    xhr.open(method, url, false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    xhr.abort();
}

(function init() {
    doRequest("GET", "https://tokiwa.github.io/data/json/stations.json");
})();