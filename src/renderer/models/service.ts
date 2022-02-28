import * as Vue from 'vue';
import { Store } from 'vuex';

export abstract class Service {
  protected app: Vue.App;

  constructor(app: Vue.App) {
    this.app = app;
  }

  get store() {
    return this.app.$store;
  }
  set store(store: Store<any>) {
    this.app.$store = store;
  }
}
