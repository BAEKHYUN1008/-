<template>
  <div class="login-container">
    <el-card class="login-card">
      <h2>用户登录</h2>
      <el-form label-width="80px">
        <el-form-item label="账号">
          <el-input placeholder="请输入账号" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" placeholder="请输入密码" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" style="width: 100%">登录</el-button>
        </el-form-item>
        <el-form-item>
          <el-button link>还没有账号？立即注册</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f2f5;
}
.login-card {
  width: 400px;
}
h2 {
  text-align: center;
  margin-bottom: 30px;
}
</style>