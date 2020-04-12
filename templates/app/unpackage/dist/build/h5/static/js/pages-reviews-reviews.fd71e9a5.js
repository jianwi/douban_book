(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-reviews-reviews"],{2723:function(t,e,i){"use strict";i.r(e);var a=i("35e8"),n=i.n(a);for(var s in a)"default"!==s&&function(t){i.d(e,t,(function(){return a[t]}))}(s);e["default"]=n.a},"2f09":function(t,e,i){"use strict";var a=i("3a61"),n=i.n(a);n.a},"35e8":function(t,e,i){"use strict";var a=i("ee27");i("99af"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var n=a(i("a199")),s={data:function(){return{reviews:null,book:null,message:"书评列表",subject:"",start:0,hasMore:!0}},components:{star:n.default},methods:{goReviewDetail:function(t){var e=t.currentTarget.dataset.code;uni.navigateTo({url:"../review/review?code="+e})}},onLoad:function(t){var e=this;this.subject=t.id,uni.showLoading({title:"加载中，请稍后"}),uni.request({url:"http://47.102.212.210:5000/book/"+t.id,success:function(t){500==t.statusCode&&uni.showToast({icon:"none",title:"抱歉！此书还没有书评"}),e.reviews=t.data.data.items,e.book=t.data.data.book,uni.hideLoading()},fail:function(){this.message="此书没有书评"}})},onReachBottom:function(){var t=this;console.log("到底了"),this.hasMore&&(uni.showLoading({title:"正在拼命加载中..."}),this.start+=20,uni.request({url:"http://47.102.212.210:5000/book/"+this.subject+"/"+this.start,success:function(e){500==e.statusCode&&(t.hasMore=!1,uni.showToast({icon:"none",title:"抱歉！没有更多书评了"})),t.reviews=t.reviews.concat(e.data.data.items),uni.hideLoading()}}))}};e.default=s},"3a61":function(t,e,i){var a=i("fc42");"string"===typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);var n=i("4f06").default;n("01347e7d",a,!0,{sourceMap:!1,shadowMode:!1})},"4e05":function(t,e,i){"use strict";var a={star:i("a199").default},n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",[i("v-uni-view",{directives:[{name:"show",rawName:"v-show",value:t.book,expression:"book"}],staticClass:"uni-flex uni-row uni-page-body",staticStyle:{padding:"10upx"}},[i("v-uni-view",{directives:[{name:"show",rawName:"v-show",value:t.book,expression:"book"}],staticClass:"uni-flex-item uni-center"},[i("v-uni-image",{staticClass:"book_pic",attrs:{src:t.book.pic,mode:"aspectFit"}})],1),i("v-uni-view",{staticClass:"uni-flex-item uni-column uni-flex  uni-container",staticStyle:{"padding-top":"12upx"}},[i("v-uni-text",{staticClass:"uni-h4"},[t._v(t._s(t.book.name))]),i("v-uni-text",{staticClass:"uni-h5"},[t._v(t._s(t.book.author))]),i("v-uni-text",{staticClass:"uni-h5"},[t._v(t._s(t.book.publish))]),i("v-uni-text",{staticClass:"uni-h5"},[t._v("价格： "+t._s(t.book.prize))]),i("v-uni-text",{staticClass:"uni-h5"},[t._v("页数："+t._s(t.book.pages))]),i("v-uni-text",{staticClass:"uni-h5"},[t._v("出版时间: "+t._s(t.book.date))])],1)],1),i("v-uni-view",{staticClass:"uni-center"},[i("v-uni-view",{staticClass:"title uni-center uni-padding-wrap uni-h4 bg-gray",staticStyle:{margin:"auto","margin-top":"30upx","margin-bottom":"35upx","border-radius":"10px",padding:"15upx"}},[t._v(t._s(t.message))])],1),i("v-uni-view",{directives:[{name:"show",rawName:"v-show",value:t.reviews,expression:"reviews"}],staticClass:"uni-flex uni-column"},t._l(t.reviews,(function(e,a){return i("v-uni-view",{key:a,staticClass:"review-container uni-flex-item uni-padding-wrap"},[i("v-uni-view",{staticClass:"avatar-container uni-flex"},[i("v-uni-image",{staticClass:"avatar",attrs:{src:e.avatar,mode:"aspectFit"}}),i("v-uni-view",{staticClass:"uni-flex uni-column"},[i("v-uni-view",{staticClass:"uni-flex base-center uni-row"},[i("v-uni-text",{staticClass:"uni-h5",staticStyle:{"margin-left":"30upx","font-size":"1.3em"}},[t._v(t._s(e.author))]),i("v-uni-text",{staticStyle:{margin:"35upx"}},[i("star",{attrs:{stars:"5"}})],1)],1)],1)],1),i("v-uni-view",[i("v-uni-view",{staticClass:"review-title",attrs:{"data-code":e.code},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.goReviewDetail.apply(void 0,arguments)}}},[t._v(t._s(e.name))]),t._v(t._s(e.review_short))],1)],1)})),1)],1)},s=[];i.d(e,"b",(function(){return n})),i.d(e,"c",(function(){return s})),i.d(e,"a",(function(){return a}))},"54f1":function(t,e,i){"use strict";i("e25e"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var a={data:function(){return{}},props:["stars"],computed:{star_count:function(){return console.log(this),parseInt(this.stars)}},methods:{}};e.default=a},"582c":function(t,e,i){"use strict";i.r(e);var a=i("54f1"),n=i.n(a);for(var s in a)"default"!==s&&function(t){i.d(e,t,(function(){return a[t]}))}(s);e["default"]=n.a},7790:function(t,e,i){var a=i("e17d");"string"===typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);var n=i("4f06").default;n("ce9e64c2",a,!0,{sourceMap:!1,shadowMode:!1})},a199:function(t,e,i){"use strict";i.r(e);var a=i("c8b3"),n=i("582c");for(var s in n)"default"!==s&&function(t){i.d(e,t,(function(){return n[t]}))}(s);i("fc20");var o,r=i("f0c5"),u=Object(r["a"])(n["default"],a["b"],a["c"],!1,null,"2ddea21a",null,!1,a["a"],o);e["default"]=u.exports},c223:function(t,e,i){"use strict";i.r(e);var a=i("4e05"),n=i("2723");for(var s in n)"default"!==s&&function(t){i.d(e,t,(function(){return n[t]}))}(s);i("2f09");var o,r=i("f0c5"),u=Object(r["a"])(n["default"],a["b"],a["c"],!1,null,"2111be3f",null,!1,a["a"],o);e["default"]=u.exports},c8b3:function(t,e,i){"use strict";var a,n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",{staticClass:"uni-flex star-container"},t._l(t.star_count,(function(e){return i("v-uni-text",[t._v("♥")])})),1)},s=[];i.d(e,"b",(function(){return n})),i.d(e,"c",(function(){return s})),i.d(e,"a",(function(){return a}))},e17d:function(t,e,i){var a=i("24fb");e=a(!1),e.push([t.i,".star-container[data-v-2ddea21a]{-webkit-box-align:center;-webkit-align-items:center;align-items:center;color:red}",""]),t.exports=e},fc20:function(t,e,i){"use strict";var a=i("7790"),n=i.n(a);n.a},fc42:function(t,e,i){var a=i("24fb");e=a(!1),e.push([t.i,".book_pic[data-v-2111be3f]{width:%?255?%;height:%?355?%;margin:2px}.review-container[data-v-2111be3f]{border-bottom:2px #9fcdff dashed;padding-bottom:%?25?%;margin-bottom:%?35?%}.avatar[data-v-2111be3f]{width:60px;height:60px;border-radius:30px;margin-right:10px}.avatar-container[data-v-2111be3f]{padding:3px;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.review-title[data-v-2111be3f]{font-size:1.3em;font-weight:800;color:#000}.base-center[data-v-2111be3f]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.bg-gray[data-v-2111be3f]{background-color:#d5df07;color:#fff}",""]),t.exports=e}}]);