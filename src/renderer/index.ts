import * as Vue from 'vue';
import { createStore } from 'vuex';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';
import Message from './models/message';

const store = createStore({
  state() {
    return {
      messages: [
        new Message(new Date(), 'Joe', 'Hey bob!'),
        new Message(new Date(), 'Bob', "Hey Joe, what's up?"),
        new Message(new Date(), 'Joe', 'Not much bro!'),
      ],
    };
  },
  mutations: {
    addMessage(state: any, message: Message) {
      state.messages.push(message);
    },
  },
  getters: {
    getMessages(state: any) {
      return state.messages;
    },
  },
});

const app = Vue.createApp(App);
app.use(store);
app.mount('#root');
