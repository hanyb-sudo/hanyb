#排序：冒泡，选择    快速，插入，计数器

#普通排序
list1 = [3,4,5,2,3,1]
list2 = sorted(list1)  #默认升序排序
print(list2)



#按绝对值大小排序
list3 = [-1,-4,-7,2,5]
#key接收函数来实现自定义排序规则
list4 = sorted(list3, key=abs)
print(list4)


#降序
list5 = [1,4,7,2,5]
list6 = sorted(list5, reverse=True)
print(list6)

#按字符串的长短来排序
#自定义函数
def sortByLen(str):
    return len(str)
list7 = ['adasfasfasd','badsfasdf','cfdas','ddfsdfsfas']
list8 = sorted(list7, key=sortByLen)
print(list8)