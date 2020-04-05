import Vue from 'vue'
import Vuex from 'vuex'
import $ from 'jquery'
import axios from 'axios'

Vue.use(Vuex);

let store = new Vuex.Store({
  state: {
    objects: [],
    object_types: []
  },
  mutations: {
    SET_OBJECTS_TO_STATE: (state, objects) => {
      state.objects = objects;
    },
    SET_OBJECT_TYPES_TO_STATE: (state, object_types) => {
      state.object_types = object_types;
    },
  },
  actions: {
    GET_OBJECTS_FROM_API({commit}){
      return axios('http://127.0.0.1:8000/api/v1/app/objects/all/', {
        method: 'GET'
      })
      .then((objects) => {
        commit('SET_OBJECTS_TO_STATE', objects.data);
        return objects.data;
      })
      .catch((error) => {
        console.log(error)
        return error;
      })
    },
      GET_OBJECTS_TYPE_FROM_API({commit}){
      return axios('http://127.0.0.1:8000/api/v1/app/object_types/all/', {
        method: 'GET'
      })
      .then((object_types) => {
        commit('SET_OBJECT_TYPES_TO_STATE', object_types.data);
        return object_types;
      })
      .catch((error) => {
        console.log(error)
        return error;
      })
    }
  },
  getters: {
    OBJECTS(state){
      return state.objects;
    },
    OBJECT_TYPES(state){
      return state.object_types;
    },
  }
});

export default store;
