<template scope="scope">
	<div id="login">
		<el-form class="passwd" :model="form"> 
			<p>登陆</p>
			<el-form-item label="账号" >
				 <el-input type="number"  v-model="form.account" auto-complete="off"></el-input>
			</el-form-item>
			<el-form-item label="密码">
				<el-input v-model="form.password" type="password" auto-complete="off"></el-input>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="onSubmit">登陆</el-button>			
				<el-button type="primary" >
					没有账号?去注册<i class="el-icon-d-arrow-right"></i>
				</el-button>
			</el-form-item>
			</el-form>
			<div>
				<p>{{description}}</p>
				<!-- <div v-for="task in tasks">
					<p>{{task.title}}</p>
					<p>{{task.description}}</p>
				</div> -->
			</div>
		</div>
</template>
<script>
	export default{
		name:'login',
		data(){
			return {
				form:{
					account:'',
					password:'',
				},
				movies:[],				
				tasks:[],
				description:''
			}
		},
		methods:{
			onSubmit(){
				// this.$axios.post('localhost:5000/data',this.form)
				// .then(function(res){
				// 	console.log(res);
				// })
				// .catch(function(err){
				// 	console.log(err);
				// })
				let url=this.HOST+"/get_tasks";
				this.$axios.get(url)
					// ,{
				// 	params:{
				// 		count:10,
				// 		start:0
				// 	}
				// })
				.then(res=>{
					console.log(res.data.tasks[0].title);
					// var finalTasks = [];
					// for(var i=0;i<res.data.tasks.length;i++){
					// 	var tasksObj = {
					// 		title:res.data.tasks[i].title,
					// 		description:res.data.tasks.description
					// 	}
					// 	finalTasks.push(tasksObj);
					// }
					// this.tasks=finalTasks;
					// this.filterData(res.data);
					this.description=res.data.tasks[0].description
				})
				.catch(err=>{
					console.log(err);
				})
				
			}
		}
	}
			
</script>
<style scoped="scoped">
	#login{
		height:500px;
	}
	.passwd{
		margin: 0px auto;
		border: solid 1px;
		background-color: #ccc;
		position: absolute;
		height: 800;
		width: auto;
		top: 20%;
		left: 40%;
		border-radius: 5px;
		text-align: center;
	}
</style>