import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import VuePapaParse from 'vue-papa-parse'
import Vue, { createApp } from '@vue/compat';
import App from './App.vue'
import './assets/main.scss'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';


export const eventBus = new Vue();

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

const app = createApp(App)
app.use(VuePapaParse)
app.mount('#app')
