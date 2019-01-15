<template>
  <div id="app">
    <!-- <img src="./assets/fengxing.jpg"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
*{
  margin: 0;
}
#app {
  /*background-image: url(/static/fengxing.jpg);*/
  /*background-color: gray;*/
  /*background-repeat: no-repeat;*/
  /*background-size: all;*/
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  /*color: #2c3e50;*/
  /*float: top;*/
  /*height: 938px;*/
}
</style>
