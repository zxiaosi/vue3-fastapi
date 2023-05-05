<script setup lang='ts'>
import { API_URL } from "@/assets/js/global";
import { clearLocal } from "@/request/auth";
import { ElMessage, type UploadRawFile } from "element-plus";
import { ref } from "vue";


const apiUrl = API_URL + '/upload/'; // 上传地址

const isDisabled = ref(false); // 是否禁用上传

/** 上传图片之前回调 */
const beforeUpload = (rawFile: UploadRawFile) => {
  const isJPG = rawFile.type === "image/jpeg";
  const isPNG = rawFile.type === "image/png";
  const isLt2M = rawFile.size / 1024 / 1024 < 2;

  if (!isJPG && !isPNG) {
    ElMessage.error("上传头像图片只能是 JPG/PNG 格式!");
  }
  if (!isLt2M) {
    ElMessage.error("上传头像图片大小不能超过 2MB!");
  }
  return (isJPG || isPNG) && isLt2M;
};

/** 上传成功回调 */
const onSuccess = ({ code, data, msg }: any, file: any, fileList: any) => {
  console.log(code, data);
  if (code == 0) {
    isDisabled.value = true;
    ElMessage.warning(msg);
    setTimeout(() => { window.location.href = "/login" }, 2000);
    clearLocal();
  } else {
    ElMessage.error(msg);
  }
};

/** 上传失败回调 */
const onError = (err: any, file: any, fileList: any) => {
  console.log(err, file, fileList);
  // this.$message.error('上传失败');
};
</script>

<template>
  <el-upload class="upload" :with-credentials="true" :action="apiUrl" :show-file-list="false" :limit="1"
    :disabled="isDisabled" :before-upload="beforeUpload" @success="onSuccess" @error="onError">
    <el-button type="primary">点击上传头像</el-button>
  </el-upload>
</template>

<style scoped>
.upload {
  width: 100%;
  height: 100%;
  text-align: center;
  cursor: pointer;
  font-size: 14px;
}
</style>