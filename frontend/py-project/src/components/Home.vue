<template scope="scope"> 
	<div id="home">
		<h2 style="font-size: xx-large;color: #000">易回测试平台</h2>
		<el-menu mode="horizontal" class="menu" style="margin: 10px 10px; font-size: 10px" background-color="#545c64" text-color="#ffd04b"  active-text-color="#ffd04b">
			<el-submenu index="1">
				<template slot="title">上传数据</template>
				<el-menu-item index="2-1" @click="onSubmit">选项1</el-menu-item>
				<el-menu-item index="2-2">选项2</el-menu-item>
				<el-menu-item index="2-3">选项3</el-menu-item>
			</el-submenu>
			<el-submenu index="2">
				<template slot="title">接口测试</template>
				<el-menu-item index="2-1">选项1</el-menu-item>
				<el-menu-item index="2-2">选项2</el-menu-item>
				<el-menu-item index="2-3">选项3</el-menu-item>
			</el-submenu>
		</el-menu>
		<el-container>
			<el-main>
				<div>
					<repay v-show="noShow"></repay>
				</div>
			</el-main>
		</el-container>
	</div>
</template>
<script >
	import repay from '@/components/Repay'
	export default{
		name:'Home',
		data(){
			// 
			return {noShow:false}
		},
		components:{
			repay
		},
		methods:{
			onSubmit(){
					this.noShow=!this.noShow;
				}
			}
		}
</script>
<!-- <style scoped="scoped">
	#home{
		text-align: center;
		position: absolute;
		margin: 0 1px;
		margin-top: 0;
		margin-left: 40%;
	}
</style> -->