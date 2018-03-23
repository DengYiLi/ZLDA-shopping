<template>
    <div>
        <h2>商品添加</h2>
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="商品名称">
                <el-input v-model="form.goodsName"></el-input>
            </el-form-item>
            <el-form-item label="商品类别">
                <el-select v-model="form.goodsClass" :placeholder="this.form.goodsClass">
                    <el-option v-for="item in goodsClass" :key="item.goodsClassListsName"
                               :value="item.goodsClassListsName"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="商品价格">
                <el-input v-model="form.goodsPrice" style="width: 150px"></el-input>
            </el-form-item>
            <el-form-item label="商品介绍">
                <el-input type="textarea" v-model="form.desc"></el-input>
            </el-form-item>
            <el-form-item label="商品图片">
                <el-upload
                        action="/api/upload"
                        list-type="picture-card"
                        :on-preview="handlePictureCardPreview"
                        :on-remove="handleRemove">
                    <i class="el-icon-plus"></i>
                </el-upload>
                <el-dialog v-model="dialogVisibleImg" size="tiny">
                    <img width="100%" :src="dialogImageUrl" alt="">
                </el-dialog>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">立即创建</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>




    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                dialogImageUrl: '',
                dialogVisibleImg: false,
                formLabelWidth: '150px',
                goodsClass: '',
                form: {
                    goodsClass: '',
                    goodsName: '',
                    goodsPrice: '',
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
        methods: {
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            },
            onSubmit() {
                const postData = {
                    'goodsName':this.form.goodsName,
                    'goodsClass':this.form.goodsClass,
                    'goodsPrice':this.form.goodsPrice,
                    'goodsdesc':this.form.desc
                }
                axios.post('/api/addgoods',postData).then((response)=>{
                    response = response.data
                    if (response.status === '200'){
                        this.addSuccess()
                    }
                })
            },
            addSuccess: function () {
                this.$notify.success({
                    title: '成功',
                    message: '商品添加成功',
                    offset: 100
                });
            },
            getGoodsClass: function () {
                axios.get('/api/goodsclass').then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.goodsClass = response.goodsClassList
                    }
                })
            }
        },
        created: function () {
            this.getGoodsClass();
        },
    }
</script>
<style>
    input[type=file]{
        display: none !important;
    }
</style>