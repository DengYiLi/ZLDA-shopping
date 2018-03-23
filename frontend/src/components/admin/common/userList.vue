<template>
    <div>
        <h2>用户列表</h2>
        <el-table v-loading="loading" element-loading-text="拼命加载中" :data="userList" border style="width: 100%">
            <el-table-column label="用户ID" width="100">
                <template scope="scope">
                    <span style="margin-left: 10px">{{scope.row.userId}}</span>
                </template>
            </el-table-column>
            <el-table-column label="用户名称" width="180">
                <template scope="scope">
                    <span style="margin-left: 10px">{{scope.row.userName}}</span>
                </template>
            </el-table-column>
            <el-table-column label="用户类别" width="100">
                <template scope="scope">
                    <span style="margin-left: 10px">{{scope.row.userIsSuperuser}}</span>
                </template>
            </el-table-column>
            <el-table-column label="上次登录时间" width="300">
                <template scope="scope">
                    <span style="margin-left: 10px">{{scope.row.userLoginTime}}</span>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template scope="scope">
                    <el-button
                            size="small"
                            type="danger"
                            @click="handleDelete(scope.$index, scope.row)">删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog
                title="删除"
                :visible.sync="dialogVisibleDelete"
                size="tiny"
                :before-close="handleClose">
            <span>删除该用户</span>
            <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisibleDelete = false">取 消</el-button>
    <el-button type="primary" @click="deleteUser">确 定</el-button>
  </span>
        </el-dialog>
    </div>
</template>
<script>
    import axios from 'axios'
    export default{
        data(){
            return {
                loading: false,
                userList: [],
                dialogVisibleDelete: false,
                userId:'',
                form: {
                    userId: '',
                    userName: '',
                    userStatus: '',
                }
            }
        },
        created: function () {
            this.getUserList()
            this.openloading()
        },
        methods: {
            getUserList: function () {
                axios.get('/api/userlist').then((response) => {
                    response = response.data
                    if (response.status === '200') {
                        this.userList = response.userList
                    }
                })
            },
            handleDelete(index, row) {
                this.dialogVisibleDelete = true
                this.userId = row.userId
            },
            deleteUser: function () {
                const deleteUserId = {
                    userId: this.userId
                }
                axios.post('/api/deleteuser', deleteUserId).then((response) => {
                    response = response.data
                    if (response.status == '200') {
                        this.deleteSuccess()
                    } else {
                        this.deleteFailed()
                    }
                })
                this.dialogVisibleDelete = false
            },
            deleteSuccess: function () {
                this.$notify.success({
                    title: '成功',
                    message: '删除用户成功',
                    offset: 100
                });
            },
            deleteFailed: function () {
                this.$notify.success({
                    title: '成功',
                    message: '删除用户成功',
                    offset: 100
                });
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