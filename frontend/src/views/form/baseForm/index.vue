<script setup lang="ts">
import { reactive, ref } from "vue";
import { ElForm, ElMessage } from "element-plus";
import type { formDataType, addressType } from ".";

// 参考: https://element-plus.gitee.io/zh-CN/component/form.html#form-%E8%A1%A8%E5%8D%95

// 实例化表单
type FormInstance = InstanceType<typeof ElForm>;
const formRef = ref<FormInstance>();

// 校验规则
const formRules = {
  name: [{ required: true, message: "请输入表单名称", trigger: "blur" }],
};

// 表单数据
const formData: formDataType = reactive({
  name: "", // 表单名称
  selectData: "", // 选择器
  datePicker: "", // 日期选择器
  timePicker: "", // 时间选择器
  switchData: true, // 选择开关
  checkbox: ["步步高"], // 多选框
  radio: "小天才", // 单选框
  textarea: "", // 文本框
  address: [], // 地址
});

// 地址
const address: addressType[] = [
  {
    value: "guangdong",
    label: "广东省",
    children: [
      {
        value: "guangzhou",
        label: "广州市",
        children: [
          { value: "tianhe", label: "天河区" },
          { value: "haizhu", label: "海珠区" },
        ],
      },
      {
        value: "dongguan",
        label: "东莞市",
        children: [
          { value: "changan", label: "长安镇" },
          { value: "humen", label: "虎门镇" },
        ],
      },
    ],
  },
  {
    value: "hunan",
    label: "湖南省",
    children: [
      {
        value: "changsha",
        label: "长沙市",
        children: [{ value: "yuelu", label: "岳麓区" }],
      },
    ],
  },
];

/**
 * 提交表单
 */
const onSubmit = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid: any) => {
    if (valid) {
      ElMessage.success("提交成功！");
    } else {
      ElMessage.warning("验证失败");
      return false;
    }
  });
};

/**
 * 重置表单
 */
const onReset = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
};
</script>

<template>
  <div>
    <!-- 头部(面包屑) -->
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-ali-calendar" />
          <span>&nbsp;表单</span>
        </el-breadcrumb-item>
        <el-breadcrumb-item>基本表单</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <!-- 表单 -->
    <div class="container">
      <div class="form-box">
        <el-form ref="formRef" :rules="formRules" :model="formData" label-width="80px">
          <el-form-item label="表单名称" prop="name">
            <el-input v-model="formData.name" />
          </el-form-item>

          <el-form-item label="选择器" prop="selectData">
            <el-select v-model="formData.selectData" placeholder="请选择">
              <el-option key="bbk" label="步步高" value="bbk" />
              <el-option key="xtc" label="小天才" value="xtc" />
              <el-option key="imoo" label="imoo" value="imoo" />
            </el-select>
          </el-form-item>

          <el-form-item label="日期时间">
            <el-col :span="11">
              <el-form-item prop="datePicker">
                <el-date-picker type="date" placeholder="选择日期" v-model="formData.datePicker" style="width: 100%" />
              </el-form-item>
            </el-col>

            <el-col class="line" :span="2">-</el-col>

            <el-col :span="11">
              <el-form-item prop="timePicker">
                <el-time-picker placeholder="选择时间" v-model="formData.timePicker" style="width: 100%" />
              </el-form-item>
            </el-col>
          </el-form-item>

          <el-form-item label="城市级联" prop="address">
            <el-cascader :options="address" v-model="formData.address" />
          </el-form-item>

          <el-form-item label="选择开关" prop="switchData">
            <el-switch v-model="formData.switchData" />
          </el-form-item>

          <el-form-item label="多选框" prop="checkbox">
            <el-checkbox-group v-model="formData.checkbox">
              <el-checkbox label="步步高" name="type" />
              <el-checkbox label="小天才" name="type" />
              <el-checkbox label="imoo" name="type" />
            </el-checkbox-group>
          </el-form-item>

          <el-form-item label="单选框" prop="radio">
            <el-radio-group v-model="formData.radio">
              <el-radio label="步步高" />
              <el-radio label="小天才" />
              <el-radio label="imoo" />
            </el-radio-group>
          </el-form-item>

          <el-form-item label="文本框" prop="textarea">
            <el-input type="textarea" rows="5" v-model="formData.textarea" @keyup.enter="onSubmit(formRef)" />
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="onSubmit(formRef)">表单提交</el-button>
            <el-button @click="onReset(formRef)">重置表单</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
