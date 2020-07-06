/*
函数
function 函数名(){
    语句
    return
}

function func(num1, num2){
for(var i =0; i<arguments.length;i++){
console.log(arguments[i])
}
//声明一个变量时没有使用var语句，该变量就会默认为全局的。
//函数内部可以向访问自己的局部变量那样访问全局变量
return num1 + num2
}

console.log(func(1,2,3,4,5,6))
*/

/*
函数也是一种数据

function mySum(num1, num2){
return(num1 + num2)
}

var f = mySum;
console.log(f(3,4))

function myfunc(s, a, b){
return s(a, b);
}

console.log(myfunc(f, 4, 5))
*/

//匿名函数
/*

var f = function(a, b){
return a + b
}

console.log(f(1,2))

function sum(function(a, b){
return a + b
}, 3, 4)
console.log(sum())
*/

//即时函数
//(匿名函数)(匿名函数传参)
/*
(function(str){console.log(str)})("hello， ymp！")
*/
