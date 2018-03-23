<template>
    <div>
        <IndexNav></IndexNav>
        <div class="container">
            <img v-bind:src="goodsIntro.goodsImg">
            <div class="introduce" style="float: right;margin-top: 120px;margin-right: 100px">
                <h3>{{goodsIntro.goodsName}}</h3>
                <h3>售价:{{goodsIntro.goodsPrice}}</h3>
                <el-tag type="gray">{{goodsIntro.goodsClass}}</el-tag>
                <br>
                <div class="buyButton">
                    <el-button>加入购物车</el-button>
                    <el-button>购买</el-button>
                </div>
            </div>
            <div class="introduce_content">
                <h1>asdsd</h1>
            </div>

        </div>
        <NavFoot></NavFoot>
    </div>
</template>
<script>
    import axios from 'axios'
    import IndexNav from '../common/navbar.vue'
    import NavFoot from '../common/NavFoot.vue'
    export default{
        data(){
            return {
                goodsIntro: [],
                params: '',
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
            this.getGoodsPage()
            this.getGoodsIntro()
        },
        methods: {
            getGoodsPage: function () {
                this.params = this.$route.params.goodsId
            },
            getGoodsIntro: function () {
                const goodsData = {
                    params: this.params
                };
                axios.post('/api/goodsintro', goodsData).then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.goodsIntro = response.goodsList
                    }
                })
            }
        }
    }
</script>
<style>
    .buyButton {
        margin-top: 20px;
    }
</style>