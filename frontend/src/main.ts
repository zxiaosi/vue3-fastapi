import { createApp } from "vue";
import { createPinia } from "pinia";
import ElementPlus from "element-plus"; // ElementPlus
import zhCn from "element-plus/dist/locale/zh-cn.mjs"; // ElementPlus 国际化
import * as ElementPlusIconsVue from "@element-plus/icons-vue"; // ElementPlus 图标

import App from "./App.vue";
import router from "./router";

import "./assets/css/main.css";
import "element-plus/dist/index.css"; // ElementPlus 样式

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(ElementPlus, { locale: zhCn });
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.mount("#app");
