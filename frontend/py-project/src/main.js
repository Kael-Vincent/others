// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import qs from 'qs'
import jsonify from 'jsonify'

// Vue.use(VueAxios, axios)
Vue.prototype.$axios=axios;
Vue.use(ElementUI)
Vue.config.productionTip = false


// axios.defaults.baseUrl="localhost:5000";
// Vue.prototype.HOST1="/signature";
Vue.prototype.HOST="/upload";
axios.interceptors.request.use(function (config) {
	if (config.method=="post") {
		config.data=jsonify.stringify(config.data);
	}
    // 在发送请求之前做些什么
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });

axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
  }, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
  });

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
