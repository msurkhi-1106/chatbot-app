import { ChatState, ChatModule } from './modules/chat';
import { createStore as createStoreVuex } from 'vuex';

const modules = {
  chat: ChatModule,
};

export const createStore = () => {
  return createStoreVuex<ChatState>({
    modules,
  });
};
