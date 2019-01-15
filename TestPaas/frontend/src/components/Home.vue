<template id="contact">
  <div>
    <h1>Home</h1>
    <p>This is the tutorial about Contact.</p>
    <div>
    	<form type="backgrounp:#fffff">
    		<el-input  type="textarea"  autosize  placeholder="请输入内容"  v-model="textarea2"></el-input>
			<div style="margin: 20px 0;"></div>
				<el-input  type="textarea"  :autosize="{ minRows: 2, maxRows: 4}"  placeholder="请输入内容"  v-model="textarea3">
				</el-input>
		</form>
	<div class="block">
    	<span class="demonstration">设置默认时间</span>
    	<el-date-picker v-model="value3" type="datetime" placeholder="选择日期时间"  default-time="12:00:00" >
    	</el-date-picker>
	</div>
	</div>
</div>			
</template>

<script>
export default {
  '/hello': 'Hello',
  data() {
    return {
      textarea2: '',
      textarea3: ''
    }
}
}
</script>