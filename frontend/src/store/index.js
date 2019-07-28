import Vue from 'vue'
import Vuex from 'vuex'
import { Part } from '../api/parts'
import {
  SET_PARTS
} from './mutation-types.js'
Vue.use(Vuex)
const state = {
  parts: []
}
const getters = {
  parts: state => state.parts
}

const mutations = {
  [SET_PARTS] (state, { parts }) {
    state.parts = parts
  }
}
// Действия
const actions = {
  getParts ({ commit }) {
    Part.list().then(parts => {
      commit(SET_PARTS, { parts })
    })
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
