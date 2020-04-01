<template>
  <div>
        <h1>ROOM</h1>
      <ul>
        <li v-for="room in rooms">
          {{rooms.username}}
        </li>
      </ul>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Room',
    data() {
      return {
        rooms: '',
      }
    },
    created() {
     $.ajaxSetup({
      headers: {"Authorization": "Token " + sessionStorage.getItem('auth_token')},
     });
     this.loadRoom()
    },
    methods: {
      loadRoom(){
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/auth/users/",
          type: "GET",
          success: (response) => {
            this.rooms = response
            console.log(response)
          }
        })
      }
    }
    }

</script>

<style scoped>

</style>
