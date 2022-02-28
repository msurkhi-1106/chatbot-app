import * as Vue from 'vue';

export class Service {
  protected app: Vue.App;
  constructor(app: Vue.App) {
    this.app = app;
  }
}
