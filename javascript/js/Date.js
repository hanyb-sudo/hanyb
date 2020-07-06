//Date对象

/*
//获取当前时间,创建Date对象
var d1 = Date()
console.log(d1)
console.log(typeof(d1))//String类型的

//设置初始值
var d2 = new Date("2019/1/26/12:30")
//var d2 = new Date("2019-1-26-12:30")
console.log(typeof(d2))//对象类型的Object
console.log(d2)

//输入时间戳
var d3 = new Date(2000)
console.log(typeof(d3))//对象类型的Object
console.log(d3)
*/

var d = new Date()
//修改年份
//d.setFullYear(2009)
//console.log(d)

//时间转换成字符串
var str = d.toLocaleString()
console.log(str)
//只要时间
var str1 = d.toLocaleTimeString()
console.log(str1)
//只要日期
var str2 = d.toLocaleDateString()
console.log(str2)

//日期运算
var d4 = new Date("2018-12-12")
console.log(d - d4)