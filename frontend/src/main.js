import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Dropdown from 'vue-simple-search-dropdown'
import "node_modules/vuejs/dist/vue.min.js"
import "node_modules/vue-simple-search-dropdown/dist/vue-simple-search-dropdown.min.js"

// Install BootstrapVue
Vue.use(BootstrapVue)
Vue.use(Dropdown)

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  router,
}).$mount("#app");
