import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";

// https://vitejs.dev/config/
// 自动导入 ElementPlus 图标 https://element-plus.org/zh-CN/component/icon.html#%E5%9F%BA%E7%A1%80%E7%94%A8%E6%B3%95
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    AutoImport({
      resolvers: [ElementPlusResolver()], // 自动导入 Element Plus 相关函数，如：ElMessage, ElMessageBox... (带样式)
    }),
    Components({
      resolvers: [ElementPlusResolver()], // 自动导入 Element Plus 组件
    }),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  css: {
    preprocessorOptions: {
      less: {
        math: "always", // 括号内才使用数学计算
      },
    },
  },
  server: {
    host: "127.0.0.1", // 请务必指定精确ip, 否则可能会Cookie无法写入 (这里localhost -> 127.0.0.1)
    strictPort: false, // 设为 true 时若端口已被占用则会直接退出，而不是尝试下一个可用端口
    https: false, // 是否启用 https
  },
});
