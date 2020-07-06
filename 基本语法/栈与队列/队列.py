import collections

# 创建一个队列
queue = collections.deque()
# print(type(queue))

# 进队(存数据)
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)

# 出队(取数据)
temp1=queue.popleft()
print(temp1)
print(queue)
temp2=queue.popleft()
print(temp2)
print(queue)
temp3=queue.popleft()
print(temp3)
print(queue)
