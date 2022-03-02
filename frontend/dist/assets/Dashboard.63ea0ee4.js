import{_ as S,g as U,a as $,b as j,u as M,c as O}from"./index.46b49780.js";import{d as P,Q,R,g as Y,S as G,r as l,o as H,h as J,k as e,w as t,i as o,t as r,j as n,x as p,T as K,U as W,V as X,B as Z,s as ee,v as te}from"./vendor.3998f262.js";const d=g=>(ee("data-v-23d07705"),g=g(),te(),g),oe={class:"body"},ae={class:"user-info"},se=d(()=>o("img",{src:O,class:"user-avator"},null,-1)),ue={class:"user-info-cont"},le={class:"user-info-name"},ne={class:"user-info-list"},de=p(" \u5F53\u524D\u767B\u5F55\u65F6\u95F4\uFF1A"),ie=d(()=>o("div",{class:"user-info-list"},[p("\u5F53\u524D\u767B\u5F55\u5730\u70B9\uFF1A"),o("span",null,"\u6D4B\u8BD5\u5730\u70B9")],-1)),ce=d(()=>o("div",{class:"clearfix"},[o("span",null,"\u8BED\u8A00\u4F7F\u7528\u8BE6\u60C5")],-1)),re={class:"grid-content grid-con-1"},_e=d(()=>o("div",{class:"grid-cont-right"},[o("div",{class:"grid-num"},"1234"),o("div",null,"\u7528\u6237\u8BBF\u95EE\u91CF")],-1)),pe={class:"grid-content grid-con-2"},me={class:"grid-cont-right"},ge={class:"grid-num"},he=d(()=>o("div",null,"\u5F85\u529E\u4E8B\u9879",-1)),fe={class:"grid-content grid-con-3"},ve={class:"grid-cont-right"},Be={class:"grid-num"},Fe=d(()=>o("div",null,"\u8BF7\u6C42\u6B21\u6570",-1)),be={class:"clearfix"},xe=d(()=>o("span",null,"\u5F85\u529E\u4E8B\u9879",-1)),Ee=p("\u6DFB\u52A0"),we=d(()=>o("div",{id:"pie",style:{height:"220px"}},null,-1)),ye=d(()=>o("div",{id:"bar",style:{height:"220px"}},null,-1)),De={class:"dialog-footer"},Ce=p("\u53D6 \u6D88"),Ve=p("\u6DFB \u52A0"),Te=P({setup(g){let F=Q("echarts");const b=U("username"),w=b==="admin"?"\u8D85\u7EA7\u7BA1\u7406\u5458":"\u666E\u901A\u7528\u6237",s=R({currentTime:"",requestNumber:0,languageDetails:[],todoList:[],todoNumber:0,todoText:""});Y(()=>{var a=new Date;s.currentTime=a.getFullYear()+"\u5E74"+(a.getMonth()+1)+"\u6708"+a.getDate()+"\u65E5",y()});const y=async()=>{let{data:a}=await $();s.requestNumber=a.request_num,s.todoList=a.todo.list,s.todoNumber=a.todo.num,s.languageDetails=a.language,T(),A()},m=G(!1),D=async()=>{let{data:a}=await j({title:s.todoText});s.todoList=a.todo_list,s.todoNumber=a.todo_num,m.value=!1,s.todoText=""},C=async a=>{await M({id:a})},V=()=>{m.value=!1,s.todoText=""},T=()=>{let a=F.init(document.getElementById("pie"));a.setOption({title:{text:"\u4FE1\u606F",left:"center",top:"center"},legend:{orient:"vertical",left:"left",data:["\u7528\u6237\u8BBF\u95EE\u91CF","\u5F85\u529E\u4E8B\u9879","\u8BF7\u6C42\u6B21\u6570"]},tooltip:{trigger:"item",formatter:"{b} : {c} ({d}%)"},series:[{type:"pie",radius:["40%","70%"],data:[{value:335,name:"\u7528\u6237\u8BBF\u95EE\u91CF"},{value:s.todoNumber,name:"\u5F85\u529E\u4E8B\u9879"},{value:s.requestNumber,name:"\u8BF7\u6C42\u6B21\u6570"}]}]}),window.onresize=function(){a.resize()}},A=()=>{let a=F.init(document.getElementById("bar"));a.setOption({title:{text:"\u5468\u8FDB\u5EA6",left:"center"},legend:{show:!0},tooltip:{trigger:"item",formatter:"{b} : {c}"},xAxis:{data:["\u5468\u4E00","\u5468\u4E8C","\u5468\u4E09","\u5468\u56DB","\u5468\u4E94","\u5468\u516D","\u5468\u65E5"]},yAxis:{},series:[{type:"bar",data:[23,24,18,25,27,28,25]}]}),window.onresize=function(){a.resize()}};return(a,_)=>{const i=l("el-card"),h=l("el-table-column"),N=l("el-progress"),x=l("el-table"),c=l("el-col"),f=l("el-icon"),v=l("el-row"),B=l("el-button"),k=l("el-checkbox"),I=l("el-input"),q=l("el-form-item"),z=l("el-form"),L=l("el-dialog");return H(),J("div",oe,[e(v,{gutter:20},{default:t(()=>[e(c,{span:8},{default:t(()=>[e(i,{class:"mgb20",style:{height:"252px"}},{default:t(()=>[o("div",ae,[se,o("div",ue,[o("div",le,r(n(b)),1),o("div",null,r(n(w)),1)])]),o("div",ne,[de,o("span",null,r(n(s).currentTime),1)]),ie]),_:1}),e(i,{style:{height:"250px"}},{header:t(()=>[ce]),default:t(()=>[e(x,{"show-header":!1,data:n(s).languageDetails,class:"language"},{default:t(()=>[e(h,{width:"100"},{default:t(u=>[p(r(u.row.title),1)]),_:1}),e(h,{style:{width:"calc(100% - 140px)"}},{default:t(u=>[e(N,{percentage:u.row.percentage,color:u.row.color},null,8,["percentage","color"])]),_:1})]),_:1},8,["data"])]),_:1})]),_:1}),e(c,{span:16},{default:t(()=>[e(v,{gutter:20,class:"mgb20"},{default:t(()=>[e(c,{span:8},{default:t(()=>[e(i,{"body-style":{padding:"0px"}},{default:t(()=>[o("div",re,[e(f,{class:"grid-con-icon"},{default:t(()=>[e(n(K))]),_:1}),_e])]),_:1})]),_:1}),e(c,{span:8},{default:t(()=>[e(i,{"body-style":{padding:"0px"}},{default:t(()=>[o("div",pe,[e(f,{class:"grid-con-icon"},{default:t(()=>[e(n(W))]),_:1}),o("div",me,[o("div",ge,r(n(s).todoNumber),1),he])])]),_:1})]),_:1}),e(c,{span:8},{default:t(()=>[e(i,{"body-style":{padding:"0px"}},{default:t(()=>[o("div",fe,[e(f,{class:"grid-con-icon"},{default:t(()=>[e(n(X))]),_:1}),o("div",ve,[o("div",Be,r(n(s).requestNumber),1),Fe])])]),_:1})]),_:1})]),_:1}),e(i,{style:{height:"402px"}},{header:t(()=>[o("div",be,[xe,e(B,{style:{float:"right",padding:"3px 0"},type:"text",onClick:_[0]||(_[0]=u=>m.value=!0)},{default:t(()=>[Ee]),_:1})])]),default:t(()=>[e(x,{"show-header":!1,data:n(s).todoList,style:{width:"100%"}},{default:t(()=>[e(h,{width:"40"},{default:t(u=>[e(k,{modelValue:u.row.status,"onUpdate:modelValue":E=>u.row.status=E,onChange:E=>C(u.$index)},null,8,["modelValue","onUpdate:modelValue","onChange"])]),_:1}),e(h,null,{default:t(u=>[o("div",{class:Z(["todo-item",{"todo-item-del":u.row.status}])},r(u.row.title),3)]),_:1})]),_:1},8,["data"])]),_:1})]),_:1})]),_:1}),e(v,{gutter:20,style:{"margin-bottom":"-10px"}},{default:t(()=>[e(c,{span:8},{default:t(()=>[e(i,null,{default:t(()=>[we]),_:1})]),_:1}),e(c,{span:16},{default:t(()=>[e(i,null,{default:t(()=>[ye]),_:1})]),_:1})]),_:1}),e(L,{title:"\u6DFB\u52A0\u5F85\u529E",modelValue:m.value,"onUpdate:modelValue":_[2]||(_[2]=u=>m.value=u),width:"30%"},{footer:t(()=>[o("span",De,[e(B,{onClick:V},{default:t(()=>[Ce]),_:1}),e(B,{type:"primary",onClick:D},{default:t(()=>[Ve]),_:1})])]),default:t(()=>[e(z,{"label-width":"100px",autocomplete:"on"},{default:t(()=>[e(q,{label:"\u5F85\u529E\u4E8B\u9879"},{default:t(()=>[e(I,{modelValue:n(s).todoText,"onUpdate:modelValue":_[1]||(_[1]=u=>n(s).todoText=u),placeholder:"\u8BF7\u8F93\u5165\u5F85\u529E\u4E8B\u9879"},null,8,["modelValue"])]),_:1})]),_:1})]),_:1},8,["modelValue"])])}}});var ke=S(Te,[["__scopeId","data-v-23d07705"]]);export{ke as default};
