<template>
    <div>
        <IndexNav></IndexNav>
        <div class="classcontent">
            <div class="class-content">
                <div class="classbar">
                    <div class="container">
                        <div class="col-md-2"></div>
                        <div class="classbar-nav-icon col-md-8">
                            <ul>
                                <li class="col-md-2">
                                    <a href="#">
                                        <i class="classbar-icons classbar-icons-phone"
                                           style="">
                                        </i>
                                        <p>Phone</p>
                                    </a>
                                </li>
                                <li class="col-md-2">
                                    <a href="#">
                                        <i class="classbar-icons classbar-icons-audio"
                                           style=""></i>
                                        <p>Audio</p>
                                    </a>
                                </li>
                                <li class="col-md-2">
                                    <a href="#">
                                        <i class="classbar-icons classbar-icons-cases"
                                           style=""></i>
                                        <p>Cases</p>
                                    </a>
                                </li>
                                <li class="col-md-2">
                                    <a href="#">
                                        <i class="classbar-icons classbar-icons-home"
                                           style="">
                                        </i>
                                        <p>Home</p>
                                    </a>
                                </li>
                                <li class="col-md-2">
                                    <a href="#">
                                        <i class="classbar-icons classbar-icons-table"
                                           style="">
                                        </i>
                                        <p>Table</p>
                                    </a>
                                </li>
                                <li class="col-md-2">
                                    <a href="#">
                                        <i class="classbar-icons classbar-icons-chromebook"
                                           style="">
                                        </i>
                                        <p>Chrome</p>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="col-md-2"></div>
                    </div>
                    <div class="store">
                        <div class="container">
                            <div class="col-md-3 col-sm-4 col-xs-12" v-for="item in goodsClassPageList">
                                <div class="goods-list text-center">
                                    <router-link :to="{  name: 'goods',  params: { goodsId: item.goodsId }}">
                                        <img class="img-responsive" v-bind:src="item.goodsImg" alt="">
                                    </router-link>
                                    <span>{{item.goodsName}}</span>
                                    <br>
                                    <div style="margin-top: 15px">
                                        <span><el-tag type="gray">售价 ¥{{item.goodsPrice}}</el-tag></span>
                                        <span>||</span>
                                        <el-button size="small" @click='cart(item)'>加入购物车</el-button>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="service-top"></div>
                    <div class="service">
                        <div class="container">
                            <ul>
                                <li class="text-center">
                                    <i class="service-icons" style="background-position: 0 -80px"></i>
                                    <p>1小时售后派单响应</p>
                                </li>
                                <li class="text-center">
                                    <i class="service-icons" style="background-position: 0 -240px"></i>
                                    <p>7天无理由退货</p>
                                </li>
                                <li class="text-center">
                                    <i class="service-icons" style="background-position: 0 0px"></i>
                                    <p>15天退货保障</p>
                                </li>
                                <li class="text-center">
                                    <i class="service-icons" style="background-position: 0 -160px"></i>
                                    <p>30天换货保障</p>
                                </li>
                            </ul>
                            <div class="service-bottom"></div>
                        </div>
                    </div>
                </div>
            </div>
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
    import * as types from '../../store/types'
    import store from '../../store/store'
    import IndexNav from '../common/navbar.vue'
    import NavFoot from '../common/NavFoot.vue'
    export default {
        name: 'shop-list',
        data() {
            return {
                id: '',
                price: '',
                goodsClassPageList: [],
                activeIndex: '1',
                activeIndex2: '1',
            }
        },
        watch: {
            '$route' (route) {
                this.getGoodsClassPageList()
            }
        },
        components: {
            'IndexNav': IndexNav,
            'NavFoot': NavFoot
        },
        created: function () {
            this.getGoodsClassPageList()
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath)
            },
            getGoodsClassPageList: function () {
                const params = this.$route.params.userId
                axios.post('/api/class' + params).then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.goodsClassPageList = response.goodsClassPageList
                    }
                })
            },
            cart: function (item) {
                if (this.$store.state.userInfo.user) {
                    var userId = this.$store.state.userInfo.user
                    var cart = {
                        userId:userId,
                        goodsId: item.goodsId,
                        goodsPrice: item.goodsPrice
                    }
                    axios.post('/api/cart',cart).then((response) => {
                        response = response.data
                        if (response.status === '200'){
                            this.cartSuccess()
                        }
                    })
                }else{
                    alert('请先登录')
                    this.$router.push('/login')
                }
            },
            cartSuccess:function () {
                this.$notify.success({
                    title: '成功',
                    message: '加入购物车成功',
                    offset: 100
                });
            }
        },
    }
</script>
