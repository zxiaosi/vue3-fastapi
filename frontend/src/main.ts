import { createApp } from "vue";
import { createPinia } from "pinia"; // 状态管理

import App from "./App.vue";
import router from "./router"; // 路由

// 全局ElementPlus
import ElementPlus from "element-plus";
import zhCn from "element-plus/es/locale/lang/zh-cn"; // 中文
import "element-plus/dist/index.css"; // 样式文件
import "@/assets/css/icon.css"; // 阿里云图标

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(ElementPlus, { locale: zhCn });

app.mount("#app");
