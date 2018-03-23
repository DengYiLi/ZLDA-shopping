<template>
    <div class="login">
        <el-card class="box-card">
            <div id="login">
                <h2 class="text-center">注册</h2>
                <el-form label-position="top" :model="registerForm" :rules="registerRules" ref="registerForm"
                         label-width="100px" class="demo-ruleForm">
                    <el-form-item label="用户名">
                        <el-input v-model="registerForm.username" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="邮箱" prop="email">
                        <el-input v-model="registerForm.email" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="pass">
                        <el-input type='password' v-model="registerForm.pass" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="checkPass">
                        <el-input type="password" v-model="registerForm.checkPass" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div id="button">
                            <el-button type="primary" @click="submitForm('registerForm')">注册</el-button>
                            <el-button type="primary" @click="resetForm('registerForm')">重置</el-button>
                        </div>
                    </el-form-item>


                </el-form>
            </div>
        </el-card>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        data() {
            var checkEmail = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入邮箱'))
                }
                else {
                    callback()
                }
            };
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                }
                if (value.length < 8) {
                    callback(new Error('密码不能少于8位'))
                }
                else {
                    if (this.registerForm.checkPass !== '') {
                        this.$refs.registerForm.validateField('checkPass');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.registerForm.pass) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                registerForm: {
                    username: '',
                    pass: '',
                    checkPass: '',
                    email: ''
                },
                registerRules: {
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {validator: validatePass2, trigger: 'blur'}
                    ],
                    email: [
                        {validator: checkEmail, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        const registerData = {
                            username: this.registerForm.username,
                            password: this.registerForm.pass,
                            email: this.registerForm.email
                        };
                        axios.post('api/register', registerData).then((response) => {
                            response = response.data
                            if (response.status === '200') {
                                this.registerSuccess()
                                this.$router.push('/login')
                            }
                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            registerSuccess: function () {
                this.$notify.success({
                    title: '成功',
                    message: '注册用户成功',
                    offset: 100
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
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
        top: 150px;
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