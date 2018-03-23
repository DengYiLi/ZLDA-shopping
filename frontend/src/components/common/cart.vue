<template>
    <div>
        <IndexNav></IndexNav>
        <div class="container">
            <h1>购物车</h1>
            <br>
            <el-table
                    v-loading="loading"
                    element-loading-text="玩命加载中"
                    :data="cart"
                    border
                    style="width: 100%"
            >
                <el-table-column
                        label="商品ID"
                        width="200">
                    <template scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.goodsId }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="商品名称"
                        width="280">
                    <template scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.goodsName }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="商品价格"
                        width="200">
                    <template scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.goodsPrice * scope.row.goodsNum}}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="商品数量"
                        width="200">
                    <template scope="scope">
                        <span style="margin-left: 30px"><el-button size="small" @click="goodsNumR(scope.row.goodsId)"
                                                                   style="margin-right: 10px">-</el-button>{{scope.row.goodsNum}}<el-button
                                size="small" @click="goodsNumA(scope.row.goodsId)">+</el-button></span>
                    </template>
                </el-table-column>
            </el-table>
            <el-button type="primary" @click="deleteCart" style="margin-top: 50px">清空购物车</el-button>
            <el-button type="primary" @click="pay" style="margin-top: 50px">付款</el-button>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import IndexNav from '../../components/common/navbar.vue'
    export default{
        data(){
            return {
                cartForm: {
                    'goodsId': '',
                    'goodsName': '',
                    'goodsPrice': '',
                    'goodsNum': '',
                    'goodsPriceTotls': ''
                },
                loading: false,
                id: '',
                cart: []
            }
        },
        components: {
            'IndexNav': IndexNav
        },
        created: function () {
            this.getCart()
            this.openloading()
            console.log(this.cart)
        },
        methods: {
            getCart: function () {
                this.id = this.$store.state.userInfo.user
                const postData = {
                    userId: this.id
                }
                axios.post('/api/getorder', postData).then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.cart = response.cartList
                        this.cartForm.goodsID = this.cart.goodsId
                        this.cartForm.goodsName = this.cart.goodsName
                        this.cartForm.goodsPrice = parseInt(this.cart.goodsPrice)
                        this.cartForm.goodsNum = parseInt(this.cart.goodsNum)
                    }
                })
            },
            openloading() {
                this.loading = true;
                setTimeout(() => {
                    this.loading = false;
                }, 1000);
            },
            deleteCart(){
                const postData = {
                    userId: this.$store.state.userInfo.user
                }
                console.log(postData)
                axios.post('/api/deletecart', postData).then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.cartDelete()
                        this.cart = []
                    }
                })
                this.cart = []
            },
            goodsNumR(id){
                this.cart[id].goodsNum--
            },
            goodsNumA(){
                this.cart[0].goodsNum++
            },
            pay(){
                this.$router.push('/pay')
            },
            cartDelete: function () {
                this.$notify.success({
                    title: '成功',
                    message: '清空购物车成功',
                    offset: 100
                });
            }
        }
    }
</script>