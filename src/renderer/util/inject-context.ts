import * as Vue from 'vue';

export const injectContext = (app: Vue.App) => (key: any, value: any) => {
  key = `$${key}`;
  app.mixin({
    beforeCreate() {
      this[key] = value;
    },
  });
  (app as any)[key] = value;
};
