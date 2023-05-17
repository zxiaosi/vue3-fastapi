# frontend

## 安装依赖

```sh
npm install
npm run dev
npm run build
```

### 关于自定义组件的样式问题

- 方案一: 使用 `:deep()` 深度选择器包一下, <font color="red">缺点: 会导致样式全局污染</font>

  ```css
  :deep(.el-table__header) {
    background-color: #f5f5f5;
  }
  ```

- 方案二: 使用 `less/scss` 的模块化, <font color="red">缺点: 要分离文件</font>

  ```css
  .dot {
    width: 10px;
    height: 10px;
    background-color: red;
  }
  ```

  ```vue
  <script setup lang="tsx">
  import styles from "./index.module.less";
  </script>

  <template>
    <div class="{styles.dot}"></div>
  </template>
  ```
