import vue from '@vitejs/plugin-vue'

export default {
    base: './',
    plugins: [vue()],
    optimizeDeps: {
        include: ['schart.js']
    },
    server: {
        host: 'localhost',
        port: 3000, // 端口号
        open: false, // 是否打开新窗口
        strictPort: false, // 设为 true 时若端口已被占用则会直接退出，而不是尝试下一个可用端口
        https: false, // 是否开启https
    },
}