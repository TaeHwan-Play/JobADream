import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueFullPage from "vue-fullpage.js";
import vuetify from "./plugins/vuetify";
import './assets/css/global.css';

Vue.config.productionTip = false;
Vue.use(VueFullPage);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");