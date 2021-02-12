
<html>
<head>
    <link rel="stylesheet" href="https://openlayers.org/en/v4.6.5/css/ol.css" type="text/css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.5.0/leaflet.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.5.0/leaflet-src.js"></script>
    <script src="https://openlayers.org/en/v4.6.5/build/ol.js" type="text/javascript"></script>
    <style>
    #map {
      height: 100%;
      width: 100%;
      z-index: 0;
    }
    </style>
</head>
<?php
  require('includes/header.php')
?>
<body>
    <div id="map"></div>
    <!-- JavaScript -->
    <script>
    const accessToken = 'asgmqjh6G8oFxgbfZSv004I37bv4s36i8qCLGHz2bEUdeQM8GxyCyP2e4WJQoMR8';
const map = L.map('map').setView([49.38173668148508, 1.0739455034193934], 12);
L.tileLayer(
    `https://tile.jawg.io/jawg-terrain/{z}/{x}/{y}.png?access-token=${accessToken}`, {
    attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank" class="jawg-attrib">&copy; <b>Jawg</b>Maps</a> | <a href="https://www.openstreetmap.org/copyright" title="OpenStreetMap is open data licensed under ODbL" target="_blank" class="osm-attrib">&copy; OSM contributors</a>',
    maxZoom: 10
}
).addTo(map);

// This add a marker with the default icon
L.marker([49.38173668148508, 1.0739455034193934]).addTo(map);
    </script>
</body>
</html>