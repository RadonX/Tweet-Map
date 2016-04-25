// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

var map, heatmap, points;


function initMap() {

  /*
  var myData = new Array();
    for ( var i = 0; i<500;i++){
      var t = Math.random();
      if (t < 0.333333){
        t = -0.5;
      }
      else if (t > 0.666667) {
        t = 0.5;
      }
      else {
        t = 0;
      }
      var tmp = {
        tweettype:"concert",
        sentiment: t,
        LatLng:myLatLng[i]
      };
      myData[i]=tmp;
    }*/
  var myData = processPoints();

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 2,
    center: {lat: 0, lng: 0},
    mapTypeId: google.maps.MapTypeId.SATELLITE
  });

  var icon_concert = {
    url: "static/icons/c_concertneu.png", // url
    scaledSize: new google.maps.Size(40, 40), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
  };
    var icon_concertpos = {
      url: "static/icons/c_concertpos.png", // url
      scaledSize: new google.maps.Size(40, 40), // scaled size
      origin: new google.maps.Point(0,0), // origin
      anchor: new google.maps.Point(0, 0) // anchor
    };
      var icon_concertneg = {
        url: "static/icons/c_concertneg.png", // url
        scaledSize: new google.maps.Size(40, 40), // scaled size
        origin: new google.maps.Point(0,0), // origin
        anchor: new google.maps.Point(0, 0) // anchor
      };
  var icon_run = {
    url: "static/icons/c_runneu.png", // url
    scaledSize: new google.maps.Size(40, 40), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
};
var icon_runpos = {
url: "static/icons/c_runpos.png", // url
scaledSize: new google.maps.Size(40, 40), // scaled size
origin: new google.maps.Point(0,0), // origin
anchor: new google.maps.Point(0, 0) // anchor
};
var icon_runneg = {
url: "static/icons/c_runneg.png", // url
scaledSize: new google.maps.Size(40, 40), // scaled size
origin: new google.maps.Point(0,0), // origin
anchor: new google.maps.Point(0, 0) // anchor
};
var icon_party = {
  url: "static/icons/c_partyneu.png", // url
  scaledSize: new google.maps.Size(40, 40), // scaled size
  origin: new google.maps.Point(0,0), // origin
  anchor: new google.maps.Point(0, 0) // anchor
};
var icon_partypos = {
  url: "static/icons/c_partypos.png", // url
  scaledSize: new google.maps.Size(40, 40), // scaled size
  origin: new google.maps.Point(0,0), // origin
  anchor: new google.maps.Point(0, 0) // anchor
};
var icon_partyneg = {
  url: "static/icons/c_partyneg.png", // url
  scaledSize: new google.maps.Size(40, 40), // scaled size
  origin: new google.maps.Point(0,0), // origin
  anchor: new google.maps.Point(0, 0) // anchor
};
var icon_trip = {
  url: "static/icons/c_tripneu.png", // url
  scaledSize: new google.maps.Size(40, 40), // scaled size
  origin: new google.maps.Point(0,0), // origin
  anchor: new google.maps.Point(0, 0) // anchor
};
var icon_trippos = {
  url: "static/icons/c_trippos.png", // url
  scaledSize: new google.maps.Size(40, 40), // scaled size
  origin: new google.maps.Point(0,0), // origin
  anchor: new google.maps.Point(0, 0) // anchor
};
var icon_tripneg = {
  url: "static/icons/c_tripneg.png", // url
  scaledSize: new google.maps.Size(40, 40), // scaled size
  origin: new google.maps.Point(0,0), // origin
  anchor: new google.maps.Point(0, 0) // anchor
};
  //var lowerbound = -1, upperbound = 1, posbound = 0.3, negbound = -0.3;
  for (var i=0;i<myData.length;i++){
    if (myData[i].tweettype == "concert") {
      //var lambda = 1;
      if (myData[i].sentiment == "negative") {
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_concertneg,
          animation: google.maps.Animation.DROP
        });
      }
      else if(myData[i].sentiment == "positive"){
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_concertpos,
          animation: google.maps.Animation.DROP
        });
      }
      else {
          var marker = new google.maps.Marker({
            position: myData[i].LatLng,
            map: map,
            title: myData[i].tweet,
            icon: icon_concert,
            animation: google.maps.Animation.DROP
          });
      }
    }
    else if (myData[i].tweettype == "party") {
      //var lambda = 1;
      if (myData[i].sentiment == "negative") {
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_partyneg,
          animation: google.maps.Animation.DROP
        });
      }
      else if(myData[i].sentiment == "positive"){
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_partypos,
          animation: google.maps.Animation.DROP
        });
      }
      else {
          var marker = new google.maps.Marker({
            position: myData[i].LatLng,
            map: map,
            title: myData[i].tweet,
            icon: icon_party,
            animation: google.maps.Animation.DROP
          });
      }
    }
    else if (myData[i].tweettype == "running") {
      //var lambda = 1;
      if (myData[i].sentiment == "negative") {
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_runneg,
          animation: google.maps.Animation.DROP
        });
      }
      else if(myData[i].sentiment == "positive"){
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_runpos,
          animation: google.maps.Animation.DROP
        });
      }
      else {
          var marker = new google.maps.Marker({
            position: myData[i].LatLng,
            map: map,
            title: myData[i].tweet,
            icon: icon_run,
            animation: google.maps.Animation.DROP
          });
      }
    }
    else if (myData[i].tweettype == "trip") {
      var lambda = 1;
      if (myData[i].sentiment == "negative") {
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_tripneg,
          animation: google.maps.Animation.DROP
        });
      }
      else if(myData[i].sentiment == "positive"){
        var marker = new google.maps.Marker({
          position: myData[i].LatLng,
          map: map,
          title: myData[i].tweet,
          icon: icon_trippos,
          animation: google.maps.Animation.DROP
        });
      }
      else {
          var marker = new google.maps.Marker({
            position: myData[i].LatLng,
            map: map,
            title: myData[i].tweet,
            icon: icon_trip,
            animation: google.maps.Animation.DROP
          });
      }
    }

    //marker.addListener('click', toggleBounce);
  }
  /*function toggleBounce() {
  if (marker.getAnimation() !== null) {
    marker.setAnimation(null);
  } else {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  }
}*/
}

