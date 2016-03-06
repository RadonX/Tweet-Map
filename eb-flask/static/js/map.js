// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

var map, heatmap, points;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 2,
        center: {lat: 0, lng: 0},
        mapTypeId: google.maps.MapTypeId.SATELLITE
    });
    $.when(getPoints()).then(function() {
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: points,
            map: map
        });
    });
}

function toggleHeatmap() {
    heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
    var gradient = [
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 0, 255, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
    ]
    heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
    heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
    heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

console.log('fetch json file: ' + field);

// Heatmap data: 500 Points
function getPoints() {
    var deferred = $.Deferred();
    // ref: http://stackoverflow.com/questions/15360393/force-code-to-execute-after-another-method-finishes-executing

    /* data format: getJSON[geometry]*/
    $.getJSON('json?keyword='+field, function(data) {
        points = [];
        $.each( data, function( key, val ) { // key == geo
            val.forEach(function(coord) {
                points.push(new google.maps.LatLng(coord['coordinates'][1], coord['coordinates'][0]));
            })
        });
        deferred.resolve();
    });
    return deferred;
}
