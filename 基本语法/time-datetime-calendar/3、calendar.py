import calendar


# 使用

# 返回指定某年某月的日历
r1 = calendar.month(2020,3)
print(r1)
print(type(r1))

# 返回指定年的日历
r2 = calendar.calendar(2020)
print(r2)
print(type(r2))

# 闰年返回True，否则False
print(calendar.isleap(2020))

# 返回某个月的weekday的第一天和这个月的所有天数
print(calendar.monthrange(2020,3))

# 返回某个月以每一周为元素的列表
print(calendar.monthcalendar())
