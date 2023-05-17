/// <reference types="vite/client" />

// 防止 App.vue 报错
declare module "*.vue" {
  import { defineComponent } from "vue";
  const Component: ReturnType<typeof defineComponent>;
  export default Component;
}

// 防止 ElementPlus 国际化报红
declare module "element-plus/dist/locale/zh-cn.mjs";
