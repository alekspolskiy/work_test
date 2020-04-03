<template>

  <div v-if='getToken()== true'>
{{this.objects}}
    <div id="mapOL">

      Hi, i'm a map!

    </div>
    <div id="marker"></div>
    <div id="popup" class="ol-popup">
     <a href="#" id="popup-closer" class="ol-popup-closer"></a>
     <div id="popup-content"></div>
 </div>
 </div>
   </div>

</template>

<script>
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import Vector from 'ol/layer/Vector';
import Vector2 from 'ol/source/Vector';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import * as olProj from 'ol/proj';
import {fromLonLat, toLonLat} from 'ol/proj';
import Overlay from 'ol/Overlay'
import {toStringHDMS} from 'ol/coordinate';
import $ from 'jquery'




  export default {
    name: 'Map',
    data() {
      return {
        objects: '',
      }
    },

    methods: {
      getToken(){
        if (sessionStorage.getItem('auth_token')){
          return true
          }
        else{

          this.$router.push({name: "Home"})

        }

      },

    createMarker(x, y){
        var marker = new Vector({
          source: new Vector2({
            features: [
             new Feature({
                 geometry: new Point(fromLonLat([x, y]))
             })
         ]
     })
  });
  return marker
    },

    },
      created(){

        $.ajax({
          url: 'http://127.0.0.1:8000/api/v1/app/objects/detail/1',
          type: 'GET',
          success: (response) => {
              this.objects = response.description.toString()
              console.log(this.objects)

              return this.objects
          }
        })
    },


    mounted() {
     var layer = new TileLayer({
  source: new OSM()
});

var map = new Map({
  layers: [layer],
  target: 'mapOL',
  view: new View({
    center: fromLonLat([39.7232800, 47.2313500]),
    zoom: 12
  })
});

map.addLayer(this.createMarker(39.7232800, 47.2313500));
map.addLayer(this.createMarker(39.7344800, 47.2311600));


var popup = new Overlay({
  element: document.getElementById('popup')
});
map.addOverlay(popup);

var container = document.getElementById('popup');
 var content = document.getElementById('popup-content');
 var closer = document.getElementById('popup-closer');

  var overlay = new Overlay({
     element: container,
     autoPan: true,
     autoPanAnimation: {
         duration: 250
     }
 });
 map.addOverlay(overlay);
 closer.onclick = function() {
     overlay.setPosition(undefined);
     closer.blur();
     return false;
 };

map.on('click', function (event) {
     if (map.hasFeatureAtPixel(event.pixel) === true) {
         var coordinate = event.coordinate;

         content.innerHTML = '<b>Как сука????</b>';
         overlay.setPosition(coordinate);
     } else {
         overlay.setPosition(undefined);
         closer.blur();
     }
 });

    },

  }
</script>

<style>
  #mapOL {
    height: 500px
  }
   #marker {
        width: 20px;
        height: 20px;
        border: 1px solid #088;
        border-radius: 10px;
        background-color: #0FF;
        opacity: 0.5;
      }
      .popover-content {
        min-width: 180px;
      }
</style>
