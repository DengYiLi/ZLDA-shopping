<template>
    <div>
        <h3>我的订单</h3>
        {{address.id}}
        <el-table :data="address"
                border
                style="width: 700px"
        >
            <el-table-column
                    label="订单号"
                    width="70">
                <template scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.id }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="收件人"
                    width="120">
                <template scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.userName }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="下单日期"
                    width="250">
                <template scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.date }}</span>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template scope="scope">
                    <el-button
                            type="primary"
                            size="small"
                            @click="handleEdit(scope.$index, scope.row)">查看订单
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog
                title="查看订单"
                :visible.sync="dialogVisible"
                size="small"
                >
            <el-table :data="cartList"
                      border
                      style="width: 800px"
            >
                <el-table-column
                        label="商品id"
                        width="240">
                    <template scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.goodsId }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="商品名"
                        width="350">
                    <template scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.goodsName }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="商品价格"
                        width="200">
                    <template scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.goodsPrice }}</span>
                    </template>
                </el-table-column>
            </el-table>
            <span slot="footer" class="dialog-footer">
    <el-button @click="cancel">取 消</el-button>
    <el-button type="primary" @click="logout">确 定</el-button>
  </span>
        </el-dialog>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        data(){
            return {
                cartForm: {
                    'goodsId': '',
                    'goodsName': '',
                    'goodsPrice': '',
                    'goodsNum': '',
                    'goodsPriceTotls': ''
                },
                dialogVisible:false,
                address:[],
                cartList:[],
                loading: false,
                id: '',
                cart: []
            }
        },
        created: function () {
            this.getOrder()
        },
        methods: {
            cancel(){
                this.dialogFormVisible = false
            },
            handleEdit(scopea, scope) {
                this.dialogVisible = true
            },
            openloading() {
                this.loading = true;
                setTimeout(() => {
                    this.loading = false;
                }, 10);
            },
            getOrder: function () {
                const userId = this.$store.state.userInfo.user
                const postData = {
                    userId: userId
                }
                axios.post('/api/getorder', postData).then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.address = response.address
                        this.cartList = response.cartList
                    }
                })
            }
        }
    }
</script>
<style>
    .el-table {
        background-color: #eef1f6 !important;
    }
</style>