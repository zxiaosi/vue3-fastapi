import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  // 用于开发环境
  base: './',

  // 根路径
  resolve: {
    alias: {
      '@': path.resolve(__dirname, "src"),
      "@api": path.resolve(__dirname, "src/api"),
      '@components': path.resolve(__dirname, "src/components"),
      '@plugins': path.resolve(__dirname, "src/plugins"),
      '@router': path.resolve(__dirname, "src/router"),
      '@store': path.resolve(__dirname, "src/store"),
      "@utils": path.resolve(__dirname, "src/utils"),
      '@views': path.resolve(__dirname, "src/views"),
    },
  },

  // 插件
  plugins: [vue()],

  // 服务器配置
  server: {
    host: 'localhost',
    port: 3000, // 端口号
    open: false, // 是否打开新窗口
    strictPort: false, // 设为 true 时若端口已被占用则会直接退出，而不是尝试下一个可用端口
    https: false, // 是否开启https
  },

  // 打包限制
  build: {
    chunkSizeWarningLimit: 1500,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {

            return id.toString().split('node_modules/')[1].split('/')[0].toString();
          }
        }
      }
    }
  },

  // 全局常量
  define: {
    // BASE_URL: JSON.stringify('http://127.0.0.1:8000/api/'),
    BASE_URL: JSON.stringify('http://8.136.82.204/api/'),
    TIMEOUT: 10000,
    TITLE: JSON.stringify('学生选课系统'),
  }
})