/*
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 2,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    });
    $.when(getPoints()).then(function() {
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: points,
            map: map
        });
    });
}*/

function processPoints() {
  var result = new Array();
  var points = [{"_type":"party","_source":{"sentiment":{"type":"neutral"},"geo":{"coordinates":[-86.86604,35.92263],"type":"Point"},"user":"Legendary Kimbros","tweet":"Paul Kramer \u0026amp; Swing Street tonight at 6 followed by @musiccityroots after party at 9:30!… https://t.co/Orkv3LXEoU"}},{"_type":"running","_source":{"sentiment":{"type":"neutral"},"user":"Andrzej Brylka","geo":{"type":"Point","coordinates":[18.5298948,54.5534645]},"tweet":"I just finished running 0.86 km in 5m:40s with #Endomondo #endorphins https://t.co/79AnFXmdiM"}},{"_type":"running","_source":{"user":"うめずまさし@マラソンシーズンオフ","geo":{"type":"Point","coordinates":[135.1401742,34.7262479]},"tweet":"I was out running 5.53 km with #Endomondo #endorphins https://t.co/XXIOH2c9Jp","sentiment":{"type":"negative","score":"-0.241706"}}},{"_type":"concert","_source":{"user":"the girl can rap","geo":{"type":"Point","coordinates":[-79.39703374,43.64516982]},"tweet":"Don't miss out TONIGHT @samenightclub after the Rihanna concert 🎉 There will also be a concert… https://t.co/jpAYM0Y0kl","sentiment":{"type":"neutral"}}},{"_type":"party","_source":{"user":"Material Grrlz","tweet":"Calling allll 6-12th graders...don't miss this tonight's block party 6:30-8:30pm!!!! @ Shepherd… https://t.co/qHG6n0L2K9","sentiment":{"type":"positive","score":"0.210393"},"geo":{"coordinates":[-118.5633,34.2743],"type":"Point"}}},{"_type":"concert","_source":{"user":"Lynn S. Connaway","tweet":"Great concert with The Boss. @ Schottenstein Center, The Ohio State University https://t.co/m2YxJMUvgv","sentiment":{"type":"positive","score":"0.507311"},"geo":{"coordinates":[-84.16667435,39.7220636],"type":"Point"}}},{"_type":"concert","_source":{"sentiment":{"type":"positive","score":"0.303898"},"geo":{"coordinates":[8.5396694,47.3831786],"type":"Point"},"user":"Marco Studer","tweet":"neck deep was so awesome\n#neckdeep #poppunk #concert #zurich #werk21 #dynamo #music #live @… https://t.co/29kt7MiqOG"}},{"_type":"party","_source":{"sentiment":{"type":"negative","score":"-0.38482"},"geo":{"coordinates":[-78.64267,35.78551],"type":"Point"},"user":"madison milhous","tweet":"yesterday was her birthday but the party lasts forever @ Dads Have Rights Too https://t.co/YzaHSC4JK6"}},{"_type":"trip","_source":{"sentiment":{"score":"0.458807","type":"positive","mixed":"1"},"user":"Beth Palm","geo":{"type":"Point","coordinates":[-93.02463024,44.99099648]},"tweet":"Personal shopping trip! #socent #arcsvaluevillage (@ Arc's Value Village Thrift Store in Saint Paul, MN) https://t.co/e7yeNTN0PD"}},{"_type":"party","_source":{"geo":{"type":"Point","coordinates":[-118.5633,34.2743]},"user":"Material Grrlz","sentiment":{"score":"0.210393","type":"positive"},"tweet":"Calling allll 6-12th graders...don't miss this tonight's block party 6:30-8:30pm!!!! @ Shepherd… https://t.co/qHG6n0L2K9"}}]
  for (var i = 0 ; i < points.length; i++){
    var tmp = {
      tweettype: points[i]["_type"],
      sentiment: points[i]["_source"]["sentiment"]["type"],
      LatLng: {lat: points[i]["_source"]["geo"]["coordinates"][1], lng: points[i]["_source"]["geo"]["coordinates"][0]},
      tweet: points[i]["_source"]["tweet"]
    };
    result[i] = tmp;
  }

  return result;
}


// Heatmap data: 500 Points
function getPoints() {
    var deferred = $.Deferred();
    // ref: http://stackoverflow.com/questions/15360393/force-code-to-execute-after-another-method-finishes-executing

    /* data format: getJSON[geometry]*/
    $.getJSON('http://b31c4b03.ngrok.io/tweets/search.json', function(data) {
        points = [];
        /*console.log(data);
        $.each( data, function( key, val ) { // key == geo
            val.forEach(function(coord) {
                points.push(new google.maps.LatLng(coord['coordinates'][1], coord['coordinates'][0]));
            })
        });*/

        deferred.resolve();
    });
    return deferred;
}

//getPoints();
