
/*var str1 = "hanyb is a good man"
var str2 = new String("hanyb is a good man")


console.log(str1)
console.log(str2)
console.log(typeof(str1))
console.log(typeof(str2))

console.log(str1.length)
console.log(str2.length)
*/

//常用方法
var str1 = "hanyb is a good man"
var str2 = new String("hanyb is a good man")

console.log(str1.charAt(12))//根据下标取对应的元素
console.log(str1.charCodeAt(12))//元素的ASCLL码值
console.log(String.fromCharCode(20975))//类名方法

var str3 = "abc"
var str4 = "abc"

console.log(str3 > str4)
console.log(str3.localeCompare(str4))//相比较

console.log(str1.indexOf("man"))//索引

var str3 = str1.replace("good","nice")//替换
console.log(str3)

var res = str1.substring(0,5)//截取
console.log(res)

//字符串分割
console.log(str1.split(" "))