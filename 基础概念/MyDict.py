#字典是另一种可变容器模型，且可存储任意类型对象。
#字典的每个键值 key=>value 对用冒号 : 分割，
#每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示： 
#d = {key1 : value1, key2 : value2, key3 : value3 }

#键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

#dict关键字

def MyTest():
    #print("wjh")
    dict1 = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
    print(dict1)
    dict1 = { 'abc': 456 }
    print(dict1)
    dict2 = { 'abc': 123, 98.6: 37 }
    print(dict2)
    #访问字典里的值
    #把相应的键放入到方括号中，如下实例:
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print ("dict1['Name']: ", dict1['Name'])
    print ("dict1['Age']: ", dict1['Age'])
        #如果用字典里没有的键访问数据，会输出错误如下：
        #print ("dict1['Alice']: ", dict1['Alice'])

    #修改字典
    #向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    dict1['Age'] = 8               # 更新 Age
    dict1['School'] = "菜鸟教程"  # 添加信息
    print ("dict1['Age']: ", dict1['Age'])
    print ("dict1['School']: ", dict1['School'])
    print(dict1)

    # 删除字典元素
    #能删单一的元素也能清空字典，清空只需一项操作。
    #显示删除一个字典用del命令，如下实例：
    del dict1['Name'] # 删除键 'Name'
    print(dict1)
    dict1.clear()     # 清空字典
        #报错
        #del dict         # 删除字典
        #print ("dict['Age']: ", dict['Age'])
        #print ("dict['School']: ", dict['School'])

    #字典键的特性
    #字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
    #两个重要的点需要记住：
    #1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
    print ("dict1['Name']: ", dict1['Name']) #dict1['Name']:  小菜鸟
    #2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
        #报错
        #dict1 = {['Name']: 'Runoob', 'Age': 7}
        #print ("dict1['Name']: ", dict1['Name'])

    #len(dict)
    #计算字典元素个数，即键的总数。
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(len(dict1))

    #str(dict)
    #输出字典，以可打印的字符串表示。
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(str(dict1))

    #type(variable)
    #返回输入的变量类型，如果变量是字典就返回字典类型。
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(type(dict1))

#测试内置函数
def MyTestFunction():
    #1
    #radiansdict.clear()
    #删除字典内所有元素 
    dict1 = {'Name': 'Zara', 'Age': 7}
    print("字典长度 : %d" %  len(dict1)) #类似于C语言的输出函数
    dict1.clear()
    print ("字典删除后长度 : %d" %  len(dict1))
    #2
    #radiansdict.copy()
    #返回一个字典的浅复制
    dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    dict2 = dict1.copy()
    print ("新复制的字典为 : ",dict2)
    #直接赋值和 copy 的区别
    dict1 =  {'user':'runoob','num':[1,2,3]}
    dict2 = dict1          # 浅拷贝: 引用对象
    dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    print("ddict1:",dict1)
    # 修改 data 数据
    dict1['user']='root'
    dict1['num'].remove(1)
    # 输出结果
    #实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，
    #dict3 父对象进行了深拷贝，不会随dict1 修改而修改，
    #子对象是浅拷贝所以随 dict1 的修改而修改。
    print(dict1)
    print(dict2)
    print(dict3)
    #3
    #radiansdict.fromkeys()
    #创建一个新字典，
    # 以序列 seq 中元素做字典的键， val 为字典 所有键 对应的初始值
    seq = ('name', 'age', 'sex')
    dict1 = dict1.fromkeys(seq)
    print ("新的字典为 : %s" %  str(dict1))
    dict1 = dict1.fromkeys(seq, 10)
    print ("新的字典为 : %s" %  str(dict1))
    x = ('key1', 'key2', 'key3')
    thisdict = dict.fromkeys(x)
    print(thisdict)
    #4
    #radiansdict.get(key, default=None)
    #返回指定键的值，如果键不在字典中返回 default 设置的默认值
    dict1 = {'Name': 'Runoob', 'Age': 27}
    print(dict1)
    print ("Age 值为 : %s" %  dict1.get('Age'))
    print ("Sex 值为 : %s" %  dict1.get('Sex', "没有这个值"))
    print ("Sex 值为 : %s" %  dict1.get('Sex'))
    #5
    #key in dict
    #如果键在字典dict里返回true，否则返回false
    dict1 = {'Name': 'Runoob', 'Age': 7}
    # 检测键 Age 是否存在
    if  'Age' in dict1:
        print("键 Age 存在")
    else :
        print("键 Age 不存在")
    # 检测键 Sex 是否存在
    if  'Sex' in dict1:
        print("键 Sex 存在")
    else :
        print("键 Sex 不存在")
    # not in
    # 检测键 Age 是否存在
    if  'Age' not in dict1:
        print("键 Age 不存在")
    else :
        print("键 Age 存在")

    #6
    #radiansdict.items()
    #以列表返回可遍历的(键, 值) 元组数组
    dict1 = {'Name': 'Runoob', 'Age': 7}
    print ("Value : %s" %  dict1.items())
        #报错？？？？
        #print(type(dict1.items())

    #7
    #radiansdict.keys()
    #返回一个迭代器，可以使用 list() 来转换为列表
    dict1 = {'Name': 'Runoob', 'Age': 7}
    print(dict1.keys()) # dict_keys(['Name', 'Age'])
    print(type(dict1.keys())) # <class 'dict_keys'>
    print(list(dict1.keys()))             # 转换为列表['Name', 'Age']


    #8
    #类似于添加元素
    #radiansdict.setdefault(key, default=None)
    #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    dict1 = {'Name': 'Runoob', 'Age': 7}
    print ("Age 键的值为 : %s" %  dict1.setdefault('Age', None))
    print ("Sex 键的值为 : %s" %  dict1.setdefault('Sex', None))
    print ("新字典为：", dict1)

    d={}  # 不设定
    d.setdefault('name','wjh')
    print(d)   # {'name':'wjh'}

    #9
    #radiansdict.update(dict2)
    #把字典dict2的键/值对更新到dict里
    #包含dict2覆盖dict1
    dict1 = {'Name': 'Runoob', 'Age': 7}
    dict2 = {'Sex': 'female' }
    dict1.update(dict2)
    print ("更新字典 dict1 : ", dict1)
    dict2 = {'Sex': 'female' ,'Age':88}
    dict1.update(dict2)
    print ("更新字典 dict1 : ", dict1)

    #10
    #radiansdict.values()
    #返回一个迭代器，可以使用 list() 来转换为列表
    dict1 = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
    print ("字典所有值为 : ",  list(dict1.values()))

    #11
    #pop(key[,default])
    #删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。
    #否则，返回default值。
    site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
    pop_obj=site.pop('name')
    print(pop_obj) #菜鸟教程
    
    #12
    #popitem()
    #随机返回并删除字典中的最后一对键和值。
    #返回一个键值对(key,value)形式，按照 LIFO（Last In First Out 后进先出法） 顺序规则，
    #即最末尾的键值对。

    site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
    pop_obj=site.popitem()
    print(pop_obj)   
    print(site)