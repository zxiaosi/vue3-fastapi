import{p as U,J as d,C as _,K as f,L as n,T as r,V as z,au as B,P as N,c as T,z as G,D as v,E as m,u as h,R as g,S as P,av as X,aw as Y,U as D,a3 as C,G as I,Q as Z,ap as ee}from"./@vue.d04bd165.js";import{e as te}from"./echarts.ebd507a1.js";import{u as H,a as F,o as oe,c as se,b as ne}from"./vue-router.ce07e720.js";import{u as O,c as ae}from"./vuex.b3663e39.js";import{L as le,M as re,N as ie,O as ce,P as _e,Q as de}from"./@element-plus.a79a71de.js";import{i as ue,z as me}from"./element-plus.59a6f374.js";import"./tslib.34a40861.js";import"./zrender.7fbaf631.js";import"./@vueuse.23e01a3f.js";import"./lodash.5c7b62b5.js";import"./dayjs.a4bdb7c5.js";import"./@popperjs.7a88ba6a.js";import"./@ctrl.2e36ce53.js";import"./async-validator.5d25c98b.js";import"./memoize-one.4ee5c96d.js";import"./normalize-wheel-es.9a219a59.js";const pe=function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const o of document.querySelectorAll('link[rel="modulepreload"]'))a(o);new MutationObserver(o=>{for(const i of o)if(i.type==="childList")for(const c of i.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&a(c)}).observe(document,{childList:!0,subtree:!0});function e(o){const i={};return o.integrity&&(i.integrity=o.integrity),o.referrerpolicy&&(i.referrerPolicy=o.referrerpolicy),o.crossorigin==="use-credentials"?i.credentials="include":o.crossorigin==="anonymous"?i.credentials="omit":i.credentials="same-origin",i}function a(o){if(o.ep)return;o.ep=!0;const i=e(o);fetch(o.href,i)}};pe();const he={setup(t){return U("echart",te),(s,e)=>{const a=d("router-view");return _(),f(a,null,{default:n(({Component:o})=>[r(z,null,{default:n(()=>[(_(),f(B,null,[(_(),f(N(o)))],1024))]),_:2},1024)]),_:1})}}},fe="modulepreload",q={},ve="./",p=function(s,e){return!e||e.length===0?s():Promise.all(e.map(a=>{if(a=`${ve}${a}`,a in q)return;q[a]=!0;const o=a.endsWith(".css"),i=o?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${a}"]${i}`))return;const c=document.createElement("link");if(c.rel=o?"stylesheet":fe,o||(c.as="script",c.crossOrigin=""),c.href=a,document.head.appendChild(c),o)return new Promise((b,x)=>{c.addEventListener("load",b),c.addEventListener("error",x)})})).then(()=>s())};var ge="./assets/img.3f6b7d00.jpg";var K=(t,s)=>{const e=t.__vccOpts||t;for(const[a,o]of s)e[a]=o;return e};const M=t=>(X("data-v-2e010f1c"),t=t(),Y(),t),be={class:"header"},xe=M(()=>m("div",{class:"logo"},"\u5B66\u751F\u9009\u8BFE\u7CFB\u7EDF",-1)),ye={class:"header-right"},Ee={class:"header-user-con"},Le={class:"btn-bell"},je={key:0,class:"btn-bell-badge"},Te=M(()=>m("div",{class:"user-avator"},[m("img",{src:ge})],-1)),Pe={class:"el-dropdown-link"},ke={href:"https://github.com/zxiaosi/Vue3-FastAPI",target:"_blank"},we=g("\u9879\u76EE\u4ED3\u5E93"),De=g("\u4E2A\u4EBA\u4E2D\u5FC3"),Ce=g("\u9000\u51FA\u767B\u5F55"),Ie={setup(t,{expose:s}){const e=localStorage.getItem("ms_username"),a=2,o=O(),i=T(()=>o.state.collapse),c=()=>{o.commit("handleCollapse",!i.value)};G(()=>{document.body.clientWidth<1490&&c()});const b=H(),x=E=>{E=="loginout"?(localStorage.removeItem("ms_username"),b.push("/login")):E=="user"&&b.push("/user")};return s({username:e,message:a,handleCommand:x}),(E,k)=>{const L=d("el-icon"),w=d("router-link"),l=d("el-tooltip"),u=d("el-dropdown-item"),y=d("el-dropdown-menu"),j=d("el-dropdown");return _(),v("div",be,[m("div",{class:"collapse-btn",onClick:c},[h(i)?(_(),f(L,{key:1,size:20},{default:n(()=>[r(h(re))]),_:1})):(_(),f(L,{key:0,size:20},{default:n(()=>[r(h(le))]),_:1}))]),xe,m("div",ye,[m("div",Ee,[m("div",Le,[r(l,{effect:"dark",content:`\u6709${a}\u6761\u672A\u8BFB\u6D88\u606F`,placement:"bottom"},{default:n(()=>[r(w,{to:"/tabs"},{default:n(()=>[r(L,{size:20,color:"#409EFC"},{default:n(()=>[r(h(ie))]),_:1})]),_:1})]),_:1},8,["content"]),(_(),v("span",je))]),Te,r(j,{class:"user-name",trigger:"click",onCommand:x},{dropdown:n(()=>[r(y,null,{default:n(()=>[m("a",ke,[r(u,null,{default:n(()=>[we]),_:1})]),r(u,{command:"user"},{default:n(()=>[De]),_:1}),r(u,{divided:"",command:"loginout"},{default:n(()=>[Ce]),_:1})]),_:1})]),default:n(()=>[m("span",Pe,[g(P(h(e))+" ",1),r(L,{size:20},{default:n(()=>[r(h(ce))]),_:1})])]),_:1})])])])}}};var Oe=K(Ie,[["__scopeId","data-v-2e010f1c"]]);const $e={class:"sidebar"},Ae={setup(t,{expose:s}){const e=[{icon:"el-icon-ali-home",index:"/dashboard",title:"\u7CFB\u7EDF\u9996\u9875"},{icon:"el-icon-ali-cascades",index:"2",title:"\u4FE1\u606F\u8868\u683C",subs:[{index:"/department",title:"\u9662\u7CFB\u8868"},{index:"/major",title:"\u4E13\u4E1A\u8868"},{index:"/teacher",title:"\u6559\u5E08\u8868"},{index:"/student",title:"\u5B66\u751F\u8868"},{index:"/course",title:"\u8BFE\u7A0B\u8868"},{index:"/selectcourse",title:"\u9009\u8BFE\u8868"},{index:"/basetable",title:"\u57FA\u7840\u8868\u683C"}]},{icon:"el-icon-ali-copy",index:"/tabs",title:"tab\u9009\u9879\u5361"},{icon:"el-icon-ali-calendar",index:"3",title:"\u8868\u5355\u76F8\u5173",subs:[{index:"/baseform",title:"\u57FA\u672C\u8868\u5355"}]},{icon:"el-icon-ali-warn",index:"4",title:"\u9519\u8BEF\u5904\u7406",subs:[{index:"/permission",title:"\u6743\u9650\u6D4B\u8BD5"},{index:"/404",title:"404\u9875\u9762"}]},{icon:"el-icon-ali-test",index:"/test",title:"\u6D4B\u8BD5\u9875\u9762"}],a=F(),o=T(()=>a.path),i=O(),c=T(()=>i.state.collapse);return s({items:e,onRoutes:o,collapse:c}),(b,x)=>{const E=d("el-icon"),k=d("el-menu-item"),L=d("el-sub-menu"),w=d("el-menu");return _(),v("div",$e,[r(w,{class:"sidebar-el-menu","default-active":h(o),collapse:h(c),"background-color":"#324157","text-color":"#bfcbd9","active-text-color":"#20a0ff","unique-opened":"",router:""},{default:n(()=>[(_(),v(D,null,C(e,l=>(_(),v(D,null,[l.subs?(_(),f(L,{index:l.index,key:l.index},{title:n(()=>[r(E,{class:I(l.icon)},null,8,["class"]),m("span",null,P(l.title),1)]),default:n(()=>[(_(!0),v(D,null,C(l.subs,(u,y)=>(_(),v(D,null,[u.subs?(_(),f(L,{index:u.index,key:u.index},{title:n(()=>[g(P(u.title),1)]),default:n(()=>[(_(!0),v(D,null,C(u.subs,(j,A)=>(_(),f(k,{key:A,index:j.index},{default:n(()=>[g(P(j.title),1)]),_:2},1032,["index"]))),128))]),_:2},1032,["index"])):(_(),f(k,{index:u.index,key:y},{default:n(()=>[g(P(u.title),1)]),_:2},1032,["index"]))],64))),256))]),_:2},1032,["index"])):(_(),f(k,{index:l.index,key:l.index},{title:n(()=>[g(P(l.title),1)]),default:n(()=>[r(E,{class:I(l.icon)},null,8,["class"])]),_:2},1032,["index"]))],64))),64))]),_:1},8,["default-active","collapse"])])}}};var Re=K(Ae,[["__scopeId","data-v-5311bdac"]]);const Ve={key:0,class:"tags"},Se=["onClick"],ze={class:"tags-close-box"},Be=g(" \u6807\u7B7E\u9009\u9879 "),Ne=g("\u5173\u95ED\u5176\u4ED6"),He=g("\u5173\u95ED\u6240\u6709"),Fe={setup(t,{expose:s}){const e=F(),a=H(),o=l=>l===e.fullPath,i=O(),c=T(()=>i.state.tagsList),b=T(()=>c.value.length>0),x=l=>{const u=c.value[l];i.commit("delTagsItem",{index:l});const y=c.value[l]?c.value[l]:c.value[l-1];y?u.path===e.fullPath&&a.push(y.path):a.push("/")},E=l=>{c.value.some(y=>y.path===l.fullPath)||(c.value.length>=8&&i.commit("delTagsItem",{index:0}),i.commit("setTagsItem",{name:l.name,title:l.meta.title,path:l.fullPath}))};E(e),oe(l=>{E(l)});const k=()=>{i.commit("clearTags"),a.push("/")},L=()=>{const l=c.value.filter(u=>u.path===e.fullPath);i.commit("closeTagsOther",l)},w=l=>{l==="other"?L():k()};return s({isActive:o,showTags:b,closeTags:x,handleTags:w}),(l,u)=>{const y=d("router-link"),j=d("el-icon"),A=d("el-button"),V=d("el-dropdown-item"),J=d("el-dropdown-menu"),Q=d("el-dropdown");return h(b)?(_(),v("div",Ve,[m("ul",null,[(_(!0),v(D,null,C(h(c),(R,S)=>(_(),v("li",{class:I(["tags-li",{active:o(R.path)}]),key:S},[r(y,{to:R.path,class:"tags-li-title"},{default:n(()=>[g(P(R.title),1)]),_:2},1032,["to"]),m("span",{class:"tags-li-icon",onClick:Ue=>x(S)},[r(j,{color:"#606266"},{default:n(()=>[r(h(_e))]),_:1})],8,Se)],2))),128))]),m("div",ze,[r(Q,{onCommand:w},{dropdown:n(()=>[r(J,{size:"small"},{default:n(()=>[r(V,{command:"other"},{default:n(()=>[Ne]),_:1}),r(V,{command:"all"},{default:n(()=>[He]),_:1})]),_:1})]),default:n(()=>[r(A,{size:"small",type:"primary"},{default:n(()=>[Be,r(j,{class:"el-icon--right"},{default:n(()=>[r(h(de))]),_:1})]),_:1})]),_:1})])])):Z("",!0)}}},qe={class:"about"},Ke={class:"content"},Me={setup(t,{expose:s}){const e=O(),a=T(()=>e.state.tagsList.map(i=>i.name)),o=T(()=>e.state.collapse);return s({tagsList:a,collapse:o}),(i,c)=>{const b=d("router-view");return _(),v("div",qe,[r(Oe),r(Re),m("div",{class:I(["content-box",{"content-collapse":h(o)}])},[r(Fe),m("div",Ke,[r(b,null,{default:n(({Component:x})=>[r(z,{name:"move",mode:"out-in"},{default:n(()=>[(_(),f(B,{include:h(a)},[(_(),f(N(x)))],1032,["include"]))]),_:2},1024)]),_:1})])],2)])}}},We=[{path:"/",redirect:"/dashboard"},{path:"/",name:"Home",component:Me,children:[{path:"/dashboard",name:"dashboard",meta:{title:"\u7CFB\u7EDF\u9996\u9875"},component:()=>p(()=>import("./Dashboard.17c71d1f.js"),["assets/Dashboard.17c71d1f.js","assets/Dashboard.8e16e95e.css","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vue.d04bd165.js","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@element-plus.a79a71de.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vue-router.ce07e720.js","assets/vuex.b3663e39.js"])},{path:"/department",name:"department",meta:{title:"\u9662\u7CFB\u8868"},component:()=>p(()=>import("./Department.c964241e.js"),["assets/Department.c964241e.js","assets/vuex.b3663e39.js","assets/@vue.d04bd165.js","assets/BaseTable.72163d05.js","assets/BaseTable.8bf0c0f6.css","assets/vue-router.ce07e720.js","assets/Pagination.3bc4fbd5.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/department.838e7cde.js","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])},{path:"/major",name:"major",meta:{title:"\u4E13\u4E1A\u8868"},component:()=>p(()=>import("./Major.ed80081a.js"),["assets/Major.ed80081a.js","assets/Major.f55498b7.css","assets/vuex.b3663e39.js","assets/@vue.d04bd165.js","assets/BaseTable.72163d05.js","assets/BaseTable.8bf0c0f6.css","assets/vue-router.ce07e720.js","assets/Pagination.3bc4fbd5.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/major.73a67e6e.js","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/department.838e7cde.js","assets/byIdGetName.f3220ff3.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])},{path:"/teacher",name:"teacher",meta:{title:"\u6559\u5E08\u8868"},component:()=>p(()=>import("./Teacher.d0b7cf7e.js"),["assets/Teacher.d0b7cf7e.js","assets/Teacher.6c676281.css","assets/vuex.b3663e39.js","assets/@vue.d04bd165.js","assets/BaseTable.72163d05.js","assets/BaseTable.8bf0c0f6.css","assets/vue-router.ce07e720.js","assets/Pagination.3bc4fbd5.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/teacher.9a357213.js","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/department.838e7cde.js","assets/byIdGetName.f3220ff3.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])},{path:"/student",name:"student",meta:{title:"\u5B66\u751F\u8868"},component:()=>p(()=>import("./Student.bcf08e60.js"),["assets/Student.bcf08e60.js","assets/Student.77610185.css","assets/vuex.b3663e39.js","assets/@vue.d04bd165.js","assets/BaseTable.72163d05.js","assets/BaseTable.8bf0c0f6.css","assets/vue-router.ce07e720.js","assets/Pagination.3bc4fbd5.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/student.7d73a33a.js","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/major.73a67e6e.js","assets/byIdGetName.f3220ff3.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])},{path:"/course",name:"course",meta:{title:"\u8BFE\u7A0B\u8868"},component:()=>p(()=>import("./Course.e92ea86d.js"),["assets/Course.e92ea86d.js","assets/Course.80fdf3b4.css","assets/vuex.b3663e39.js","assets/@vue.d04bd165.js","assets/BaseTable.72163d05.js","assets/BaseTable.8bf0c0f6.css","assets/vue-router.ce07e720.js","assets/Pagination.3bc4fbd5.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/course.27eccbb8.js","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])},{path:"/selectcourse",name:"selectcourse",meta:{title:"\u9009\u8BFE\u8868"},component:()=>p(()=>import("./SelectCourse.c5aa4656.js"),["assets/SelectCourse.c5aa4656.js","assets/SelectCourse.107a6757.css","assets/@vue.d04bd165.js","assets/vuex.b3663e39.js","assets/BaseTable.72163d05.js","assets/BaseTable.8bf0c0f6.css","assets/vue-router.ce07e720.js","assets/Pagination.3bc4fbd5.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/http.b52ceb59.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/student.7d73a33a.js","assets/teacher.9a357213.js","assets/course.27eccbb8.js","assets/byIdGetName.f3220ff3.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])},{path:"/basetable",name:"basetable",meta:{title:"\u57FA\u7840\u8868\u683C"},component:()=>p(()=>import("./BaseTable.880c9b7a.js"),["assets/BaseTable.880c9b7a.js","assets/BaseTable.dc2b604c.css","assets/baseTable.20703755.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vue.d04bd165.js","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@element-plus.a79a71de.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vue-router.ce07e720.js","assets/vuex.b3663e39.js"])},{path:"/baseform",name:"baseform",meta:{title:"\u57FA\u672C\u8868\u5355"},component:()=>p(()=>import("./BaseForm.2b02df69.js"),["assets/BaseForm.2b02df69.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vue.d04bd165.js","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@element-plus.a79a71de.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vue-router.ce07e720.js","assets/vuex.b3663e39.js"])},{path:"/tabs",name:"tabs",meta:{title:"tab\u6807\u7B7E"},component:()=>p(()=>import("./Tabs.6a8677b3.js"),["assets/Tabs.6a8677b3.js","assets/Tabs.80382fa5.css","assets/@vue.d04bd165.js"])},{path:"/permission",name:"permission",meta:{title:"\u6743\u9650\u7BA1\u7406",permission:!0},component:()=>p(()=>import("./Permission.0970c0d9.js"),["assets/Permission.0970c0d9.js","assets/Permission.b62af482.css","assets/@vue.d04bd165.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vue-router.ce07e720.js","assets/vuex.b3663e39.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js"])},{path:"/404",name:"404",meta:{title:"\u627E\u4E0D\u5230\u9875\u9762"},component:()=>p(()=>import("./404.752fc9da.js"),["assets/404.752fc9da.js","assets/404.1ab6dc8f.css","assets/vue-router.ce07e720.js","assets/@vue.d04bd165.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vuex.b3663e39.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js"])},{path:"/403",name:"403",meta:{title:"\u6CA1\u6709\u6743\u9650"},component:()=>p(()=>import("./403.f8872829.js"),["assets/403.f8872829.js","assets/403.345ef6f9.css","assets/vue-router.ce07e720.js","assets/@vue.d04bd165.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vuex.b3663e39.js","assets/@element-plus.a79a71de.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js"])},{path:"/test",name:"test",meta:{title:"\u6D4B\u8BD5\u9875\u9762"},component:()=>p(()=>import("./Test.9d08f31b.js"),["assets/Test.9d08f31b.js","assets/Test.3ee78bb2.css","assets/Pagination.3bc4fbd5.js","assets/@vue.d04bd165.js","assets/baseTable.20703755.js","assets/request.441f8969.js","assets/axios.82d3905a.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@element-plus.a79a71de.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js","assets/vue-router.ce07e720.js","assets/vuex.b3663e39.js"])}]},{path:"/login",name:"Login",meta:{title:"\u767B\u5F55"},component:()=>p(()=>import("./Login.eb3f4a46.js"),["assets/Login.eb3f4a46.js","assets/Login.e27feeeb.css","assets/@vue.d04bd165.js","assets/vuex.b3663e39.js","assets/vue-router.ce07e720.js","assets/element-plus.59a6f374.js","assets/element-plus.54e24444.css","assets/@vueuse.23e01a3f.js","assets/lodash.5c7b62b5.js","assets/dayjs.a4bdb7c5.js","assets/@element-plus.a79a71de.js","assets/@popperjs.7a88ba6a.js","assets/@ctrl.2e36ce53.js","assets/async-validator.5d25c98b.js","assets/memoize-one.4ee5c96d.js","assets/normalize-wheel-es.9a219a59.js","assets/echarts.ebd507a1.js","assets/tslib.34a40861.js","assets/zrender.7fbaf631.js"])}],W=se({history:ne(),routes:We});W.beforeEach((t,s,e)=>{document.title=`${t.meta.title} | \u5B66\u751F\u9009\u8BFE\u7CFB\u7EDF`;const a=localStorage.getItem("ms_username");!a&&t.path!=="/login"?e("/login"):t.meta.permission?a==="admin"?e():e("/403"):e()});var Je=ae({state:{tagsList:[],collapse:!1,departmentData:[],majorData:[],teacherData:[],studentData:[],courseData:[],selectCourseData:[]},mutations:{delTagsItem(t,s){t.tagsList.splice(s.index,1)},setTagsItem(t,s){t.tagsList.push(s)},clearTags(t){t.tagsList=[]},closeTagsOther(t,s){t.tagsList=s},closeCurrentTag(t,s){for(let e=0,a=t.tagsList.length;e<a;e++)if(t.tagsList[e].path===s.$route.fullPath){e<a-1?s.$router.push(t.tagsList[e+1].path):e>0?s.$router.push(t.tagsList[e-1].path):s.$router.push("/"),t.tagsList.splice(e,1);break}},handleCollapse(t,s){t.collapse=s},handleData(t,s){const e=s[0]+"Data";t[e]=s[1]}},actions:{},modules:{}}),Qe=t=>{t.use(ue,{locale:me})};const $=ee(he);Qe($);$.config.errorHandler=()=>null;$.config.warnHandler=()=>null;$.use(Je).use(W).mount("#app");export{K as _,ge as a};