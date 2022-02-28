import * as Vue from 'vue';
import { createStore } from 'renderer/util/createStore';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';

const app = Vue.createApp(App);
const store = createStore();
app.use(store);
app.mount('#root');
