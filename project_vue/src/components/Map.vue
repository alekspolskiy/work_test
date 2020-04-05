<template>
  <div v-if='getToken()== true'>
    <div id="mapOL">
    </div>
    <div>
    <addModal></addModal>
    </div>
    <div id="marker" title="Marker"></div>
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
import {fromLonLat, toLonLat, transform} from 'ol/proj';
import Overlay from 'ol/Overlay'
import {toStringHDMS} from 'ol/coordinate';
import $ from 'jquery'
import Modal from '@/components/Modal'
import {mapActions, mapGetters} from 'vuex'
import {defaults as defaultControls, FullScreen} from 'ol/control'

  export default {
    name: 'Map',
    data() {
      return {
        mess: '',
        objects: ''
      }
    },
    components: {
      addModal: Modal
    },

    computed: {
      ...mapGetters([
        'OBJECTS'
      ]),
    },

    methods: {
     ...mapActions([
      'GET_OBJECTS_FROM_API'
     ]),

     changeMess(event) {
        this.mess = event.target.value
        this.$emit('messChange', this.mess)
      },

      getToken(){
        if (sessionStorage.getItem('auth_token')){
          return true
          }
        else{
          this.$router.push({name: "Home"})
        }
      },

     createFeature(description,coordinate_1 ,coordinate_2){
        var feature = new Feature({
        type: 'click',
        desc: description,
        geometry: new Point(fromLonLat([coordinate_1, coordinate_2]))
});
      return feature
     },

    createMarker(feature){
        var marker = new Vector({
        source: new Vector2({
        features: [feature]
    })
})
  return marker
    },

    },
      created(){
      				$.ajax({
					url: 'http://127.0.0.1:8000/api/v1/app/objects/all/',
					type: 'GET',

					success: (response) => {
            var descriptions = []
            var obj_type = []
						for (var i=0; i<response.length; i++){
						  descriptions.push(response[i].description)
						}
						for (var i=0; i<descriptions.length; i++){
            sessionStorage.setItem("desc" + [i].toString(), descriptions[i])
            }
            for (var i=0; i<response.length;i++){
              obj_type.push(response[i].object_type)
            }
            sessionStorage.setItem('obj_type', obj_type)
            sessionStorage.setItem('obj_type_len', obj_type.length)
					},
				}),
						$.ajax({
						url: 'http://127.0.0.1:8000/api/v1/app/object_types/all/',
					type: 'GET',
					success: (response) => {
            var names = []
						for (var i=0; i<response.length; i++){
						  names.push(response[i].name)
						}
						for (var i=0; i<names.length; i++){
            sessionStorage.setItem([i+1].toString(), names[i])
            console.log( [i+1].toString(), names[i])
            }
					},
				})
    },

    mounted() {
     var layer = new TileLayer({
  source: new OSM()
});

var map = new Map({
  controls: defaultControls().extend([
    new FullScreen()
  ]),
  layers: [layer],
  target: 'mapOL',
  view: new View({
    center: fromLonLat([39.7232800, 47.2313500]),
    zoom: 12
  })
});

var popup = new Overlay({
  element: document.getElementById('popup')
});
map.addOverlay(popup);

var container = document.getElementById('popup');
 var content = document.getElementById('popup-content');
 var closer = document.getElementById('popup-closer');

  var overlay = new Overlay({
     element: container
 });
 map.addOverlay(overlay);

var obj_type_len = sessionStorage.getItem('obj_type_len')
var desc = []
var obj_type = []
var obj_type_name = []
for (var i=0; i<sessionStorage.getItem('obj_type').length;i++){
  if (i%2 == 0){
    obj_type.push(sessionStorage.getItem('obj_type')[i])
  }
}

for (var i=0; i<obj_type_len;i++){
   desc.push(sessionStorage.getItem('desc' + [i].toString()))
}

for (var i=0; i<obj_type.length; i++){
  obj_type_name.push(sessionStorage.getItem('name' + obj_type[i].toString()))
}

var des = []
for (i=0;i<desc.length;i++){
var s = '<b>' + 'Описание объекта: ' + desc[i] + '<br>' + 'Тип объекта: ' + obj_type_name[i] + '<b>'
des.push(s)
}

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

for (var i=0; i<desc.length;i++){
  var cor_1 = getRandomArbitrary(39.7 ,39.76)
  var cor_2 = getRandomArbitrary(47.21 ,47.27)
  map.addLayer(this.createMarker(this.createFeature(des[i], cor_1, cor_2)))
}

closer.onclick = function() {
     overlay.setPosition(undefined);
     closer.blur();
     return false;
 };

 map.on('singleclick', function (event) {
     var f = map.forEachFeatureAtPixel(
        event.pixel,
        function(ft, layer){return ft;}
    );
     if (f && f.values_.type == 'click') {
         var coordinate = event.coordinate;
         content.innerHTML = f.values_.desc;
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


</style>
