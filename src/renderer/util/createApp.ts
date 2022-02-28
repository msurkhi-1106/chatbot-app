import * as Vue from 'vue';
import { createStore } from './createStore';
import { services } from '../services/services';
import { injectContext } from './inject-context';

export const createApp: Vue.CreateAppFunction<Element> = (
  rootComponent,
  rootProps
): Vue.App => {
  const app = Vue.createApp(rootComponent, rootProps);
  const inject = injectContext(app);

  // Setup vuex
  const store = createStore();
  app.use(store);
  inject('store', store);

  // Setup services
  app.use(services);

  return app;
};
