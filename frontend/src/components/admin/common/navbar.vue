<template>
    <!--<el-menu theme="dark"  class="el-menu-demo" mode="horizontal"-->
    <!--@select="handleSelect">-->
    <!--<el-menu-item index="1" style="margin-right: 8%">管理中心</el-menu-item>-->
    <!--<div></div>-->
    <!--<div id="userStatus">-->
    <!--<el-submenu index="5">-->
    <!--<template slot="title">用户</template>-->
    <!--<el-menu-item index="5">修改信息</el-menu-item>-->
    <!--<el-menu-item index="5">注销登录</el-menu-item>-->
    <!--</el-submenu>-->
    <!--</div>-->
    <!--</el-menu>-->
    <div class="gutter">
        <el-row :gutter="15" style="
        height: 100%">
            <el-col :xs="8" :sm="6" :md="4" :lg="3" style="height: 100%;background-color: #324157">
                <el-menu default-active="home" theme="dark" router>
                    <el-menu-item index="home">
                        <i class="el-icon-menu"></i>首页
                    </el-menu-item>
                    <el-submenu index="1">
                        <template slot="title"><i class="el-icon-edit"></i>商品管理</template>
                        <el-menu-item index="goodsList">商品列表</el-menu-item>
                        <el-menu-item index="classList">品类列表</el-menu-item>
                    </el-submenu>
                    <el-submenu index="2">
                        <template slot="title"><i class="el-icon-edit"></i>订单管理</template>
                        <el-menu-item index="pendingOrder">待处理订单</el-menu-item>
                        <el-menu-item index="1-1">已完成订单</el-menu-item>
                    </el-submenu>
                    <el-menu-item index="add"><i class="el-icon-plus"></i>添加管理</el-menu-item>
                    <el-menu-item index="userList"><i class="el-icon-star-on"></i>用户管理</el-menu-item>
                    <el-menu-item index="about"><i class="el-icon-share"></i>关于</el-menu-item>
                    <el-menu-item index="logout"><i class="el-icon-share"></i>退出登录</el-menu-item>
                </el-menu>
            </el-col>
            <el-col :xs="16" :sm="18" :md="20" :lg="21">
                <router-view></router-view>
            </el-col>
        </el-row>
    </div>
</template>
<script>
    import * as types from '../../../store/types'
    import {mapState} from 'vuex'
    import store from '../../../store/store'

    export default {
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1'
            };
        },
        created:function () {
        },
        computed: mapState({
            title: state => state.title,
            token: state => state.token
        }),
        methods: {
            handleSelect(key, keyPath) {
            },
            logout(){
                this.$store.commit(types.LOGOUT)
                this.$router.push({
                    path: '/'
                })
            },
            handleOpen(key, keyPath) {
            },
            handleClose(key, keyPath) {
            }
        }
    }
</script>
<style>
    #app {
        height: 100%;
    }

    .gutter {
        height: 100%;
        padding-right: 7.5px;
    }

    #userStatus {
        float: right;
    }
</style>