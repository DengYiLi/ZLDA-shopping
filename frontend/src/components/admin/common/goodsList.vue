<template>
    <div class="goodsList">
        <h2>商品列表</h2>
        <el-table
                v-loading="loading"
                element-loading-text="玩命加载中"
                :data="goodsList"
                border
                style="width: 100%">
            <!--<el-table-column-->
            <!--label="商品编号"-->
            <!--width="180">-->
            <!--<template scope="scope">-->
            <!--<span style="margin-left: 10px">{{ scope.row.goodsId }}</span>-->
            <!--</template>-->
            <!--</el-table-column>-->
            <el-table-column
                    label="商品名称"
                    width="280">
                <template scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.goodsName }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="商品类别"
                    width="180">
                <template scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.goodsClass }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="商品价格"
                    width="180">
                <template scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.goodsPrice }}</span>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template scope="scope">
                    <el-button
                            size="small"
                            @click="handleEdit(scope.$index, scope.row)">编辑
                    </el-button>
                    <el-button
                            size="small"
                            type="danger"
                            @click="handleDelete(scope.$index, scope.row)">删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="商品编辑" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="商品名称" :label-width="formLabelWidth">
                    <el-input v-model="form.goodsName" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="商品类别" :label-width="formLabelWidth">
                    <el-select v-model="form.goodsClass" :placeholder="this.form.goodsClass">
                        <el-option v-for="item in goodsClass" :key="item.goodsClassListsName"
                                   :value="item.goodsClassListsName"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="商品价格" :label-width="formLabelWidth">
                    <el-input v-model="form.goodsPrice" auto-complete="off"></el-input>
                </el-form-item>

            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitData">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog
                title="删除"
                :visible.sync="dialogVisibleDelete"
                size="tiny"
                :before-close="handleClose">
            <span>删除该商品</span>
            <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisibleDelete = false">取 消</el-button>
    <el-button type="primary" @click="DeleteData">确 定</el-button>
  </span>
        </el-dialog>
    </div>

</template>
<script>
    import axios from 'axios'
    //    import ElForm from "../../../../node_modules/element-ui/packages/form/src/form";
    //    import ElFormItem from "../../../../node_modules/element-ui/packages/form/src/form-item";
    //    import ElInput from "../../../../node_modules/element-ui/packages/input/src/input";
    export default{
        components: {
//            ElInput,
//            ElFormItem,
//            ElForm
        },
        data() {
            return {
                dialogImageUrl: '',
                dialogVisible: false,
                dialogVisibleDelete: false,
                loading: false,
                formLabelWidth: '150px',
                dialogTableVisible: false,
                dialogFormVisible: false,
                goodsClass: [],
                goodsList: [],

                form: {
                    id: '',
                    region: '',
                    goodsName: '',
                    goodsClass: '',
                    goodsPrice: '',
                    goodsIntro: ''
                }
            }
        },
        created: function () {
            this.getGoodsList();
            this.getGoodsClass();
            this.openloading()
        },
        methods: {
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            },
            getGoodsList: function () {
                axios.get('/api/goodsList').then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.goodsList = response.goodsList
                    }
                })
            },
            getGoodsClass: function () {
                axios.get('/api/goodsclass').then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.goodsClass = response.goodsClassList
                    }
                })
            },
            DeleteData: function () {
                this.dialogVisibleDelete = false
                const deleteGoodsData = {
                    goodsId: this.form.goodsId
                };
                axios.post('/api/deletegoods', deleteGoodsData).then((response = null) => {
                    response = response.data
                    if (response.status === '200') {
                        this.updateSuccess()
                    } else {
                        this.updateFail()
                    }
                })
            },
            submitData: function () {
                const newGoodsData = {
                    goodsId: this.form.id,
                    goodsName: this.form.goodsName,
                    goodsClass: this.form.goodsClass,
                    goodsPrice: this.form.goodsPrice
                }
                this.dialogFormVisible = false
                axios.post('/api/updategoods', newGoodsData).then((response = null) => {
                    response = response.data
                    if (response.status === '200') {
                        this.updateSuccess()
                    } else {
                        this.updateFail()
                    }
                })

            },
            updateSuccess: function () {
                this.$notify.success({
                    title: '成功',
                    message: '商品信息更新成功',
                    offset: 100
                });
            },
            updateFail: function () {
                this.$notify.error({
                    title: '更新失败',
                    message: '商品信息更新失败',
                    offset: 100
                });
            },
            handleEdit(index, row) {
                this.getSelectItemData(index, row)
            },
            deleteSelectItemData(index, row){
                this.dialogVisibleDelete = true
                this.form.goodsId = row.goodsIdf
            },
            handleDelete(index, row) {
                this.deleteSelectItemData(index, row)
            },
            getSelectItemData(index, row){
                this.dialogFormVisible = true
                this.form.id = row.goodsId
                this.form.goodsName = row.goodsName
                this.form.goodsClass = row.goodsClass
                this.form.goodsPrice = row.goodsPrice
                this.form.goodsIntro = row.goodsIntro
            },
            openloading() {
                this.loading = true;
                setTimeout(() => {
                    this.loading = false;
                }, 1000);
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
<style>
    .goodsList {
        margin-top: 25px;
    }
</style>