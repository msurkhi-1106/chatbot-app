import Message from 'renderer/models/message';
import { createStore as createStoreVuex } from 'vuex';

export const createStore = () => {
  return createStoreVuex({
    state() {
      return {
        messages: [],
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
};
