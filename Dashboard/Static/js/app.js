function test() {
    let changedElement = d3.select(this);
    // Save the value that was changed as a variable.
    let changedValue = changedElement.property('value');
    // Save the id of the filter that was changed as a variable.
    let filterID = changedElement.attr('id');
    console.log(changedValue);
  // Attach an event to listen for changes to each filter
}  
d3.selectAll('input').on('change',test);

//Machine Learning function 
function ML(event) {
  // event.preventDefault();
  let values = [];
  for (const feature of [].slice.call(document.getElementsByClassName("MLData"))){
    values.push(feature.value);
  }
  // console.log(values);
  url = '/predict/';
  for (const value in values) {
    url+=values[value]+'/';
  }
  url=url.slice(0,-1);
  console.log(url)
  // window.location.href=url;
  fetch(url)
    .then(response => response.json())
    // .then(result => console.log(result))
    .then(result=>document.getElementById("result").innerHTML='<h1>'+result+'</h1>');
  }

//watch for Button click 
d3.select("a").on("click", ML);

//add varieties and provinces variables
var varieties = ['Barbera','Bordeaux-style Red Blend','Bordeaux-style White Blend','Cabernet Franc','Cabernet Sauvignon','Champagne Blend','Chardonnay','Corvina','Dolcetto','Garganega','Gewurztraminer','Glera','Grenache','Malbec','Meritage','Merlot','Moscato','Mourvedre','Nebbiolo','Nero dAvola','Petit Verdot','Petite Sirah','Pinot Blanc','Pinot Grigio','Pinot Gris','Pinot Noir','Red Blend','Rhone-style Red Blend','Rhone-style White Blend','Riesling','Rose','Sangiovese','Sangiovese Grosso','Sauvignon Blanc','Sparkling Blend','Syrah','Tempranillo','Vermentino','Viognier','White Blend','Zinfandel']
var provinces = ['Alsace','Aquitaine','Burgundy','California','Champagne-Ardenne','New York','Oregon','Piemonte','Sicilia','Tuscany','Veneto','Washington']

//build provinces options list
for (i=0; i < provinces.length; i++){
  var opt = document.createElement("option");
  document.getElementById("provops").innerHTML += '<option id="' + i + '" value="' + provinces[i] + '">'+provinces[i]+'</option>';
}

//build varieties options list
for (i=0; i < varieties.length; i++){
  var opt = document.createElement("option");
  document.getElementById("vrtyops").innerHTML += '<option id="' + i + '" value="' + varieties[i] + '">'+varieties[i]+'</option>';
}