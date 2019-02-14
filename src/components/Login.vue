<template>
  <div id="login" class="login-container">
    <el-form
      ref="loginForm"
      :model="loginForm"
      :rules="loginRules"
      class="login-form"
      autocomplete="on"
      label-position="left"
    >
      <div class="title-container">
        <h3 class="title">欢迎，请登录！</h3>
      </div>

      <el-form-item prop="username">
        <el-input
          v-model="loginForm.username"
          placeholder="用户名"
          name="username"
          type="text"
          autocomplete="on"
          @keyup.enter.native="handlerLogin"
        />
      </el-form-item>

      <el-form-item prop="password">
        <el-input
          v-model="loginForm.password"
          placeholder="密码"
          name="password"
          type="password"
          autocomplete="on"
          @keyup.enter.native="handlerLogin"
        />
      </el-form-item>

      <el-button class="thirdparty-button" type="primary" :loading="loading" @click="handlerLogin()">
        登录
      </el-button>

    </el-form>

  </div>
</template>

<script>
// 导入方法要用{}
import { isInputNull } from "../utils/validate.js";
import store from "../vuex/store.js";
import storage from "../model/storage.js";
import constantDict from "../model/constants.js";

export default {
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!isInputNull(value)) {
        callback(new Error("用户名不能为空！"));
      } else {
        callback();
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (!isInputNull(value)) {
        callback(new Error("密码不能为空！"));
      } else {
        callback();
      }
    };
    return {
      loading: false, //点击登录的时候显示加载中，默认设置为false
      // 这个是ref引用的数据
      loginForm: {
        username: "",
        password: ""
      },
      // 表单中的规则
      loginRules: {
        username: [
          { required: true, trigger: "blur", validator: validateUsername }
        ],
        password: [
          { required: true, trigger: "blur", validator: validatePassword }
        ]
      }
    };
  },
  store: store,
  methods: {
    // 处理登录的函数
    handlerLogin() {
      var url = constantDict.HOST + "login";
      var name = this.loginForm.username;
      var passwd = this.loginForm.password;

      if(!name){
        alert("请填写用户名！")
        return
      }
      if(!passwd){
        alert("请填写密码！")
        return
      }
      /**post 发送数据到后端，需要第三个参数 {emulateJSON:true}。

emulateJSON 的作用： 如果Web服务器无法处理编码为 application/json 的请求，你可以启用 emulateJSON 选项。 */

      // vue.http.headers={"Access-Control-Allow-Origin":false}
      this.$http
        .post(url, { username: name, password: passwd }, { emulateJSON: true })
        .then(
          response => {
            this.loading = true;
            // 请求成功跳转到主页面去
            var loginData = response.body;
            if (loginData.success == "true") {
              var token = loginData.data.token;
              // 保存一下token
              storage.set("token", token);
              // 跳转到主页去
              this.$router.push({ name: "home" });
            } else {
              alert(loginData.errmsg);
            }
            this.loading = false;
          },
          err => {
            console.log(err);
          }
        );
    },
    handlerEnterLogin(){
      console.log(123);
      
      this.handlerLogin();
    }
  }
};
</script>


<style lang="scss" scoped>
// $bg: #2d3a4b;
// $dark_gray: #889aa4;
$bg: #fff;
$dark_gray: #fff;
$light_gray: #111;
.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;
  .login-form {
    position: relative;
    width: 300px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }
  .title-container {
    position: relative;
    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }
  .thirdparty-button {
    position: relative;
    right: 45px;
    bottom: 6px;
    width: 30%;
    margin: 0px 50%;
  }
}
</style>
