import { ChatState } from 'renderer/store/modules/chat';
import * as Vue from 'vue';
import { Store } from 'vuex';
import { ChatService } from '../renderer/services/chat-service';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $chatService: ChatService;
  }

  interface App {
    $chatService: ChatService;
    $store: Store<ChatState>;
  }
}
