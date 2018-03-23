<template>
    <div>
        <IndexNav></IndexNav>
        <div class="container">
            <el-row class="tac" style="height: 600px;background-color: #eef1f6">
                <el-col :span="8">
                    <el-menu default-active="1" class="el-menu-vertical-demo" router>
                        <el-menu-item index="personHome">
                            <i class="el-icon-menu"></i>个人中心
                        </el-menu-item>
                        <el-submenu index="1">
                            <template slot="title"><i class="el-icon-edit"></i>我的订单</template>
                            <el-menu-item index="ordered">已购买</el-menu-item>
                        </el-submenu>
                        <el-submenu index="2">
                            <template slot="title"><i class="el-icon-edit"></i>物流查询</template>
                            <el-menu-item index="express">我的物流</el-menu-item>
                        </el-submenu>
                        <el-menu-item index="userlogout"><i class="el-icon-share"></i>退出登录</el-menu-item>
                    </el-menu>
                </el-col>
            <router-view></router-view>
            </el-row>
            <div class="footer text-center">
                <div class="container">
                    <div class="row">
                        <!-- <div class="col-lg-2 col-sm-2">
                               <ul>
                                   <li style="list-style: none"><span>产品</span></li>
                               </ul>
                           </div>-->
                        <div class="col-lg-2 col-sm-2">
                            <ul>
                                <li style="list-style: none"><span>关于ZLDA</span></li>
                                <li style="list-style: none">了解ZLDA</li>
                                <li style="list-style: none">加入ZLDA</li>
                            </ul>
                        </div>
                        <div class="col-lg-2 col-sm-2">
                            <ul>
                                <li style="list-style: none"><span>服务支持</span></li>
                                <li style="list-style: none">技术支持</li>
                                <li style="list-style: none">售后服务</li>
                                <li style="list-style: none">自助服务</li>
                            </ul>
                        </div>
                        <div class="col-md-6 col-sm-6">
                            <h3>400-888-1111</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <NavFoot></NavFoot>
    </div>
</template>
<script>
    import axios from 'axios'
    import IndexNav from '../common/navbar.vue'
    import NavFoot from '../common/NavFoot.vue'
    import store from '../../store/store'
    export default{
        data(){
            return {
                userInfo:{}
            }
        },
        watch(){

        },
        components: {
            'IndexNav': IndexNav,
            'NavFoot': NavFoot
        },
        created:function () {
            this.userInfo = this.$store.state.userInfo
            console.log(this.$store.state.userInfo)
        },
        method: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>
<style>
    .el-col-8{
        width:20% !important;
    }
</style>