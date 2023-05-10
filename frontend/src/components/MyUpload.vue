<script setup lang="ts">
import { uploadImg } from "@/apis";
import { clearLocal, setLocal } from "@/request/auth";
import { useUserStore } from "@/stores";
import { ElMessage, type UploadFile, type UploadFiles, type UploadRequestOptions } from "element-plus";
import { ref } from "vue";

const userStore = useUserStore();

const isDisabled = ref(false); // 是否禁用上传

/** 上传图片之前回调 */
const beforeUpload = (rawFile: File) => {
  const isJPG = rawFile.type === "image/jpeg";
  const isPNG = rawFile.type === "image/png";
  const isLt2M = rawFile.size / 1024 / 1024 < 2;

  if (!((!isJPG && isPNG) || (!isPNG && isJPG))) {
    ElMessage.error("上传头像图片只能是 JPG/PNG 格式!");
    return false;
  }
  if (!isLt2M) {
    ElMessage.error("上传头像图片大小不能超过 2MB!");
    return false;
  }

  return (isJPG || isPNG) && isLt2M;
};

/** 自定义上传图片 */
const customUpload = async (options: UploadRequestOptions) => {
  // console.log(options);
  const formData = new FormData();
  formData.append("file", options.file);
  formData.append("filename", options.file.name);
  const resp = await uploadImg(formData);
  return resp;
};

/** 上传成功回调 */
const onSuccess = ({ data: { code, data, msg } }: any, uploadFile: UploadFile, uploadFiles: UploadFiles) => {
  // console.log(code, msg);
  if (code == 0) {
    isDisabled.value = true;
    // ElMessage.warning(msg);
    // setTimeout(() => {
    //   window.location.href = "/login";
    // }, 2000);
    // clearLocal();
    setLocal("userInfo", data);
    userStore.updateUser(data);
  } else {
    ElMessage.error(msg);
  }
};

/** 上传失败回调 */
const onError = (err: Error, uploadFile: UploadFile, uploadFiles: UploadFiles) => {
  console.log(err);
  ElMessage.error("上传失败");
};
</script>

<template>
  <el-upload
    class="upload"
    :show-file-list="false"
    :limit="1"
    :disabled="isDisabled"
    :before-upload="beforeUpload"
    :http-request="customUpload"
    @success="onSuccess"
    @error="onError"
  >
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