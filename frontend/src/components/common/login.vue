<template>
    <div class="login">
        <el-card class="box-card">
            <div id="login">
                <h2 class="text-center">登录</h2>
                <el-form label-position="top" :model="loginForm" :rules="loginRules" ref="loginForm"
                         label-width="100px" class="demo-ruleForm">
                    <el-form-item label="用户名" prop="email">
                        <el-input v-model="loginForm.email"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="pass">
                        <el-input type="password" v-model="loginForm.pass" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div id="button">
                            <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
                            <router-link to="/register">
                                <el-button type="primary">注册</el-button>
                            </router-link>
                        </div>
                    </el-form-item>
                </el-form>
            </div>
        </el-card>
    </div>
</template>
<script>
    import axios from 'axios'
    import * as types from '../../store/types'
    import store from '../../store/store'
    export default {
        data() {
            var checkEmail = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入邮箱'))
                } else {
                    callback()
                }
            }
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'))
                } else {
                    callback()
                }
            };
            return {
                userinfo: [],
                token: "",
                loginForm: {
                    email: '',
                    pass: '',
                },
                loginRules: {
                    email: [
                        {validator: checkEmail, trigger: 'blur'}
                    ],
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
//                        const headers = Cookies.get('token')?{'Authorization': 'Token ' + Cookies.get('token')}:{},
                        const loginParam = {
                            username: this.loginForm.email,
                            password: this.loginForm.pass,
                        };
                        axios.post('/api/login', loginParam).then((response) => {
                            response = response.data
                            this.userInfo = response
                            this.token = response.token
                            if (response.code === 100) {
                                if (this.token) {
                                    this.$store.commit(types.LOGIN, this.token)
                                    this.$store.commit(types.USER, this.userInfo)
                                    if (this.userInfo.user_s === true) {
                                        this.$router.push('/admin')
                                        this.loginSuccess()
                                    }
                                    if (this.userInfo.user_s === false) {
                                        this.$router.push('/person')
                                        this.loginSuccess()
                                    }

//                                    let redirect = decodeURIComponent(this.$route.query.redirect || '/admin')
//                                    this.$router.push({
//                                        path:redirect
//                                    })
                                }
                            } else {
                                this.loginFail()
                            }
                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            loginSuccess: function () {
                this.$notify.success({
                    title: '成功',
                    message: '登录成功',
                    offset: 100
                });
            },
            loginFail: function () {
                this.$notify.error({
                    title: '失败',
                    message: '登录失败',
                    offset: 100
                });
            },
        },
        created: function () {
            if (this.$store.state.userInfo) {
                if (this.$store.state.userInfo.user_s === true) {
                    this.$router.push('/admin')
                }
                if (this.$store.state.userInfo.user_s === false) {
                    this.$router.push('/person')
                }

//                                    let redirect = decodeURIComponent(this.$route.query.redirect || '/admin')
//                                    this.$router.push({
//                                        path:redirect
//                                    })
            }
        },
        mounted(){
            this.$store.commit(types.TITLE, 'Login')
        }
    }
</script>
<style>

    h2 {
        color: #48576a;
    }

    .login {
        font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
        color: #48576a;
        position: relative;
        /*margin-top: 250px;*/
        margin-right: auto;
        margin-left: auto;
        top: 250px;
        width: 400px;
        height: 45%;
    }

    #login {
        margin: 10% auto;
        width: 300px;
    }

    .el-form-item__label {
        font-weight: 500;
        /*padding: 20px 12px 20px 0 !important;*/
    }

    .el-input {
        margin-top: 0 !important;
    }

    #button button {
        margin-left: 55px;
    }

    #button a {
        color: #fff !important;
    }
</style>