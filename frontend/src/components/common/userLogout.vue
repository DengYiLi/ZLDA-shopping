<template>
    <div>
        <el-dialog
                title="注销"
                :visible.sync="dialogVisible"
                size="tiny"
                :before-close="handleClose">
            <span>是否注销登录</span>
            <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="logout">确 定</el-button>
  </span>
        </el-dialog>
    </div>
</template>
<script>
    import * as types from '../../store/types'
    import {mapState} from 'vuex'
    export default{
        data(){
            return {
                dialogVisible:true
            }
        },
        computed: mapState({
            title: state => state.title,
            token: state => state.token
        }),
        methods:{
            logout:function () {
                this.$store.commit(types.LOGOUT)
                this.$router.push({
                    path: '/'
                })
            },
            handleClose(done) {
                this.$confirm('确认关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => {
                    });
            }
        }
    }
</script>