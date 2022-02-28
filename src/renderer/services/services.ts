import * as Vue from 'vue';

import { ChatService } from './chat-service';
import { injectContext } from '../util/inject-context';

export const services: Vue.Plugin = (app: Vue.App, ...options: any[]) => {
  const inject = injectContext(app);
  const services = {
    chatService: ChatService,
  };

  for (const key in services) {
    inject(key, new (services as any)[key](app));
    console.log(app);
  }
};
