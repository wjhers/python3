'''
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
'''
import sys
def MyTest():
    aL = [1,2,3,4]
    it = iter(aL)
    print(next(it))
    print(next(it))

    #for循环遍历
    it = iter(aL)
    for x in it:
        print(x,end=" ")

    print()
    #while遍历
    it = iter(aL)
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()



























MyTest()
