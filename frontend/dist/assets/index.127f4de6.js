import{d as y,u as x,g as C,Y as B,r as m,o as I,i as b,j as _,l as t,k as n,a4 as R,w as a,x as V,y as k,a6 as U,a7 as A,Z as S,z as q,E as w}from"./vendor.be4efd2f.js";import{l as D,A as E,_ as N,u as T,s as v}from"./index.643fda45.js";const $=s=>D.request({headers:{"Content-Type":"application/x-www-form-urlencoded"},url:`${E}/login`,method:"POST",data:s,transformRequest:[function(u){var r="";for(var e in u)if(Array.isArray(u[e])){let l=u[e].join(" ");r+=encodeURIComponent(e)+"="+encodeURIComponent(l)+"&"}else r+=encodeURIComponent(e)+"="+encodeURIComponent(u[e])+"&";return r.substring(0,r.length-1)}]});var h=(s=>(s.admin="admin",s.teacher="teacher",s.student="student",s))(h||{});const j=s=>(V("data-v-05bf2ce3"),s=s(),k(),s),z={class:"login-wrap"},K={class:"ms-login"},L=j(()=>_("div",{class:"ms-title"},"\u5B66\u751F\u9009\u8BFE\u7CFB\u7EDF",-1)),O={class:"login-btn"},J=q("\u767B\u5F55"),M=y({setup(s){T().clearTags;const r=x(),e=C({username:"admin",password:"123"}),l=B(),F={username:[{required:!0,message:"\u8BF7\u8F93\u5165\u7528\u6237\u540D",trigger:"blur"}],password:[{required:!0,message:"\u8BF7\u8F93\u5165\u5BC6\u7801",trigger:"blur"}]},f=c=>{!c||c.validate(async o=>{if(o){let d={username:e.username,password:e.password,scope:[h.admin]};const{access_token:i}=await $(d);w.success("\u767B\u5F55\u6210\u529F"),v("userInfo",JSON.stringify({name:e.username})),v("Authorization",i),r.push("/")}else return w.warning("\u6570\u636E\u6821\u9A8C\u5931\u8D25\uFF01"),!1})};return(c,o)=>{const d=m("el-button"),i=m("el-input"),g=m("el-form-item");return I(),b("div",z,[_("div",K,[L,t(n(R),{ref_key:"loginRef",ref:l,model:n(e),rules:F,"label-width":"0px",class:"ms-content"},{default:a(()=>[t(g,{prop:"username"},{default:a(()=>[t(i,{modelValue:n(e).username,"onUpdate:modelValue":o[0]||(o[0]=p=>n(e).username=p),placeholder:"\u7528\u6237\u540D",maxlength:"10"},{prepend:a(()=>[t(d,{icon:n(U)},null,8,["icon"])]),_:1},8,["modelValue"])]),_:1}),t(g,{prop:"password"},{default:a(()=>[t(i,{type:"password",placeholder:"\u5BC6\u7801",modelValue:n(e).password,"onUpdate:modelValue":o[1]||(o[1]=p=>n(e).password=p),"show-password":"",maxlength:"20",onKeyup:o[2]||(o[2]=S(p=>f(l.value),["enter"]))},{prepend:a(()=>[t(d,{icon:n(A)},null,8,["icon"])]),_:1},8,["modelValue"])]),_:1}),_("div",O,[t(d,{type:"primary",onClick:o[3]||(o[3]=p=>f(l.value))},{default:a(()=>[J]),_:1})])]),_:1},8,["model"])])])}}});var G=N(M,[["__scopeId","data-v-05bf2ce3"]]);export{G as default};
