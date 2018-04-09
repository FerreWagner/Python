#计算面积
def area(width, height):
    return width*height
print(area(10,20))


def feiwu():
    print("feiwu");

feiwu();


# 参数传递
# 变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象
# 以下代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型
a=[1,2,3]
print(a)
a="Runoob"
print(a)


# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)


# 可写函数说明
def printme(str = ''):
    "打印任何传入的字符串"
    print(str);
    return;


# 调用printme函数
printme('asd');



# 函数参数的使用不需要使用指定顺序
def fakeu(age, name):
    print(age);
    print(name);
    return;

fakeu(name='asd', age=1)


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);




# python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
action = lambda a,b: a - b; #减法匿名函数

print(action(10, 2));


fade1 = int(6.7);
print(fade1);



# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
numric = 12;
def newnum():
    global numric;
    print(numric);

    numric = 120;
    print(numric)

newnum();




def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

