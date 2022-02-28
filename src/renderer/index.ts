import 'bootstrap/dist/css/bootstrap.css';

import * as Vue from 'vue';
import { createApp } from './util/createApp';
import App from './App.vue';

const app: Vue.App = createApp(App);
app.mount('#root');
