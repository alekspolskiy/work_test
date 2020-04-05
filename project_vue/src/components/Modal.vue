<template>
<div>
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">
  Add object
</button>

<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLongTitle">Add new object</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <input v-model='obj_type' type='text' placeholder='Тип объекта'/>
        <input v-model='description' type='text' placeholder='Описание'/>
        <br>
        <p>Select a type:
       <b> {{this.names.toString()}}</b>
        </p>
      </div>
      <div class="modal-footer">
        <button data-dismiss="modal">Close</button>
        <button @click="AddObject">Add</button>
      </div>
    </div>
  </div>
</div>
</div>

</template>

<script>
import axios from 'axios'
import {mapActions, mapGetters} from 'vuex'


	export default {
		data() {
      return {
        modal: false,
        obj_type: '',
        description: '',
        names: [],
      }
		},
		methods: {
		  AddObject(){
		      axios.post('http://127.0.0.1:8000/api/v1/app/objects/create/', {
		        description: this.description,
		        object_type: this.GetTypeIndex()
		      })
		      .catch (function (error){
            alert('not correct')
		      })
		  },

      GetTypeIndex(){
          return this.names.indexOf(this.obj_type)+1
        }

		},
		created(){
		  $.ajax({
			  url: 'http://127.0.0.1:8000/api/v1/app/object_types/all/',
				type: 'GET',
				success: (response) => {
					for (var i=0; i<response.length; i++){
					  this.names.push(response[i].name)
						}
					},
				})
		}
	}
</script>

<style scoped>
</style>
