<template>
	<div>
		<el-form class="passwd"> 
			<p>注册</p>
			<el-form-item label="账号" >
				 <el-input type="number" placeholder="请输入手机号码"></el-input>
			</el-form-item>
			<el-form-item label="密码">
				<el-input type="password" placeholder="请输入6-18位密码"></el-input>
			</el-form-item>
			<el-form-item label="确认密码">
				<el-input type="password" placeholder="请输入6-18位密码"></el-input>
			</el-form-item>
			<el-form-item style="background-color: #eee">
				<el-button type="primary">
					<router-link to="login">注册</router-link><br>
					<router-link to="register/login">已有账号?去登陆<i class="el-icon-d-arrow-right"></i>
					</router-link>
				</el-button>
			</el-form-item>
			</el-form>
		</div>
</template>
<script>
	export default{
		'/Register':'Register'
	}
</script>
<style scoped>
	.passwd{
		margin: 0px auto;
		border: solid 1px;
		background-color: #ccc;	
		position: absolute;
		height: auto;
		width: 20%;
		top: 20%;
		left: 40%;
		border-radius: 5px;
		text-align: center;
	}
</style>