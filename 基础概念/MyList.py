from collections import Counter

def reverseWords(input): 
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
    # 重新组合字符串
    output = ' '.join(inputWords) 
    return output 

def MyTest():
    #列表的数据项不需要具有相同的类型
    list1 = ['Google', 'Runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5 ]
    list3 = ["a", "b", "c", "d"]
    list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print("list1:",list1)
    print("list2:",list2)
    print("list3:",list3)
    print("list4:",list4)
    #访问列表中的值
    list1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print("list1:",list1)
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[-1])
    print(list1[-2])
    print(list1[-3])
    #列表元素的截取
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print("nums:",nums)
    print("nums[0:4]:",nums[0:4])
    list1 = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
    print("list1:",list1)
    # 读取第二位
    print ("list1[1]: ", list1[1])
    # 从第二位开始（包含）截取到倒数第二位（不包含）
    print ("list1[1:-2]: ", list1[1:-2])
    #列表的更新
    list1 = ['Google', 'Runoob', 1997, 2000]
    print("list1:",list1)
    print ("第三个元素为 : ", list1[2])
    list1[2] = 2001
    print ("更新后的第三个元素为 : ", list1[2])
    print("list1:",list1)
    #删除列表元素
    list1 = ['Google', 'Runoob', 1997, 2000]
    print ("原始列表 : ", list1)
    del list1[2]
    print ("删除第三个元素 : ", list1)
    #列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
    print(len([1, 2, 3]))
    print([1,2,3]+[4,5,"wjh"])
    print(['Hi!'] * 4)
    print(3 in [1, 2, 3])
    for x in [1, 2, 3]: print(x, end=" ")
    print()
    #列表拼接操作
    squares = [1, 4, 9, 16, 25]
    squares += [36, 49, 64, 81, 100]
    print(squares)
    print(len(squares))
    #嵌套列表
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x) # [['a', 'b', 'c'], [1, 2, 3]]
    print(x[0]) # ['a', 'b', 'c']
    print(x[0][1]) # 'b'
    #len(list)
    #列表元素个数
    list1 = ['Google', 'Runoob', 'Taobao']
    print(len(list1))
    list2=list(range(5)) # 创建一个 0-4 的列表
    print(len(list2))
    #max(list)
    #返回列表元素最大值
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print ("list1 最大元素值 : ", max(list1))
    print ("list2 最大元素值 : ", max(list2))
    #min(list)
    #返回列表元素最小值
    print ("list1 最小元素值 : ", min(list1))
    print ("list2 最小元素值 : ", min(list2))
    #list(seq)
    #将元组转换为列表
    aTuple = (123, 'Google', 'Runoob', 'Taobao')
    list1 = list(aTuple)
    print ("列表元素 : ", list1)
    str="Hello World"
    list2=list(str)
    print ("列表元素 : ", list2)
    #1
    #list.append(obj)
    #在列表末尾添加新的对象
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.append('Baidu')
    print ("更新后的列表 : ", list1)
    #2
    #list.count(obj)
    #统计某个元素在列表中出现的次数
    aList = [123, 'Google', 'Runoob', 'Taobao', 123];
    print ("123 元素个数 : ", aList.count(123))
    print ("Runoob 元素个数 : ", aList.count('Runoob'))
    #3
    #list.extend(seq)
    #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list1 = ['Google', 'Runoob', 'Taobao']
    list2=list(range(5)) # 创建 0-4 的列表
    list1.extend(list2)  # 扩展列表
    print ("扩展后的列表：", list1)
    #4
    #list.index(obj)
    #从列表中找出某个值第一个匹配项的索引位置
        #list.index(x[, start[, end]])
            #x-- 查找的对象。
            #start-- 可选，查找的起始位置。
            #end-- 可选，查找的结束位置。
    list1 = ['Google', 'Runoob', 'Taobao']
    print ('Runoob 索引值为', list1.index('Runoob'))
    print ('Taobao 索引值为', list1.index('Taobao'))
    print ('Taobao 索引值为', list1.index('Runoob',1))
    #5
    #list.insert(index, obj)
    #将对象插入列表
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.insert(1, 'Baidu')
    print ('列表插入元素后为 : ', list1)
    #6
    #list.pop([index=-1])
    #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.pop()
    print ("列表现在为 : ", list1)
    list1.pop(1)
    print ("列表现在为 : ", list1)
    #7
    #list.remove(obj)
    #移除列表中某个值的第一个匹配项
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.remove('Taobao')
    print ("列表现在为 : ", list1)
    list1.remove('Baidu')
    print ("列表现在为 : ", list1)
    #8
    #list.reverse()
    #反向列表中元素
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.reverse()
    print ("列表反转后: ", list1)
    #9
    #list.sort( key=None, reverse=False)
    #对原列表进行排序
    #reverse = True 降序， reverse = False 升序（默认）。
    aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
    aList.sort()
    print ( "List : ", aList)
    # 列表
    vowels = ['e', 'a', 'u', 'o', 'i']
    # 降序
    vowels.sort(reverse=True)
    # 输出结果
    print ( '降序输出:', vowels )
    # 获取列表的第二个元素
    def takeSecond(elem):
        return elem[1]
    # 列表
    ranL = [(2, 2), (3, 4), (4, 1), (1, 3)]
    # 指定第二个元素排序,默认升序
    #ranL.sort(key=takeSecond)
    #降序
    ranL.sort(key=takeSecond,reverse=True)
    # 输出类别
    print ('排序列表：', ranL)

    #10
    #list.clear()
    #清空列表
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.clear()
    print ("列表清空后 : ", list1)
    #11
    #list.copy()
    #复制列表，深拷贝
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list2 = list1.copy()
    print ("list2 列表: ", list2)
    list2[0] = "AAA"
    print ("list2 列表: ", list2)
    print("list1 列表:",list1)

def CounterTest():
    c = Counter('sadasfas')
    print(c)
    a=['su','bu','sum','bu','sum','bu']
    c = Counter(a)
    print(c)
    c.update('sadasfas') #添加
    print(c)