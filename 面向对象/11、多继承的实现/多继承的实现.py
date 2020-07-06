from children import Children

def main():
    child1 = Children(100, "beautiful")

    # 如果父类中方法名相同，默认调用的是在括号中排前面的父类中的方法
    child1.func()



if __name__ == '__main__':
    main()