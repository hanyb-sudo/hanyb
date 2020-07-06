/*
BOM：浏览器对象模型（Browser Object Model），
是一个用于访问浏览器和计算机屏幕的对象集合。
我们可以通过全局对象windows来访问这些对象。
*/
/*
console.log(window.document)//html标签
console.log(window.frames)//windows框架
console.log(window.navigator)//浏览器信息
console.log(window.screen)//屏幕信息
console.log(window.location)
*/
/*
href属性  控制浏览器地址栏的内容
reload()    刷新页面
reload(true)    刷新页面，不带缓存
assign()    加载新的页面
replace()   加载新的页面(注意：不会在浏览器的历史记录中留下记录)
*/
//console.log(window.history)
/*
window.history.length   获取历史记录的长度
back()    上一页
forward() 下一页
go(num)     num<0时，跳转到自己后方的第num个记录。
            num>0时，跳转到自己前方的第num个记录。
*/

function red(){
    console.log("你点击了red按钮，跳转到red页面")
    window.location.href = "red.html"
}

function pink(){
    console.log("你点击了pink按钮，跳转到pink页面")
    window.location.href = "pink.html"
}

function lastPage(){
    console.log("你点击了上一页按钮")
    window.history.back()
}

function nextPage(){
    console.log("你点击了下一页按钮")
    window.history.forward()
}

function reload(){
    console.log("你点击了刷新按钮")
    window.location.reload()
}

function func1(){
    window.open("red.html", "blank", "width=400px, height=500px, top=0px, left=300px");
}

function func2(){
    window.close()
}