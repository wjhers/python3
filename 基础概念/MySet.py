'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
def MyTest():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print(type(basket))
    print('orange' in basket)
    print('crabgrass' in basket)

    
    seta = set('aabbccddeeff') #{'e', 'c', 'd', 'f', 'b', 'a'} set中元素不能重复
    print(seta)
    setb = set('alacazam')

    
    print(setb)
    print(seta - setb)   # 集合a中包含而集合b中不包含的元素
    print(seta | setb)   # 集合a或b中包含的所有元素
    print(seta & setb)   # 集合a和b中都包含了的元素
    print(seta ^ setb)   # 不同时包含于a和b的元素
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)   #{'r', 'd'}

    
    #1、添加元素
    #语法格式如下：
    #s.add( x )
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.add("Facebook")
    print(thisset) #{'Taobao', 'Facebook', 'Google', 'Runoob'}    
    #还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，
    #语法格式如下：
    #s.update( x )
    seta = set(("Google","Runoob","TaoBao"))
    seta.update({1,3})
    print(seta)
    seta.update([1,4],[5,6])
    print(seta)

    
    #2、移除元素
    #语法格式如下：
    #s.remove()
    seta.remove("TaoBao")
    print(seta)
    #seta.remove("FaceBook") #不存在元素会发生错误
    #移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
    #s.discard( x )
    seta.discard("FaceBook")
    print(seta)
    #我们也可以设置随机删除集合中的一个元素，语法格式如下：
    #s.pop()
    #set 集合的 pop 方法会对集合进行无序的排列，
    #然后将这个无序排列集合的左面第一个元素进行删除。
    re = seta.pop()
    print(re)

    #3、计算集合元素个数
    #语法格式如下：
    #len(s)
    setb = set(("Goolge","Runoob","TaoBao"))
    print(len(setb))

    #4、清空集合，但是内存地址不删除
    #s.clear()
    setb.clear() 
    print(setb) #set()

    #add()
    fruits = {"apple","banana","cherry"}
    fruits.add("orange")
    print(fruits)

    #del()
    #del(fruits)
        #print(fruits) #报错

    #拷贝后内存地址发生了变化
    x = fruits.copy()
    
    print(x)
    print("id(x)=",id(x))
    print("id(fruits)=",id(fruits))
    #id(x)= 2311373165288
    #id(fruits)= 2311372767016

    #seta.difference(setb)元素包含在seta中不在setb中，返回一个新集合
    x = {"apple","banana","cheery"}
    y = {"google","apple","microsoft"}
    z = x.difference(y)
    print(z) #{'banana', 'cheery'}

    #difference_update()移除两个集合都包含的元素，直接在原集合上修改
    x.difference_update(y)#直接在集合x上修改
    print(x)

    #discard()删除指定元素，集合中没有该元素也不报错
    y.discard("AAA")
    print(y)

    #intersection() 返回集合的交集
    #set.intersection(set1, set2 ... etc)
    x = {"a","b","CC"}
    y = {"b","AA","CC"}
    z = x.intersection(y)
    print(z) #{'b', 'CC'}
    #多个集合的交集
    z = {"b","DD","EE"}
    re = x.intersection(y,z) #{"b"}
    print(re)

    #intersection_update()不用返回，直接在原集合上修改
    #set.intersection_update(set1, set2 ... etc)
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    x.intersection_update(y, z)
    print(x)

    #isdisjoint() 方法用于判断两个集合是否包含相同的元素，
    #如果 “没有”返回 True，否则返回 False。
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "facebook"}
    z = x.isdisjoint(y)
    print(z) #True

    #issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，
    #如果是则返回 True，否则返回 False。
    #set.issubset(set)
    x = {"a", "b", "c"}
    y = {"f", "e", "d", "c", "b", "a"}
    z = x.issubset(y)
    zz = y.issubset(x)
    print(z) #True
    print(zz)#False

    #issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，
    #如果是则返回 True，否则返回 False。
    #set.issuperset()
    z = y.issuperset(x) # y包含x
    print(z) #True

    #union() 方法返回两个集合的并集，
    #即包含了所有集合的元素，重复的元素只会出现一次。
    #set.union(set1, set2...)
    x = {"a", "b", "c"}
    y = {"f", "d", "a"}
    z = {"c", "d", "e"}
    result = x.union(y, z) 
    print(result) 

    #symmetric_difference()返回两个集合中不重复的元素的集合，
    #会移除两个集合中都存在的元素
    #set.symmetric_difference()
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y) #{'runoob', 'google', 'cherry', 'banana'}
    print(z)

    #symmetirc_difference_uodate()方法移除当前集合中在另外一个指定集合相同的元素，
    #并将另外一个指定集合中不同的元素插入到当前集合中。
    #set.symmetric_difference_update(set)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    x.symmetric_difference_update(y) #{'google', 'banana', 'runoob', 'cherry'}
    print(x)
    
    



    


MyTest()
