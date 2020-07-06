import re


print("---------------------匹配单个字符与数字--------------------------")
'''
.       匹配除换行符以外的任意字符
[0123456789]    []是字符集合，表示匹配方括号所包含的任意一种字符
[hanyb]     匹配[]中的任意一个字符
[a-z]       表示匹配任意小写字母
[A-Z]       表示匹配任意大写字母
[0-9]       匹配任意数字，类似[0123456789]
[0-9a-zA-Z] 匹配任意数字和字母
[0-9a-zA-Z_]    匹配任意数字和字母和下划线
[^hanyb]    匹配除了hanyb这几个字符以外的所有字符,中括号中的^称为脱字符，表示不匹配集合中的字符
[^0-9]      匹配所有非数字字符
\d          匹配数字，效果同[0-9]
\D          匹配非数字字符，效果同[^0-9]
\w          匹配数字、字母和下划线，效果同[0-9a-zA-Z_]
\W          匹配非数字、字母和下划线，效果同[^0-9a-zA-Z_]
\s          匹配任意的空白符(换行、回车、空白、换页、制表)，效果同[ \f\n\r\t]
\S          匹配任意的非空白符，效果同[^ \f\n\r\t]

'''
print(re.findall("[\W]", "hanyb is a handsome boy45!"))


print("-----------------------锚字符(边界字符)--------------------------")
'''
^       行首匹配，和在[]里的不是一个意思
$       行尾匹配
\A      匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z      匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结尾，即使在re.M模式下也不会匹配它行的行尾
\b      匹配一个单词的边界，也就是指单词和空格间的位置
        'er\b'可以匹配never，不能匹配nerve
\B      匹配非单词边界


'''
# print(re.findall("^hanyb", "hanyb is a good man!\nhanyb Hello man!", re.M))
# print(re.findall("\Ahanyb", "hanyb is a good man!\nhanyb Hello man!", re.M))
# print(re.findall("man!$", "hanyb is a good man!\nhanyb Hello man!", re.M))
# print(re.findall("man!\Z", "hanyb is a good man!\nhanyb Hello man!", re.M))

print(re.search(r"er\b", "never"))
print(re.search(r"er\b", "nerve"))
print(re.search(r"er\B", "never"))
print(re.search(r"er\B", "nerve"))


print("-------------------------匹配多个字符-------------------------------")

'''
说明：下方的x、y、z均为假设的普通字符，不是正则表达式的元字符

(xyz)   匹配小括号内的xyz(作为一个整体去匹配)
x?      匹配0个或者1个x
x*      匹配0个或者任意多个x   (.*)表示匹配0个或者任意多个字符(换行符除外)
x+      匹配至少一个x
x{n}    匹配确定的n个x(n是一个非负整数)
x{n, }  匹配至少n个x
x{n,m}  匹配至少n个至多m个x。注意：n <= m
x|y     |表示或，匹配的是x或y


'''

# print(re.findall("hanyb", "hanyb is a good man hanyb"))
# print(re.findall("a?", "aaaaaaaaa")) #非贪婪匹配(尽可能少的匹配)
# print(re.findall("a*", "aaaaaaaabbaaa")) #贪婪匹配(尽可能多的匹配)
print(re.findall("a+", "dddjklaa"))
print(re.findall("a{2}", "aaaaaaa"))
print(re.findall("a{1,3}", "aaa"))
print(re.findall("((h|H)anyb)", "hanyb ----Hanyb"))


#需求：提取hanyb……man
str = "hanyb is a good man!hanyb is a nice man!hanyb is a handsome man!hanyb is a perfect man!"
print(re.findall(r"hanyb.*?man", str))




print("-------------------------特殊---------------------------")
'''
*?      +?      x?  最小匹配  通常都是尽可能多的匹配，可以使用这种解决贪婪匹配

(?:x)       类似(xyz)，但不表示一个组
'''

#注释：/*  part1   */  /*   part2   */

#转义//*   /*/(/转义*，/*代表普通字符*)
print(re.findall(r"//*.*?/*/", "/*  part1   */  /*   part2   */"))
