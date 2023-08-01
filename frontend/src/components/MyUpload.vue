<script setup lang="ts">
import { uploadImg } from "@/apis";
import { clearLocal, setLocal } from "@/request/auth";
import { useUserStore } from "@/stores";
import type { UploadFile, UploadFiles, UploadRequestOptions } from "element-plus";
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
    setLocal("userInfo", data);
    userStore.updateUser(data);

    setTimeout(() => {
      isDisabled.value = false;
    }, 60 * 1000);
  } else {
    ElMessage.error(msg);
  }
};

/** 上传失败回调 */
const onError = (err: Error, uploadFile: UploadFile, uploadFiles: UploadFiles) => {
  console.log(err);
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
    <el-button type="primary">
      <div v-if="!isDisabled">点击上传头像</div>
      <el-countdown v-else title="" format="HH:mm:ss" :value="Date.now() + 60 * 1000" value-style="color: #fff" />
    </el-button>
  </el-upload>
</template>

<style scoped lang="less">
.upload {
  width: 100%;
  height: 100%;
  color: #fff;
  text-align: center;
  cursor: pointer;
  font-size: 14px;
}
</style>
