'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
===========================================================
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
'''
# 在Python中没有switch – case语句。
def MyTest():
    var1 = 100
    if var1:
        print("1-if表达式条件为真")
        print(var1)
    var2  = 0
    if var2:
        print("2-if表达式条件为真")
        print(var2)
    print("Good bye!")

    age = int(input("请输入你家狗的年龄:"))
    print("")
    if age <= 0:
        print("你是在逗我吧")
    elif age==1:
        print("相当于14岁的人")
    elif age==2:
        print("相当于22岁的人")
    elif age>2:
        human = 22 + (age-2)*5
        print("对应人类的年龄:",human)

    print("点击enter键退出")

    '''
    <	小于
    <=	小于或等于
    >	大于
    >=	大于或等于
    ==	等于，比较两个值是否相等
    !=	不等于
    '''
    print(5==6)
    x = 5
    y = 8
    print(x==y)

    #猜数字
    number=7
    guess=-1
    while guess!=number:
        guess=int(input("请输入你猜的数字:"))
        if guess==number:
            print("恭喜你猜对了")
        elif guess<number:
            print("猜的数字小了...")
        elif guess>number:
            print("猜的数字大了...")

    # 条件语句嵌套
    '''
    if 表达式1:
        语句
        if 表达式2:
            语句
        elif 表达式3:
            语句
        else:
            语句
    elif 表达式4:
        语句
    else:
        语句
    '''
    num = int(input("输入一个数字:"))
    if num%2==0:
        if num%3==0:
            print("你输入的数字既可以整除2也可以整除3")
        else:
            print("你输入的数字既可以整除2,不能整除3")
    else:
        if num%3==0:
            print("你输入的数字既可以整除3,不能整除2")
        else:
            print("你输入的数字不能整除2也不能整除3")








MyTest()


















    
