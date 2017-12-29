# tuple: ()
# set  : ([])
# list : []
# dict : {k: v}


# d = {'you': 12, 'are': 23, 'my': 34, 'sunshine': 45}
# # print(d['you'])
# b = [6,5,4]
# s = set([1,2,8,6,4,b,'a'])
# s.add(123)
# s.remove(8)
# print(s)

# a = 123
# st = str(hex(a))
# print(st)



# print(hex(100))
# def hehe(x):
#     if x > 0:
#         print('谢特')
#     else :
#         print('好的')
#
# def hao():
#     pass


# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x


import math

# def mio(x, y, z = 0):
#     xz = x*math.cos(z)
#     yz = y*math.sin(z)
#     return xz, yz
#
# print(mio(10, 20, 0.5)) #反悔了一个tuple


# def x3(x, n = 3):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s*x
#
#     return s
#
# print(x3(9,2))

# def city(x, y, z = '小红'):
#     print('你:', x)
#     print('我:', y)
#     print('他:', z)
#
# city(z = '小倩',y = '小梦', x = '孟浩然')


# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
def fact(n):
    if n == 1:
        return 1
    return n * fact((n - 1))

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(100, 5))


