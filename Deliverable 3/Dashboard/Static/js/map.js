// Add console.log to check to see if our code is working.
console.log("it's working!!!");

// We create the second tile layer that will be the background of our map.
let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

// Create the map object with center, zoom level and default layer.
let map = L.map("mapid", {
	center: [38, -50],
	zoom: 4,
	layers: [satelliteStreets]
});

// Create a base layer that holds all three maps.
let baseMaps = {
    "Satellite": satelliteStreets
  };
  


// create layers for the data
let precipitation = new L.LayerGroup();
let temperature = new L.LayerGroup();
let ratings = new L.LayerGroup();

// add reference to data in overlays object
let overlays = {
    "Precipitation": precipitation,
    "Temperature": temperature,
    "Ratings": ratings
  };

// Then we add a control to the map that will allow the user to change which
// overlays are visible.
L.control.layers(baseMaps, overlays).addTo(map);

// Retrieve the  GeoJSON data.
d3.json("https://raw.githubusercontent.com/kylejohnsonks/Points_Region/main/means_by_province.geojson").then(function(data) {
  // This function returns the style data for each of the variables we plot on
  // the map. We pass the value of the variable into two separate functions
  // to calculate the color and radius.
  function styleInfo(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: getColor(feature.properties.precipitation),
      color: "#000000",
      radius: getRadius(feature.properties.precipitation),
      stroke: true,
      weight: 0.5
    };
  }

// This function determines the color of the marker based on value of variable
  function getColor(precipitation) {
    if (precipitation > 1100) {
      return "#1E3F66";
    }
    if (precipitation > 900) {
      return "#2E5984";
    }
    if (precipitation > 800) {
      return "#528AAE";
    }
    if (precipitation > 700) {
      return "#73a5c6";
    }
    if (precipitation > 600) {
      return "#91bad6";
    }
    if (precipitation > 400) {
      return "#bcd2e8";
    }
    return "#000000";
  }

  // This function determines the radius of the  marker based on its magnitude.

  function getRadius(precipitation) {
    return precipitation / 25;
  }

  // Creating a GeoJSON layer with the retrieved data.
  L.geoJson(data, {
    // We turn each feature into a circleMarker on the map.
    pointToLayer: function(feature, latlng) {
          console.log("Latlng:"+latlng);
          return L.circleMarker(latlng);
    },
  // We set the style for each circleMarker using our styleInfo function.
    style: styleInfo,
 // We create a popup for each circleMarker to display the magnitude and location of the earthquake
 //  after the marker has been created and styled.
    onEachFeature: function(feature, layer) {
        layer.bindPopup("Precipitation: " + feature.properties.precipitation + "<br>Province: " + feature.properties.province);
}
}).addTo(precipitation);

// Then we add the earthquake layer to our map.
precipitation.addTo(map);  


});