<template>



<div id="map" style="width: 100%; height: 400px;"></div>


</template>

<script>
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';

    var map = new ol.Map({
      target: 'map'
    });
    var osmLayer = new ol.layer.Tile({
      source: new ol.source.OSM()
    });
    map.addLayer(osmLayer);
    var view = new ol.View({
      center: [ 4188426.7147939987, 7508764.236877314 ],
      zoom: 12
    });
    map.setView(view);
  	export default {
		name: 'Map',
		}
</script>
<style scoped>
</style>
