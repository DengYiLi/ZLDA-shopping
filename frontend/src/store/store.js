/**
 * Created by alan on 6/18/17.
 */
import Vuex from 'vuex'
import Vue from 'vue'
import * as types from './types'

Vue.use(Vuex);
export default new Vuex.Store({
    state: {
        cart:[],
        userInfo:{},
        user: {},
        token: {},
        title: ''
    },
    mutations: {
        userInfo(state,data){
            state.userInfo = data
        },
        [types.CART]:(state,data) => {
            localStorage.cart = data
            state.cart = data
        },
        [types.LOGIN]: (state, data) => {
            localStorage.token = data;
            state.token = data;
        },
        [types.LOGOUT]: (state) => {
            localStorage.removeItem('token');
            state.token = null
        },
        [types.TITLE]: (state, data) => {
            state.title = data;
        },
        [types.USER]: (state, data) => {
            state.userInfo = data;
        }
    }
})