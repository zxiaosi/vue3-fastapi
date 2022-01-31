import{_ as z}from"./index.f7cf4d0f.js";import{E as B}from"./element-plus.59a6f374.js";import{a as E,r as N,J as n,C as S,D as F,E as i,T as e,L as l,R as d}from"./@vue.d04bd165.js";import"./echarts.ebd507a1.js";import"./tslib.34a40861.js";import"./zrender.7fbaf631.js";import"./vue-router.ce07e720.js";import"./vuex.b3663e39.js";import"./@element-plus.a79a71de.js";import"./@vueuse.23e01a3f.js";import"./lodash.5c7b62b5.js";import"./dayjs.a4bdb7c5.js";import"./@popperjs.7a88ba6a.js";import"./@ctrl.2e36ce53.js";import"./async-validator.5d25c98b.js";import"./memoize-one.4ee5c96d.js";import"./normalize-wheel-es.9a219a59.js";const T={name:"baseform",setup(){const f=[{value:"guangdong",label:"\u5E7F\u4E1C\u7701",children:[{value:"guangzhou",label:"\u5E7F\u5DDE\u5E02",children:[{value:"tianhe",label:"\u5929\u6CB3\u533A"},{value:"haizhu",label:"\u6D77\u73E0\u533A"}]},{value:"dongguan",label:"\u4E1C\u839E\u5E02",children:[{value:"changan",label:"\u957F\u5B89\u9547"},{value:"humen",label:"\u864E\u95E8\u9547"}]}]},{value:"hunan",label:"\u6E56\u5357\u7701",children:[{value:"changsha",label:"\u957F\u6C99\u5E02",children:[{value:"yuelu",label:"\u5CB3\u9E93\u533A"}]}]}],a={name:[{required:!0,message:"\u8BF7\u8F93\u5165\u8868\u5355\u540D\u79F0",trigger:"blur"}]},m=E(null),o=N({name:"",region:"",date1:"",date2:"",delivery:!0,type:["\u6B65\u6B65\u9AD8"],resource:"\u5C0F\u5929\u624D",desc:"",options:[]});return{options:f,rules:a,formRef:m,form:o,onSubmit:()=>{m.value.validate(s=>{if(s)console.log(o),B.success("\u63D0\u4EA4\u6210\u529F\uFF01");else return!1})},onReset:()=>{m.value.resetFields()}}}},q={class:"crumbs"},D=i("i",{class:"el-icon-ali-calendar"},null,-1),J=d(" \u8868\u5355 "),L=d("\u57FA\u672C\u8868\u5355"),M={class:"container"},A={class:"form-box"},G=d("-"),H=d("\u8868\u5355\u63D0\u4EA4"),I=d("\u91CD\u7F6E\u8868\u5355");function K(f,a,m,o,V,y){const s=n("el-breadcrumb-item"),g=n("el-breadcrumb"),b=n("el-input"),r=n("el-form-item"),u=n("el-option"),h=n("el-select"),j=n("el-date-picker"),c=n("el-col"),k=n("el-time-picker"),x=n("el-cascader"),U=n("el-switch"),p=n("el-checkbox"),w=n("el-checkbox-group"),_=n("el-radio"),C=n("el-radio-group"),v=n("el-button"),R=n("el-form");return S(),F("div",null,[i("div",q,[e(g,{separator:"/"},{default:l(()=>[e(s,null,{default:l(()=>[D,J]),_:1}),e(s,null,{default:l(()=>[L]),_:1})]),_:1})]),i("div",M,[i("div",A,[e(R,{ref:"formRef",rules:o.rules,model:o.form,"label-width":"80px"},{default:l(()=>[e(r,{label:"\u8868\u5355\u540D\u79F0",prop:"name"},{default:l(()=>[e(b,{modelValue:o.form.name,"onUpdate:modelValue":a[0]||(a[0]=t=>o.form.name=t)},null,8,["modelValue"])]),_:1}),e(r,{label:"\u9009\u62E9\u5668",prop:"region"},{default:l(()=>[e(h,{modelValue:o.form.region,"onUpdate:modelValue":a[1]||(a[1]=t=>o.form.region=t),placeholder:"\u8BF7\u9009\u62E9"},{default:l(()=>[e(u,{key:"bbk",label:"\u6B65\u6B65\u9AD8",value:"bbk"}),e(u,{key:"xtc",label:"\u5C0F\u5929\u624D",value:"xtc"}),e(u,{key:"imoo",label:"imoo",value:"imoo"})]),_:1},8,["modelValue"])]),_:1}),e(r,{label:"\u65E5\u671F\u65F6\u95F4"},{default:l(()=>[e(c,{span:11},{default:l(()=>[e(r,{prop:"date1"},{default:l(()=>[e(j,{type:"date",placeholder:"\u9009\u62E9\u65E5\u671F",modelValue:o.form.date1,"onUpdate:modelValue":a[2]||(a[2]=t=>o.form.date1=t),style:{width:"100%"}},null,8,["modelValue"])]),_:1})]),_:1}),e(c,{class:"line",span:2},{default:l(()=>[G]),_:1}),e(c,{span:11},{default:l(()=>[e(r,{prop:"date2"},{default:l(()=>[e(k,{placeholder:"\u9009\u62E9\u65F6\u95F4",modelValue:o.form.date2,"onUpdate:modelValue":a[3]||(a[3]=t=>o.form.date2=t),style:{width:"100%"}},null,8,["modelValue"])]),_:1})]),_:1})]),_:1}),e(r,{label:"\u57CE\u5E02\u7EA7\u8054",prop:"options"},{default:l(()=>[e(x,{options:o.options,modelValue:o.form.options,"onUpdate:modelValue":a[4]||(a[4]=t=>o.form.options=t)},null,8,["options","modelValue"])]),_:1}),e(r,{label:"\u9009\u62E9\u5F00\u5173",prop:"delivery"},{default:l(()=>[e(U,{modelValue:o.form.delivery,"onUpdate:modelValue":a[5]||(a[5]=t=>o.form.delivery=t)},null,8,["modelValue"])]),_:1}),e(r,{label:"\u591A\u9009\u6846",prop:"type"},{default:l(()=>[e(w,{modelValue:o.form.type,"onUpdate:modelValue":a[6]||(a[6]=t=>o.form.type=t)},{default:l(()=>[e(p,{label:"\u6B65\u6B65\u9AD8",name:"type"}),e(p,{label:"\u5C0F\u5929\u624D",name:"type"}),e(p,{label:"imoo",name:"type"})]),_:1},8,["modelValue"])]),_:1}),e(r,{label:"\u5355\u9009\u6846",prop:"resource"},{default:l(()=>[e(C,{modelValue:o.form.resource,"onUpdate:modelValue":a[7]||(a[7]=t=>o.form.resource=t)},{default:l(()=>[e(_,{label:"\u6B65\u6B65\u9AD8"}),e(_,{label:"\u5C0F\u5929\u624D"}),e(_,{label:"imoo"})]),_:1},8,["modelValue"])]),_:1}),e(r,{label:"\u6587\u672C\u6846",prop:"desc"},{default:l(()=>[e(b,{type:"textarea",rows:"5",modelValue:o.form.desc,"onUpdate:modelValue":a[8]||(a[8]=t=>o.form.desc=t)},null,8,["modelValue"])]),_:1}),e(r,null,{default:l(()=>[e(v,{type:"primary",onClick:o.onSubmit},{default:l(()=>[H]),_:1},8,["onClick"]),e(v,{onClick:o.onReset},{default:l(()=>[I]),_:1},8,["onClick"])]),_:1})]),_:1},8,["rules","model"])])])])}var se=z(T,[["render",K]]);export{se as default};
