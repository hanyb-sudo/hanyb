/*
内置对象就是指这个语言自带的一些对象，供开发者使用，
这些对象提供了一些常用的或者是最基本而必要的功能。

浏览器上面跑的js的内置对象有Math,String,Array,Date等

对象：包含属性和方法（函数）

数组：就是对象
可以存储多个不同类型的数据
*/
/*
数组相当于python中的列表
arr1 = ["han", "yi", "bo"]
for(var i in arr1){
console.log(arr1[i])
}

var arr2 = new Array(1,2,3,"han")
console.log(arr2)

var arr3 = new Array(10)
arr3[0] = 1
arr3[1] = 1
arr3[2] = 1
arr3[3] = 1
console.log(arr3)

//修改
arr3[0] = 2

//改变长度
arr3.length = 4

//删除(只是删除了数组中的数据)
delete arr3[0]
*/
/*
//数组中常用的方法
arr4 = [1,2,3,4,5,6]

arr4.push(8)//往后放
console.log(arr4)
arr4.unshift(7)//往前放
console.log(arr4)
console.log(arr4.pop())//删除最后一个
console.log(arr4.shift())//删除开始的一个
console.log(arr4)

console.log(arr4.join("-"))//将数组中的元素用特殊符号连接

arr4.reverse()//反转
console.log(arr4)

arr5 = arr4.slice(1,4)//截取
console.log(arr5)

//arr4.splice(0,2,10,11)//在指定位置插入或者替换
//console.log(arr4)

var a = arr4.concat([10,20,30])//拼接成一个新的数组
console.log(a)

var res = arr4.indexOf(90)//在数组中查找元素，有则返回下标，否则返回-1
console.log(res)

console.log(arr4)
var res1 = arr4.lastIndexOf(1)
console.log(res1)
*/

//排序
arr6 = ["abc", "dfdk", "fg", "fafasf"]

arr6.sort(function(x,y){
    return x.length - y.length
})

console.log(arr6)