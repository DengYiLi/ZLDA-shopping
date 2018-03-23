<template>
    <div>
    <el-tag type="gray">{{userInfo.name}}</el-tag>
    <h3>登录成功</h3>
    </div>
</template>
<script>
    import axios from 'axios'
    import store from '../../store/store'
    export default{
        data(){
            return{
                userInfo:{}
            }
        },
        watch(){
        },
        components: {},
        created: function () {
            this.userInfo = this.$store.state.userInfo
        },
        method: {}
    }
</script>
<style>

</style>