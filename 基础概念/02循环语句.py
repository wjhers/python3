'''
python循环有for和while
'''
def MyTest():

    '''
    while循环
    '''
    n = 100
    ans = 0
    counter = 1
    while counter <= n:
        ans = ans + counter
        counter += 1
    print("1 到 %d 之和为:%d" % (n,ans))

    #while-else
    count=0
    while count < 5:
        print(count," 小于5")
        count +=1
    else:
        print(count," 大于或等于5")

    flag = 0
    while (flag): print ('欢迎访问菜鸟教程!')
    print ("Good bye!")

    '''
    for 语句
    Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串
    '''
    languages = ["C","C++","Perl","Python"]
    for x in languages:
        print(x)

    sites = ["Baidu", "Google","Runoob","Taobao"]
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程!")
            break
        print("循环数据 " + site)
    else:
        print("没有循环数据!")
    print("完成循环!")

    #range()函数
    for i in range(5): #[0 1 2 3 4]
        print(i)
    for i in range(5,9): #[5 6 7 8]
        print(i)

    for i in range(0,10,3): #[0,3,6,9]
        print(i)
    for i in range(-10,-100,-30): #[-10,-40,-70]
        print(i)

    a = ["A","B","C"]
    for i in range(len(a)):
        print(i,a[i])

    a = list(range(5))
    print(a)

    #continue语句被用来告诉python当前循环块中剩余语句，然后进行下一轮循环
    #break语句可以跳出当前for循环或者while循环的循环体
    sites = ["Goolge","Wiki","Weibo","Runoob"]
    for site in sites:
        if len(site)!=4:
            continue
        print(f"Hello,{site}")

        if site=="Runoob":
            break
    print("Done!")

    n=5
    while n >0:
        n-=1
        if n==2:
            break
        print(n)
    print("循环结束")

    #循环目标为字符串
    for letter in "Runoob":
        if letter =='b':
            break
        print("当前字母为:",letter)

    for letter in 'Runoob':
        if letter == 'o':
            continue
        print("当前字母为:",letter)

    #如下实例用于查询质数的循环例子:
    # for-else
    for n in range(2,10):
        for i in range(2,n):
            if n%i==0:
                print(n,"等于",i,"*",n//i)
                break
        else:
            print(n," 是质数")


    #    while True:
    #        pass
    for letter in 'Runoob': 
       if letter == 'o':
          pass
          print ('执行 pass 块')
       print ('当前字母 :', letter)
     
    print ("Good bye!")




    

    
    


MyTest()    
