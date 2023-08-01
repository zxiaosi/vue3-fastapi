import { createApp } from "vue";
import { createPinia } from "pinia";
// import * as ElementPlusIconsVue from "@element-plus/icons-vue"; // ElementPlus 图标

import App from "./App.vue";
import router from "./router";

import "./assets/css/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
// for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
//   app.component(key, component);
// }

app.mount("#app");
