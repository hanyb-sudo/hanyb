#引入模块

import sys

print(sys.argv)

# 获取命令行参数列表
for i in sys.argv:
    print(i)

# 从cmd执行并输入参数
name = sys.argv[1]
age = sys.argv[2]
hobby = sys.argv[3]

print(name,age,hobby)

# 查找模块所需模块的路径的列表
print(sys.path)