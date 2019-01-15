<template>
  <div >
    <div class="head">
      <head>
        <img src="/static/little_panda2.jpg">
      </head>
    </div>
    <div class="lay">
      <div class="d1" >
      </div>
      <div class="d2">
        <img src="/static/little_panda2.jpg" sizes="100px*100px">
      </div>
      <div class="d3"></div>
  </div>
  </div>
</template>
<script>
  export default{
    name:'home'
  }
</script>

<style scoped>
  .head{
    margin-top: 0;
    /*background-color: black;*/
    /*background-image: url(/static/little_panda2.jpg);*/
    height: 180px;
    width: 1900px;
    /*position: fixed;
    top: 0;*/
    margin-bottom: 10px;
    border-radius: 10px;
  }
  .lay{
    margin: 150px;
  }
  .d1{
    margin-top: 70px;
    background-color: #7FFFD4;
    margin-top: 2% ;
    margin-left: 2.5%;
    width: 20%;
    height: 900px;
    border-radius: 10px;  
    display: inline-block;
  }
  .d2{
     margin-top: 70px;
    background-color: #7FFFD4;
    margin-top: 2% ;
    margin-left: 2.5%;
    width: 50%;
    height: 900px;
    border-radius: 10px;
    display:inline-block;
  }
  .d3{
    margin-top: 70px;
    background-color: #7FFFD4;
    margin-top: 2% ;
    margin-left: 2.5%;
    width: 20%;
    height: 900px;
    border-radius: 10px;
    display:inline-block;
  }
</style>