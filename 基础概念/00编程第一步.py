def MyTest():
    #Fibonacci series斐波那契数列
    # 1 1 2 3
    #两个元素的和确定下一个元素
    a,b = 0,1
    while b < 10:
        print(b)
        a,b = b,a+b

    i = 256 * 256
    print("i的值为:",i)

    #end关键字
    #关键字end可以用于将结果输出到同一行，或者改变输出末尾加不同的字符
    
    a,b = 0,1
    while b < 1000:
        print(b,end=',')
        a,b = b,a+b





MyTest()
