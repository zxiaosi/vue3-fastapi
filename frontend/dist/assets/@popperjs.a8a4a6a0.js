var R="top",C="bottom",S="right",$="left",we="auto",_=[R,C,S,$],G="start",ee="end",et="clippingParents",Te="viewport",te="popper",tt="reference",Me=_.reduce(function(t,e){return t.concat([e+"-"+G,e+"-"+ee])},[]),Le=[].concat(_,[we]).reduce(function(t,e){return t.concat([e,e+"-"+G,e+"-"+ee])},[]),rt="beforeRead",nt="read",at="afterRead",ot="beforeMain",it="main",st="afterMain",ft="beforeWrite",pt="write",ct="afterWrite",ut=[rt,nt,at,ot,it,st,ft,pt,ct];function L(t){return t?(t.nodeName||"").toLowerCase():null}function T(t){if(t==null)return window;if(t.toString()!=="[object Window]"){var e=t.ownerDocument;return e&&e.defaultView||window}return t}function re(t){var e=T(t).Element;return t instanceof e||t instanceof Element}function k(t){var e=T(t).HTMLElement;return t instanceof e||t instanceof HTMLElement}function We(t){if(typeof ShadowRoot=="undefined")return!1;var e=T(t).ShadowRoot;return t instanceof e||t instanceof ShadowRoot}function lt(t){var e=t.state;Object.keys(e.elements).forEach(function(r){var a=e.styles[r]||{},n=e.attributes[r]||{},o=e.elements[r];!k(o)||!L(o)||(Object.assign(o.style,a),Object.keys(n).forEach(function(s){var i=n[s];i===!1?o.removeAttribute(s):o.setAttribute(s,i===!0?"":i)}))})}function vt(t){var e=t.state,r={popper:{position:e.options.strategy,left:"0",top:"0",margin:"0"},arrow:{position:"absolute"},reference:{}};return Object.assign(e.elements.popper.style,r.popper),e.styles=r,e.elements.arrow&&Object.assign(e.elements.arrow.style,r.arrow),function(){Object.keys(e.elements).forEach(function(a){var n=e.elements[a],o=e.attributes[a]||{},s=Object.keys(e.styles.hasOwnProperty(a)?e.styles[a]:r[a]),i=s.reduce(function(p,c){return p[c]="",p},{});!k(n)||!L(n)||(Object.assign(n.style,i),Object.keys(o).forEach(function(p){n.removeAttribute(p)}))})}}var dt={name:"applyStyles",enabled:!0,phase:"write",fn:lt,effect:vt,requires:["computeStyles"]};function W(t){return t.split("-")[0]}function J(t,e){var r=t.getBoundingClientRect(),a=1,n=1;return{width:r.width/a,height:r.height/n,top:r.top/n,right:r.right/a,bottom:r.bottom/n,left:r.left/a,x:r.left/a,y:r.top/n}}function Oe(t){var e=J(t),r=t.offsetWidth,a=t.offsetHeight;return Math.abs(e.width-r)<=1&&(r=e.width),Math.abs(e.height-a)<=1&&(a=e.height),{x:t.offsetLeft,y:t.offsetTop,width:r,height:a}}function He(t,e){var r=e.getRootNode&&e.getRootNode();if(t.contains(e))return!0;if(r&&We(r)){var a=e;do{if(a&&t.isSameNode(a))return!0;a=a.parentNode||a.host}while(a)}return!1}function H(t){return T(t).getComputedStyle(t)}function mt(t){return["table","td","th"].indexOf(L(t))>=0}function N(t){return((re(t)?t.ownerDocument:t.document)||window.document).documentElement}function ue(t){return L(t)==="html"?t:t.assignedSlot||t.parentNode||(We(t)?t.host:null)||N(t)}function Ne(t){return!k(t)||H(t).position==="fixed"?null:t.offsetParent}function ht(t){var e=navigator.userAgent.toLowerCase().indexOf("firefox")!==-1,r=navigator.userAgent.indexOf("Trident")!==-1;if(r&&k(t)){var a=H(t);if(a.position==="fixed")return null}for(var n=ue(t);k(n)&&["html","body"].indexOf(L(n))<0;){var o=H(n);if(o.transform!=="none"||o.perspective!=="none"||o.contain==="paint"||["transform","perspective"].indexOf(o.willChange)!==-1||e&&o.willChange==="filter"||e&&o.filter&&o.filter!=="none")return n;n=n.parentNode}return null}function ne(t){for(var e=T(t),r=Ne(t);r&&mt(r)&&H(r).position==="static";)r=Ne(r);return r&&(L(r)==="html"||L(r)==="body"&&H(r).position==="static")?e:r||ht(t)||e}function xe(t){return["top","bottom"].indexOf(t)>=0?"x":"y"}var F=Math.max,ae=Math.min,le=Math.round;function ve(t,e,r){return F(t,ae(e,r))}function Fe(){return{top:0,right:0,bottom:0,left:0}}function qe(t){return Object.assign({},Fe(),t)}function Ve(t,e){return e.reduce(function(r,a){return r[a]=t,r},{})}var gt=function(e,r){return e=typeof e=="function"?e(Object.assign({},r.rects,{placement:r.placement})):e,qe(typeof e!="number"?e:Ve(e,_))};function yt(t){var e,r=t.state,a=t.name,n=t.options,o=r.elements.arrow,s=r.modifiersData.popperOffsets,i=W(r.placement),p=xe(i),c=[$,S].indexOf(i)>=0,f=c?"height":"width";if(!(!o||!s)){var m=gt(n.padding,r),E=Oe(o),l=p==="y"?R:$,h=p==="y"?C:S,d=r.rects.reference[f]+r.rects.reference[p]-s[p]-r.rects.popper[f],v=s[p]-r.rects.reference[p],x=ne(o),g=x?p==="y"?x.clientHeight||0:x.clientWidth||0:0,b=d/2-v/2,u=m[l],w=g-E[f]-m[h],y=g/2-E[f]/2+b,O=ve(u,y,w),A=p;r.modifiersData[a]=(e={},e[A]=O,e.centerOffset=O-y,e)}}function bt(t){var e=t.state,r=t.options,a=r.element,n=a===void 0?"[data-popper-arrow]":a;n!=null&&(typeof n=="string"&&(n=e.elements.popper.querySelector(n),!n)||!He(e.elements.popper,n)||(e.elements.arrow=n))}var wt={name:"arrow",enabled:!0,phase:"main",fn:yt,effect:bt,requires:["popperOffsets"],requiresIfExists:["preventOverflow"]};function K(t){return t.split("-")[1]}var Ot={top:"auto",right:"auto",bottom:"auto",left:"auto"};function xt(t){var e=t.x,r=t.y,a=window,n=a.devicePixelRatio||1;return{x:le(le(e*n)/n)||0,y:le(le(r*n)/n)||0}}function Xe(t){var e,r=t.popper,a=t.popperRect,n=t.placement,o=t.variation,s=t.offsets,i=t.position,p=t.gpuAcceleration,c=t.adaptive,f=t.roundOffsets,m=f===!0?xt(s):typeof f=="function"?f(s):s,E=m.x,l=E===void 0?0:E,h=m.y,d=h===void 0?0:h,v=s.hasOwnProperty("x"),x=s.hasOwnProperty("y"),g=$,b=R,u=window;if(c){var w=ne(r),y="clientHeight",O="clientWidth";w===T(r)&&(w=N(r),H(w).position!=="static"&&i==="absolute"&&(y="scrollHeight",O="scrollWidth")),w=w,(n===R||(n===$||n===S)&&o===ee)&&(b=C,d-=w[y]-a.height,d*=p?1:-1),(n===$||(n===R||n===C)&&o===ee)&&(g=S,l-=w[O]-a.width,l*=p?1:-1)}var A=Object.assign({position:i},c&&Ot);if(p){var P;return Object.assign({},A,(P={},P[b]=x?"0":"",P[g]=v?"0":"",P.transform=(u.devicePixelRatio||1)<=1?"translate("+l+"px, "+d+"px)":"translate3d("+l+"px, "+d+"px, 0)",P))}return Object.assign({},A,(e={},e[b]=x?d+"px":"",e[g]=v?l+"px":"",e.transform="",e))}function Et(t){var e=t.state,r=t.options,a=r.gpuAcceleration,n=a===void 0?!0:a,o=r.adaptive,s=o===void 0?!0:o,i=r.roundOffsets,p=i===void 0?!0:i,c={placement:W(e.placement),variation:K(e.placement),popper:e.elements.popper,popperRect:e.rects.popper,gpuAcceleration:n};e.modifiersData.popperOffsets!=null&&(e.styles.popper=Object.assign({},e.styles.popper,Xe(Object.assign({},c,{offsets:e.modifiersData.popperOffsets,position:e.options.strategy,adaptive:s,roundOffsets:p})))),e.modifiersData.arrow!=null&&(e.styles.arrow=Object.assign({},e.styles.arrow,Xe(Object.assign({},c,{offsets:e.modifiersData.arrow,position:"absolute",adaptive:!1,roundOffsets:p})))),e.attributes.popper=Object.assign({},e.attributes.popper,{"data-popper-placement":e.placement})}var Pt={name:"computeStyles",enabled:!0,phase:"beforeWrite",fn:Et,data:{}},de={passive:!0};function At(t){var e=t.state,r=t.instance,a=t.options,n=a.scroll,o=n===void 0?!0:n,s=a.resize,i=s===void 0?!0:s,p=T(e.elements.popper),c=[].concat(e.scrollParents.reference,e.scrollParents.popper);return o&&c.forEach(function(f){f.addEventListener("scroll",r.update,de)}),i&&p.addEventListener("resize",r.update,de),function(){o&&c.forEach(function(f){f.removeEventListener("scroll",r.update,de)}),i&&p.removeEventListener("resize",r.update,de)}}var Dt={name:"eventListeners",enabled:!0,phase:"write",fn:function(){},effect:At,data:{}},Rt={left:"right",right:"left",bottom:"top",top:"bottom"};function me(t){return t.replace(/left|right|bottom|top/g,function(e){return Rt[e]})}var $t={start:"end",end:"start"};function Ye(t){return t.replace(/start|end/g,function(e){return $t[e]})}function Ee(t){var e=T(t),r=e.pageXOffset,a=e.pageYOffset;return{scrollLeft:r,scrollTop:a}}function Pe(t){return J(N(t)).left+Ee(t).scrollLeft}function jt(t){var e=T(t),r=N(t),a=e.visualViewport,n=r.clientWidth,o=r.clientHeight,s=0,i=0;return a&&(n=a.width,o=a.height,/^((?!chrome|android).)*safari/i.test(navigator.userAgent)||(s=a.offsetLeft,i=a.offsetTop)),{width:n,height:o,x:s+Pe(t),y:i}}function Bt(t){var e,r=N(t),a=Ee(t),n=(e=t.ownerDocument)==null?void 0:e.body,o=F(r.scrollWidth,r.clientWidth,n?n.scrollWidth:0,n?n.clientWidth:0),s=F(r.scrollHeight,r.clientHeight,n?n.scrollHeight:0,n?n.clientHeight:0),i=-a.scrollLeft+Pe(t),p=-a.scrollTop;return H(n||r).direction==="rtl"&&(i+=F(r.clientWidth,n?n.clientWidth:0)-o),{width:o,height:s,x:i,y:p}}function Ae(t){var e=H(t),r=e.overflow,a=e.overflowX,n=e.overflowY;return/auto|scroll|overlay|hidden/.test(r+n+a)}function Ie(t){return["html","body","#document"].indexOf(L(t))>=0?t.ownerDocument.body:k(t)&&Ae(t)?t:Ie(ue(t))}function oe(t,e){var r;e===void 0&&(e=[]);var a=Ie(t),n=a===((r=t.ownerDocument)==null?void 0:r.body),o=T(a),s=n?[o].concat(o.visualViewport||[],Ae(a)?a:[]):a,i=e.concat(s);return n?i:i.concat(oe(ue(s)))}function De(t){return Object.assign({},t,{left:t.x,top:t.y,right:t.x+t.width,bottom:t.y+t.height})}function Ct(t){var e=J(t);return e.top=e.top+t.clientTop,e.left=e.left+t.clientLeft,e.bottom=e.top+t.clientHeight,e.right=e.left+t.clientWidth,e.width=t.clientWidth,e.height=t.clientHeight,e.x=e.left,e.y=e.top,e}function ze(t,e){return e===Te?De(jt(t)):k(e)?Ct(e):De(Bt(N(t)))}function St(t){var e=oe(ue(t)),r=["absolute","fixed"].indexOf(H(t).position)>=0,a=r&&k(t)?ne(t):t;return re(a)?e.filter(function(n){return re(n)&&He(n,a)&&L(n)!=="body"}):[]}function kt(t,e,r){var a=e==="clippingParents"?St(t):[].concat(e),n=[].concat(a,[r]),o=n[0],s=n.reduce(function(i,p){var c=ze(t,p);return i.top=F(c.top,i.top),i.right=ae(c.right,i.right),i.bottom=ae(c.bottom,i.bottom),i.left=F(c.left,i.left),i},ze(t,o));return s.width=s.right-s.left,s.height=s.bottom-s.top,s.x=s.left,s.y=s.top,s}function Ue(t){var e=t.reference,r=t.element,a=t.placement,n=a?W(a):null,o=a?K(a):null,s=e.x+e.width/2-r.width/2,i=e.y+e.height/2-r.height/2,p;switch(n){case R:p={x:s,y:e.y-r.height};break;case C:p={x:s,y:e.y+e.height};break;case S:p={x:e.x+e.width,y:i};break;case $:p={x:e.x-r.width,y:i};break;default:p={x:e.x,y:e.y}}var c=n?xe(n):null;if(c!=null){var f=c==="y"?"height":"width";switch(o){case G:p[c]=p[c]-(e[f]/2-r[f]/2);break;case ee:p[c]=p[c]+(e[f]/2-r[f]/2);break}}return p}function ie(t,e){e===void 0&&(e={});var r=e,a=r.placement,n=a===void 0?t.placement:a,o=r.boundary,s=o===void 0?et:o,i=r.rootBoundary,p=i===void 0?Te:i,c=r.elementContext,f=c===void 0?te:c,m=r.altBoundary,E=m===void 0?!1:m,l=r.padding,h=l===void 0?0:l,d=qe(typeof h!="number"?h:Ve(h,_)),v=f===te?tt:te,x=t.rects.popper,g=t.elements[E?v:f],b=kt(re(g)?g:g.contextElement||N(t.elements.popper),s,p),u=J(t.elements.reference),w=Ue({reference:u,element:x,strategy:"absolute",placement:n}),y=De(Object.assign({},x,w)),O=f===te?y:u,A={top:b.top-O.top+d.top,bottom:O.bottom-b.bottom+d.bottom,left:b.left-O.left+d.left,right:O.right-b.right+d.right},P=t.modifiersData.offset;if(f===te&&P){var j=P[n];Object.keys(A).forEach(function(B){var q=[S,C].indexOf(B)>=0?1:-1,D=[R,C].indexOf(B)>=0?"y":"x";A[B]+=j[D]*q})}return A}function Tt(t,e){e===void 0&&(e={});var r=e,a=r.placement,n=r.boundary,o=r.rootBoundary,s=r.padding,i=r.flipVariations,p=r.allowedAutoPlacements,c=p===void 0?Le:p,f=K(a),m=f?i?Me:Me.filter(function(h){return K(h)===f}):_,E=m.filter(function(h){return c.indexOf(h)>=0});E.length===0&&(E=m);var l=E.reduce(function(h,d){return h[d]=ie(t,{placement:d,boundary:n,rootBoundary:o,padding:s})[W(d)],h},{});return Object.keys(l).sort(function(h,d){return l[h]-l[d]})}function Mt(t){if(W(t)===we)return[];var e=me(t);return[Ye(t),e,Ye(e)]}function Lt(t){var e=t.state,r=t.options,a=t.name;if(!e.modifiersData[a]._skip){for(var n=r.mainAxis,o=n===void 0?!0:n,s=r.altAxis,i=s===void 0?!0:s,p=r.fallbackPlacements,c=r.padding,f=r.boundary,m=r.rootBoundary,E=r.altBoundary,l=r.flipVariations,h=l===void 0?!0:l,d=r.allowedAutoPlacements,v=e.options.placement,x=W(v),g=x===v,b=p||(g||!h?[me(v)]:Mt(v)),u=[v].concat(b).reduce(function(X,M){return X.concat(W(M)===we?Tt(e,{placement:M,boundary:f,rootBoundary:m,padding:c,flipVariations:h,allowedAutoPlacements:d}):M)},[]),w=e.rects.reference,y=e.rects.popper,O=new Map,A=!0,P=u[0],j=0;j<u.length;j++){var B=u[j],q=W(B),D=K(B)===G,Q=[R,C].indexOf(q)>=0,Z=Q?"width":"height",Y=ie(e,{placement:B,boundary:f,rootBoundary:m,altBoundary:E,padding:c}),V=Q?D?S:$:D?C:R;w[Z]>y[Z]&&(V=me(V));var he=me(V),I=[];if(o&&I.push(Y[q]<=0),i&&I.push(Y[V]<=0,Y[he]<=0),I.every(function(X){return X})){P=B,A=!1;break}O.set(B,I)}if(A)for(var se=h?3:1,ge=function(M){var pe=u.find(function(ye){var U=O.get(ye);if(U)return U.slice(0,M).every(function(be){return be})});if(pe)return P=pe,"break"},z=se;z>0;z--){var fe=ge(z);if(fe==="break")break}e.placement!==P&&(e.modifiersData[a]._skip=!0,e.placement=P,e.reset=!0)}}var Wt={name:"flip",enabled:!0,phase:"main",fn:Lt,requiresIfExists:["offset"],data:{_skip:!1}};function Ge(t,e,r){return r===void 0&&(r={x:0,y:0}),{top:t.top-e.height-r.y,right:t.right-e.width+r.x,bottom:t.bottom-e.height+r.y,left:t.left-e.width-r.x}}function Je(t){return[R,S,C,$].some(function(e){return t[e]>=0})}function Ht(t){var e=t.state,r=t.name,a=e.rects.reference,n=e.rects.popper,o=e.modifiersData.preventOverflow,s=ie(e,{elementContext:"reference"}),i=ie(e,{altBoundary:!0}),p=Ge(s,a),c=Ge(i,n,o),f=Je(p),m=Je(c);e.modifiersData[r]={referenceClippingOffsets:p,popperEscapeOffsets:c,isReferenceHidden:f,hasPopperEscaped:m},e.attributes.popper=Object.assign({},e.attributes.popper,{"data-popper-reference-hidden":f,"data-popper-escaped":m})}var Nt={name:"hide",enabled:!0,phase:"main",requiresIfExists:["preventOverflow"],fn:Ht};function Ft(t,e,r){var a=W(t),n=[$,R].indexOf(a)>=0?-1:1,o=typeof r=="function"?r(Object.assign({},e,{placement:t})):r,s=o[0],i=o[1];return s=s||0,i=(i||0)*n,[$,S].indexOf(a)>=0?{x:i,y:s}:{x:s,y:i}}function qt(t){var e=t.state,r=t.options,a=t.name,n=r.offset,o=n===void 0?[0,0]:n,s=Le.reduce(function(f,m){return f[m]=Ft(m,e.rects,o),f},{}),i=s[e.placement],p=i.x,c=i.y;e.modifiersData.popperOffsets!=null&&(e.modifiersData.popperOffsets.x+=p,e.modifiersData.popperOffsets.y+=c),e.modifiersData[a]=s}var Vt={name:"offset",enabled:!0,phase:"main",requires:["popperOffsets"],fn:qt};function Xt(t){var e=t.state,r=t.name;e.modifiersData[r]=Ue({reference:e.rects.reference,element:e.rects.popper,strategy:"absolute",placement:e.placement})}var Yt={name:"popperOffsets",enabled:!0,phase:"read",fn:Xt,data:{}};function It(t){return t==="x"?"y":"x"}function zt(t){var e=t.state,r=t.options,a=t.name,n=r.mainAxis,o=n===void 0?!0:n,s=r.altAxis,i=s===void 0?!1:s,p=r.boundary,c=r.rootBoundary,f=r.altBoundary,m=r.padding,E=r.tether,l=E===void 0?!0:E,h=r.tetherOffset,d=h===void 0?0:h,v=ie(e,{boundary:p,rootBoundary:c,padding:m,altBoundary:f}),x=W(e.placement),g=K(e.placement),b=!g,u=xe(x),w=It(u),y=e.modifiersData.popperOffsets,O=e.rects.reference,A=e.rects.popper,P=typeof d=="function"?d(Object.assign({},e.rects,{placement:e.placement})):d,j={x:0,y:0};if(!!y){if(o||i){var B=u==="y"?R:$,q=u==="y"?C:S,D=u==="y"?"height":"width",Q=y[u],Z=y[u]+v[B],Y=y[u]-v[q],V=l?-A[D]/2:0,he=g===G?O[D]:A[D],I=g===G?-A[D]:-O[D],se=e.elements.arrow,ge=l&&se?Oe(se):{width:0,height:0},z=e.modifiersData["arrow#persistent"]?e.modifiersData["arrow#persistent"].padding:Fe(),fe=z[B],X=z[q],M=ve(0,O[D],ge[D]),pe=b?O[D]/2-V-M-fe-P:he-M-fe-P,ye=b?-O[D]/2+V+M+X+P:I+M+X+P,U=e.elements.arrow&&ne(e.elements.arrow),be=U?u==="y"?U.clientTop||0:U.clientLeft||0:0,Re=e.modifiersData.offset?e.modifiersData.offset[e.placement][u]:0,$e=y[u]+pe-Re-be,je=y[u]+ye-Re;if(o){var Be=ve(l?ae(Z,$e):Z,Q,l?F(Y,je):Y);y[u]=Be,j[u]=Be-Q}if(i){var Ze=u==="x"?R:$,_e=u==="x"?C:S,ce=y[w],Ce=ce+v[Ze],Se=ce-v[_e],ke=ve(l?ae(Ce,$e):Ce,ce,l?F(Se,je):Se);y[w]=ke,j[w]=ke-ce}}e.modifiersData[a]=j}}var Ut={name:"preventOverflow",enabled:!0,phase:"main",fn:zt,requiresIfExists:["offset"]};function Gt(t){return{scrollLeft:t.scrollLeft,scrollTop:t.scrollTop}}function Jt(t){return t===T(t)||!k(t)?Ee(t):Gt(t)}function Kt(t){var e=t.getBoundingClientRect(),r=e.width/t.offsetWidth||1,a=e.height/t.offsetHeight||1;return r!==1||a!==1}function Qt(t,e,r){r===void 0&&(r=!1);var a=k(e);k(e)&&Kt(e);var n=N(e),o=J(t),s={scrollLeft:0,scrollTop:0},i={x:0,y:0};return(a||!a&&!r)&&((L(e)!=="body"||Ae(n))&&(s=Jt(e)),k(e)?(i=J(e),i.x+=e.clientLeft,i.y+=e.clientTop):n&&(i.x=Pe(n))),{x:o.left+s.scrollLeft-i.x,y:o.top+s.scrollTop-i.y,width:o.width,height:o.height}}function Zt(t){var e=new Map,r=new Set,a=[];t.forEach(function(o){e.set(o.name,o)});function n(o){r.add(o.name);var s=[].concat(o.requires||[],o.requiresIfExists||[]);s.forEach(function(i){if(!r.has(i)){var p=e.get(i);p&&n(p)}}),a.push(o)}return t.forEach(function(o){r.has(o.name)||n(o)}),a}function _t(t){var e=Zt(t);return ut.reduce(function(r,a){return r.concat(e.filter(function(n){return n.phase===a}))},[])}function er(t){var e;return function(){return e||(e=new Promise(function(r){Promise.resolve().then(function(){e=void 0,r(t())})})),e}}function tr(t){var e=t.reduce(function(r,a){var n=r[a.name];return r[a.name]=n?Object.assign({},n,a,{options:Object.assign({},n.options,a.options),data:Object.assign({},n.data,a.data)}):a,r},{});return Object.keys(e).map(function(r){return e[r]})}var Ke={placement:"bottom",modifiers:[],strategy:"absolute"};function Qe(){for(var t=arguments.length,e=new Array(t),r=0;r<t;r++)e[r]=arguments[r];return!e.some(function(a){return!(a&&typeof a.getBoundingClientRect=="function")})}function rr(t){t===void 0&&(t={});var e=t,r=e.defaultModifiers,a=r===void 0?[]:r,n=e.defaultOptions,o=n===void 0?Ke:n;return function(i,p,c){c===void 0&&(c=o);var f={placement:"bottom",orderedModifiers:[],options:Object.assign({},Ke,o),modifiersData:{},elements:{reference:i,popper:p},attributes:{},styles:{}},m=[],E=!1,l={state:f,setOptions:function(x){var g=typeof x=="function"?x(f.options):x;d(),f.options=Object.assign({},o,f.options,g),f.scrollParents={reference:re(i)?oe(i):i.contextElement?oe(i.contextElement):[],popper:oe(p)};var b=_t(tr([].concat(a,f.options.modifiers)));return f.orderedModifiers=b.filter(function(u){return u.enabled}),h(),l.update()},forceUpdate:function(){if(!E){var x=f.elements,g=x.reference,b=x.popper;if(!!Qe(g,b)){f.rects={reference:Qt(g,ne(b),f.options.strategy==="fixed"),popper:Oe(b)},f.reset=!1,f.placement=f.options.placement,f.orderedModifiers.forEach(function(j){return f.modifiersData[j.name]=Object.assign({},j.data)});for(var u=0;u<f.orderedModifiers.length;u++){if(f.reset===!0){f.reset=!1,u=-1;continue}var w=f.orderedModifiers[u],y=w.fn,O=w.options,A=O===void 0?{}:O,P=w.name;typeof y=="function"&&(f=y({state:f,options:A,name:P,instance:l})||f)}}}},update:er(function(){return new Promise(function(v){l.forceUpdate(),v(f)})}),destroy:function(){d(),E=!0}};if(!Qe(i,p))return l;l.setOptions(c).then(function(v){!E&&c.onFirstUpdate&&c.onFirstUpdate(v)});function h(){f.orderedModifiers.forEach(function(v){var x=v.name,g=v.options,b=g===void 0?{}:g,u=v.effect;if(typeof u=="function"){var w=u({state:f,name:x,instance:l,options:b}),y=function(){};m.push(w||y)}})}function d(){m.forEach(function(v){return v()}),m=[]}return l}}var nr=[Dt,Yt,Pt,dt,Vt,Wt,Ut,wt,Nt],ar=rr({defaultModifiers:nr});export{ar as c};