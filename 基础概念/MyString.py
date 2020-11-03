
#测试一些字符串的样例
def MyTest():
    #字符串中字符索引从0开始计数
    var1 = "Hello World!"
    var2 = "Runoob"
    #原字符串
    print("var1:",var1)
    print("var2:",var2)
    #获取字符串中固定位置的值
    print("var1[0]:",var1[0])
    #字符串取值左闭右开
    print("var2[1:5]:",var2[1:5])
    #字符串中字符索引可以为负
    print("var2[-1]:",var2[-1])
    #-5到-4其实就是取的是-5处的元素
    print("var2[-5:-4]:",var2[-5:-4])
    #字符串拼接 
    print("var1[:6]+'Runoob!':",var1[:6]+'Runoob!')

    #子串的判断
    a = var1;
    if( "H" in a) :
        print("H 在变量 a 中")
    else :
        print("H 不在变量 a 中")
 
    if( "M" not in a) :
        print("M 不在变量 a 中")
    else :
        print("M 在变量 a 中")
 
    #原生字符串：不转义任何字符
    print (r'\n')
    print (R'\n')

    #字符串格式化
    print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

    #f-string
    name = "wjh"
    strr = 'hello %s'%name
    print(strr)
    #f函数+{}的使用
    new = f'hello {name}'
    print(new)
    c = f'{1+2}'
    print(c)
    w = {'name': 'Runoob', 'url': 'www.runoob.com'}
    n = f'{w["name"]}: {w["url"]}'
    print(n)

def MyTestFunction():
    #str.capitalize()
    #将字符串的第一个字符转换为大写
    str="hello PYTHON";
    str.capitalize()
    print(str)
    str="123 hello PYTHON"
    str.capitalize()
    print(str)
    str="@ Hello PYTHON"
    str.capitalize()
    print(str)

    #str.find(str, beg=0, end=len(string))
    #如果包含子字符串返回开始的索引值，否则返回-1。
    str1 = "Runoob example....wow!!!"
    str2 = "exam";
    print (str1.find(str2))
    print (str1.find(str2, 5))
    print (str1.find(str2, 10))

    #str.isdigit()
    #如果字符串只包含数字则返回 True 否则返回 False。
    str = "123456";
    print (str.isdigit())

    str = "Runoob example....wow!!!"
    print (str.isdigit())

    #str.isspace()
    #如果字符串中只包含空格，则返回 True，否则返回 False.
    str = "       " 
    print (str.isspace())
 
    str = "Runoob example....wow!!!"
    print (str.isspace())

    #str.replace(old, new[, max])
    #返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
    str = "www.w3cschool.cc"
    print ("菜鸟教程旧地址：", str)
    print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
 
    str = "igigigigigigig!!"
    print (str.replace("ig", "IG", 3))

    #str.rstrip([chars])
    #rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
    str = "     this is string example....wow!!!     "
    print (str.rstrip())
    str = "*****this is string example....wow!!!*****"
    print (str.rstrip('*'))

    #str.split(str="", num=string.count(str))
    #split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
    #分割后，指定的字符消失
    str = "this is string example....wow!!!"
    print (str.split( ))       # 以空格为分隔符
    print (str.split('i',1))   # 以 i 为分隔符
    print (str.split('w'))     # 以 w 为分隔符
    '''
    ['this', 'is', 'string', 'example....wow!!!']
    ['th', 's is string example....wow!!!']
    ['this is string example....', 'o', '!!!']
    '''
    txt = "Google#Runoob#Taobao#Facebook"
    # 第二个参数为 1，返回两个参数列表
    x = txt.split("#", 1)
    print(x)
    #['Google', 'Runoob#Taobao#Facebook']

    #str.swapcase();
    #将字符串中大写转换为小写，小写转换为大写
    str = "this is string example....wow!!!"
    print (str.swapcase())
    str = "This Is String Example....WOW!!!"
    print (str.swapcase())
    	
    #upper()
    #转换字符串中的小写字母为大写
    str = "wjh"
    print(str.upper())
    #lower()
    #转换字符串中所有大写字符为小写.
    str = "Runoob EXAMPLE....WOW!!!"
    print(str.lower())

def URL_Split():
    #!/usr/bin/python3
    url = "http://www.baidu.com/python/image/123456.jpg"
    #以“.” 进行分隔
    path =url.split(".")
    print(path) # ['http://www', 'baidu', 'com/python/image/123456', 'jpg']
    path = url.split('/')
    print(path) # ['http:', '', 'www.baidu.com', 'python', 'image', '123456.jpg']
    #我们在学习 python 爬虫的时候例如需要保存图片，图片名称的获取，可以依照下列方法：
    path =url.split("/")[-1]
    print(path) # '123456.jpg'
