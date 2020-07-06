import re


'''
字符串切割
split(pattern, string, maxsplit=0, flags=0)
'''
str1 = "hanyb   is   a   good man"
print(str1.split(" "))
print(re.split(r" +", str1))

'''
re.finditer函数
原型：finditer(pattern, string, flags=0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器

'''
str = "hanb is a good man!hanb is a good man!hanb is a good man!hanb is a good man!"
it = re.finditer("hanb", str)
'''
while True:
    try:
        print(next(it))

    except StopIteration as e:
        break
'''

'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
参数：
pattern:    正则表达式(规则)
repl:   指定的用来替换的字符串
string: 目标字符串
count:  最多替换次数
flags:
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。
可以指定替换的次数。如果不指定，替换所有匹配的字符串

区别：
前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数

'''
str = "hanb is a good man!hanb is a good man!hanb is a good man!hanb is a good man!"
print(re.sub(r"(good)", "nice", str))#返回字符串类型
print(re.subn(r"(good)", "nice", str))  #返回元组



'''
分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是提取分组

'''
str1 = "010-53247654"

m = re.match(r"((?P<f1>\d{3})-(\d{8}))", str1)
#使用序号获取对应组的信息，group(0)一直代表的原始字符串
print(m.group(0))
print(m.group(1))
#根据组的名字取出组的内容
print(m.group("f1"))
print(m.group(2))
print(m.group(3))

#查看匹配各组的情况
print(m.groups())


'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
pattern：要编译的正则表达式

'''
pat = r"(^1[34578]\d{9})$"
#编译成正则对象
re_telphone = re.compile(pat)

print(re_telphone.match("13540598422"))

#re模块调用
#re对象调用
# re.match(pattern, string, flags=0)
#re_telphone.match(string)
# re.search(pattern, string, flags=0)
#re_telphone.search(string)
# re.findall(pattern, string, flags=0)
#re_telphone.findall(string)
# re.finditer(pattern, string, flags=0)
#re_telphone.finditer(string)
# re.split(pattern, string, maxsplit=0, flags=0)
#re_telphone.split(string, maxsplit=0)
# re.sub(pattern, repl, string, flags=0)
#re_telphone.sub(repl, string, flags=0)
# re.subn(pattern, repl, string, flags=0)
#re_telphone.subn(repl, string, flags=0)