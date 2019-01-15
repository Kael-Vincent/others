<template>
	<div id="repay">
		<el-form ref="form"  :model="form"  label="上传还款" :rules="rules">
			<el-form-item label="流水号" prop="serialNum">
				<el-input v-model="form.serialNum" type="number"  placeholder="请输流水编号" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="债务编号" >
				<el-input v-model="form.taskCode" type="number" placeholder="请输入债务编号" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="还款时间">
				<el-date-picker	v-model="form.refundTime" type="datetime"	placeholder="选择日期时间">
			</el-date-picker>
			</el-form-item>
			<el-form-item label="还款总额">
				<el-input  v-model="form.refundTotal" type="number" placeholder="请输入还款总额" class="label">
				</el-input>
			</el-form-item>
			<el-form-item  label="还款本金">
				<el-input v-model="form.refundPrincipal" type= "number" placeholder="请输入还款本金" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="还款利息">
				<el-input v-model="form.refundInterest" type="number" placeholder="请输入还款利息" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="还款违约金">
				<el-input v-model="form.refundCompensation" type="number" placeholder="请输入还款违约金" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="实际还款">
				<el-input v-model="form.actualRefundTotal" type="number" placeholder="请输入实际还款总额" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="手续费">
				<el-input v-model="form.refundPoundage" tpye="number" placeholder="请输入还款手续费" class="label">
				</el-input>
			</el-form-item>
			<el-form-item label="手续费违约金">
				<el-input v-model="form.refundPoundageCompensation" type="number" placeholder="请输入还款手续费违约金" class="label">
				</el-input>
			</el-form-item >
			<el-form-item label="债权方电话号码">
				<el-input v-model="form.creditorMobile" type="mobile" placeholder="请输入债权方电话" class="label" value="18510000002">
				</el-input>
			</el-form-item>
			<el-form-item label="还款方式">
				<el-radio-group v-model="form.refundWay" value="0" class="label">
					<el-radio border="true" label="0">线上还款</el-radio>
					<el-radio border="true" label="1">线下还款</el-radio>
				</el-radio-group>
			</el-form-item>
			<el-form-item>
				<el-button type="success" @click="onSubmit">立即创建</el-button>
				<el-button type="warning">取消</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default{
		name:"Repay",
		data(){
			return{
				form:{
					creditorMobile:'',
					serialNum:'',
					taskCode:'1',
					refundTime:'1',
					refundTotal:'1',
					refundPrincipal:'1',
					refundInterest:'1',
					refundCompensation:'1',
					actualRefundTotal:'1',
					refundPoundage:'1',
					refundPoundageCompensation:'1',
					refundWay:'0'
				}
			}
		},
		rules:{
			creditorMobile:[{
				required:true,trigger:'blur',message: '请输流水编号'
			}]
		},
		methods:{
			onSubmit(){
				var refundTime=Date.parse(this.form.refundTime);
				var timestamp = Date.parse(new Date());
				this.form['refundTime']=refundTime;
				// var url1 = this.HOST1+'/openapi/uploadRepayments?timestamp='+timestamp+'&version=1.0&app_key='+this.form.creditorMobile;
				let url = this.HOST+'/upload_repay';
				//获取还款签名
				this.$axios.post(url,{'repay':[this.form]},{headers:{
					'Content-Type':'application/json'
				}})
				.then(res1=>{
					console.log(res1.data);
					alert(res1.data.msg)
					// alert(res1.data.data);
					// // var url2=this.HOST2+'/openapi/uploadRepayments?timestamp='+timestamp+'&version=1.0&app_key='+this.form.creditorMobile;
					// let url2=this.HOST2+'/openapi/uploadRepayments?timestamp='+timestamp+'&version=1.0&app_key='+this.form.creditorMobile;
					// //上传还款
					// this.$axios.post(url2,["Repay":this.form],{
					// 	headers:{
					// 		'Content-Type':'application/json;charset=utf-8',
					// 		'signature':res1.data.data
					// 	}
					// }).then(res2=>{
					// 	console.log(res2.data.data);
					// })
					// .catch(err=>{
					// 	alert(err);
					// })
				})
				.catch(function(err){
					console.log(err);
				});
			}
		}
	}
</script>


<style scoped="scoped">
	 #repay{
	 	width: 400px;
	 	height:auto;
	 	text-align: center;
	 	margin-left: 35%;
	 	margin-top: 0 solid;
	 	padding-bottom: solid;
	 }
</style>