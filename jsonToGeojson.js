
// Parameters
const folder = './2022-09-20/';
const file = 'data.json';

// Libs
const fs = require('fs');

function saveFile(file, content) {
    try {
        fs.writeFileSync(file, content, { flag: 'w+' });
        console.log('OK ' + file)
    } catch (err) {
        console.error('KO ' + file + ' ' + err);
    }
}

function convert(data) {
    var count = data.length;
    console.log('Converting...');

    // Create default geojson object structure
    var geo = {
        "type": "FeatureCollection",
        "features": []
    };

    // Loop through all the bookcase
    for (var i = 0; i < count; i++) {
        var b = data[i];
        var lat = parseFloat(b.lt);
        var lon = parseFloat(b.ln);

        // Create the geojson feature
        var f = {
            "type": "Feature",
            "properties": {
                "id": b.m,
                "name": b.t,
                "icon": b.i,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    lon, lat
                ]
            }
        };
        // Adding the feature in the geojson object
        geo.features.push(f);
    }

    console.log("Converted " + geo.features.length);

    // Convert the geojson object to string
    return JSON.stringify(geo, null, 4);
}

// Read data
const data = require(folder + file);
console.log("json file indicates it contains " + data.total + " bookcases");

console.log("Sort data...");
// sort books by id desc
var books = data.items.sort(function (a, b) { return parseInt(b.m) - parseInt(a.m) });

// remove duplicates
var coords = [];
var duplicates = [];
var uniques = [];

for (var i = 0; i < books.length; i++) {
    var cur = books[i];
    var curCoords = cur.lt + ',' + cur.ln;
    if (coords.includes(curCoords)) {
        // This is a duplicate!
        duplicates.push(cur);
    } else {
        // Not a duplicate
        uniques.push(cur);
        coords.push(curCoords);
    }
}

console.log("# Total: " + books.length);
console.log("# Uniques: " + uniques.length);
uniques = convert(uniques);
saveFile(folder + "bookcase.geojson", uniques);

console.log("# Duplicates: " + duplicates.length);
duplicates = convert(duplicates);
saveFile(folder + "duplicates.geojson", duplicates);

console.log("Done.");