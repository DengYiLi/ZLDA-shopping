<template>
    <div>
    <h1>about</h1>
    <div class="right">
        logout
    </div>
    </div>
</template>
<script>
    import * as types from '../../../store/types'
    import {mapState} from 'vuex'
    export default {
        name: 'app',
        data () {
            return {
                msg: 'Welcome to Your Vue.js App',
            }
        },
        computed: mapState({
            title: state => state.title,
            token: state => state.token
        }),
        methods: {
            logout(){
                this.$store.commit(types.LOGOUT)
                this.$router.push({
                    path: '/'
                })
            }
        }
    }
</script>