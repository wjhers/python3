def MyTest():
    #Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    #元组使用小括号 ( )，列表使用方括号 [ ]。
    #元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    tup1 = ('Google', 'Runoob', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5 )

    tup3 = "a", "b", "c", "d"   #  不需要括号也可以

    print(tup3)
    print(type(tup3)) #<class 'tuple'>
    #创建空元组
    temptuple = ()
    print(temptuple)
    print(type(temptuple))
    #创建只包含一个元素的元组时，元素后面加逗号
    tupl1 = (2)
    print(type(tupl1)) # 假的元组 #<class 'int'>
    tupl2 = (2,)
    print(type(tupl2)) #<class 'tuple'>
    #元组与字符串类似，下标索引从 0 开始，可以进行截取，组合等。
    tup1 = ('Google', 'Runoob', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7 )
    print("tup1:",tup1)
    print ("tup1[0]: ", tup1[0])
    print("tup2:",tup2)
    print ("tup2[1:5]: ", tup2[1:5])
    #元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')
        # 以下修改元组元素操作是非法的。
        # tup1[0] = 100
    # 创建一个新的元组
    tup3 = tup1 + tup2
    print (tup3)
    #元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
    tup = ('Google', 'Runoob', 1997, 2000)
    print (tup)
    del tup
        #报错
        #print("删除后的元组 tup : ")
        #print(tup)
    #与字符串一样，元组之间可以使用 + 号和 * 号进行运算。
    #这就意味着他们可以组合和复制，运算后会生成一个新的元组。
    tup = (1,2,3)
    print(len(tup))
    tup1 = (1,2,3)
    tup2 = (4,5,6)
    print(tup1+tup2)
    print(("Hi",)*4)
    print(3 in tup1)
    for i in tup2:
        print(i,)
    #因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，
    #也可以截取索引中的一段元素，如下所示：
    tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo','Weixin')
    print(tup[1]) #'Runoob'
    print(tup[-2]) #'Weibo'
    print(type(tup[-2])) # <class 'str'>
    print(tup[1:])#('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
    print(tup[1:4]) #('Runoob', 'Taobao', 'Wiki')
    #tuple(iterable)将可迭代系列转换为元组
    # 一定注意是 可迭代系列 的转换
    list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
    tuple1=tuple(list1)
    print(tuple1) #('Google', 'Taobao', 'Runoob', 'Baidu')
        #报错
        #a = 3
        #b = tuple(a)
        #print(b)
        #print(type(b))

    #关于元组是不可变的
    #所谓元组的不可变指的是元组所指向的内存中的内容不可变。
    tup = ('r', 'u', 'n', 'o', 'o', 'b')
        #tup[0] = 'g'     # 不支持修改元素
        #Traceback (most recent call last):
        #  File "<stdin>", line 1, in <module>
        #TypeError: 'tuple' object does not support item assignment
    print(id(tup))     # 查看内存地址
    tup = (1,2,3)
    print(id(tup))     # 内存地址不一样了
