
// Create the map object with center, zoom level and default layer.
let map = L.map('mapid').setView([38,-50],3);


// We create the tile layer that will be the background of our map.
L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
}).addTo(map);

//set marker options
var geojsonMarkerOptions = {
  radius: 8,
  fillColor: "#ff7800",
  color: "#000",
  weight: 1,
  opacity: 1,
  fillOpacity: 0.8
};


// Retrieve the  GeoJSON data.
d3.json("https://raw.githubusercontent.com/kylejohnsonks/Points_Region/main/means_by_province.geojson").then(function(data) {
  // Creating a GeoJSON layer with the retrieved data.
  L.geoJson(data, {
    // We turn each feature into a circleMarker on the map.
    pointToLayer: function(feature, latlng) { 
      return L.marker(latlng, geojsonMarkerOptions);
    },
    onEachFeature: function(feature, layer) {
      layer.bindPopup("Province: " + feature.properties.province+ "<br>Avg Precipitation: " + feature.properties.precipitation + "<br>Avg Temperature: "+feature.properties.temperature+"<br>Avg Wine Rating: "+feature.properties.points+"<br>(2016 data)");
    }
  }).addTo(map)
});

// .bindPopup("Precipitation: " + feature.properties.precipitation + "<br>Province: " + feature.properties.province);