<template>
	<div>
		<el-form ref="form" :model="form">
			<el-form-item label="task">
				<el-input v-model="form.task">
				</el-input>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="onSubmit">submit</el-button>
			</el-form-item>
			
		</el-form>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				form:{
					task:""
				}
			}
		},
		methods:{
			onSubmit(){
				console.log(this.form);
				let url=this.HOST+"/todos";
				this.$axios.post(url,this.form,{ headers:{
					"Content-Type":"application/json"
				}})
				.then(res=>{
					console.log(res.data);
					this.task=res.data.task;
				})
				.catch(function(err){
					console.log(err);
				})
			}
		}
	}
</script>