<template>
    <div>
        <IndexNav></IndexNav>
        <div class="container">
            <h1>付款</h1>
            <div>
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="收货人">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>
                    <el-form-item label="手机">
                        <el-input v-model="form.phone" style="width: 400px"></el-input>
                    </el-form-item>
                    <el-form-item label="省份">
                        <el-select v-model="form.address" placeholder="请选择收货地址">
                            <el-option label="四川省" value="四川省"></el-option>
                            <el-option label="北京市" value="北京市"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="详细地址">
                        <el-input v-model="form.detailAddress"></el-input>
                    </el-form-item>
                    <el-form-item label="收货时间">
                        <el-col :span="11">
                            <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
                        </el-col>
                        <el-col class="line" :span="2">-</el-col>

                    </el-form-item>

                    <el-form-item label="邮政编码">
                        <el-input v-model="form.ems" style="width: 200px"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">立即付款</el-button>
                        <router-link to="/person"><el-button>取消</el-button></router-link>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import IndexNav from '../../components/common/navbar.vue'
    export default{
        data(){
            return {
                form: {
                    phone:'',
                    detailAddress:'',
                    ems:'',
                    address:'',
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                }
            }
        },
        components: {
            'IndexNav': IndexNav
        },
        methods: {
            onSubmit() {
                const postData = {
                    'userid':this.$store.state.userInfo.user,
                    'userName':this.form.name,
                    'address':this.form.address,
                    'detailAddress':this.form.detailAddress,
                    'date':this.form.date1,
                    'ems':this.form.ems,
                    'phone':this.form.phone
                }
                axios.post('/api/getems',postData).then((response)=>{
                    response = response.data
                    if (response.status === '200'){
                        this.paySuccess()
                        this.$router.push('/money')
                    }
                })
            },
            paySuccess: function () {
                this.$notify.success({
                    title: '成功',
                    message: '订单创建成功',
                    offset: 100
                });
            },
        }
    }
</script>