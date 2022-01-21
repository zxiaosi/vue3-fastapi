import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import installElementPlus from './plugins/element'
import './assets/css/icon.css'

const app = createApp(App)
installElementPlus(app)
// 屏蔽错误信息
// app.config.errorHandler = () => null;
// 屏蔽警告信息
// app.config.warnHandler = () => null;
app
  .use(store)
  .use(router)
  .mount('#app')
