<template>
    <div id="mapOL">
      Hi, i'm a map!
    </div>
</template>

<script>
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';

  export default {
    name: 'Map',
    data() {
      return {

      }
    },
    mounted() {
      let map = new Map({
        target: 'mapOL',
        layers: [
          new TileLayer({source: new OSM()})
        ],
        view: new View({
          center: [4419926.7147939987,5982300.236877314],
          zoom: 12
        })
      })
    }
  }
</script>

<style>
  #mapOL {
    height: 500px
  }
</style>
