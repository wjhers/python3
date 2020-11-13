"""
在python中类型属于对象，变量是没有类型的，变量仅仅是一个指针，指向的类型可以变化
"""
a = [1,2,3]
a = "wjh"
a = 5

#不可变类型
print(id(a)) #1400532112
a = 10
print(id(a)) #1400532272

#可变类型
la = [1,2,3]
print(id(la)) #2098878033416
la[1]=4
print(id(la)) #2098878033416

"""
python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如 整数、字符串、元组。
           如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。
           如果在 fun(a)）内部修改 a 的值，则是新生成来一个 a。
可变类型：类似 C++ 的引用传递，如 列表，字典。
         如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
"""
def changeList(aL):
    aL[0] = aL[0] + 1
aL = [1,2,3,4]
changeList(aL)
print(aL) #[2, 2, 3, 4]

# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)

#以下实例中演示了函数参数的使用不需要使用指定顺序：
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )

#不定长参数,*tuple,**dict
def printmanyinfo(arg1,*vartuple):
    print(arg1)
    print("type(arg1):",type(arg1))
    print(vartuple)
    print("type(argtuple):",type(vartuple))

printmanyinfo(30,60,70)
print("----------------------------")
printmanyinfo(10)
#10
#type(arg1): <class 'int'>
#()
#type(argtuple): <class 'tuple'>

#**dict
def printInfoDict(arg1,**vardict):
    print(arg1)
    print(vardict)
    print("type(vardict):",type(vardict))
printInfoDict(1,a=2,b=3)

# 函数参数列表中有*,*号后的参数传递必须指明参数名称
def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=3))
#匿名函数
"""
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""
summ = lambda arg1,arg2:arg1*arg2
print(summ(10,10))

#return语句
"""
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
不带参数值的return语句返回None。
"""
def summ1(arg1,arg2):
    total = arg1 + arg2
    print("函数内:",total)
    return total
total = summ1(30,30)
print("函数外:",total)
