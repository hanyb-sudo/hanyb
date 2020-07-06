import doctest
# doctest 模块可以提取注释中的代码执行
#doctest 严格按照Python交互模式的输入提取


def mySum(x, y):
    '''
    get The Sum of The x and y
    :param x: firstNumber
    :param y: secondNumber
    :return: sum

    example:
    >>> print(mySum(1, 2))  #>>>后面要加上一个空格
    3               #3 只能放在>>>下面
    '''
    return x + y


print(mySum(1, 2))

# mySum(1, 2)
#进行文档测试
doctest.testmod()