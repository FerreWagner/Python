L = ['faith', 'sccc', 'moggy', 'kpii', 'kaka']

# c = L[0:4]  #L[0:4]表示，从索引0开始取，直到索引4为止，但不包括索引4
# c = L[:4]
# a = list(range(100))
# c = L[-2:]
# d = L[:]    #copy list L

# e = (0,9,8,7,6) #tuple cut

# print('ASDDSA'[:3]);    #string cut
# print('ABCDRF'[::2])       #2 step cut
# print(e[:3])



# iteration
# lis = [x * x for x in range(1, 11) if x % 2 == 0]
# mn  = [m + n for m in 'KIU' for n in 'POU']
# print(mn)

#列出所有文件名和目录名
# import os
# dd = [d for d in os.listdir('.')]
# print(dd)

# for循环其实可以同时使用两个甚至多个变量
# d = {'a':'A','b':'B','c':'C','d':'D'}
# for k,v in d.items():
#     print(k, '哈哈', v)

# 列表生成式也可以使用两个变量来生成list
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# uu = [k + '=' + v for k, v in d.items()]
# print(uu)

# L = ['Hello', 'World', 18, 'Apple', None]
# for s in L:
#     if isinstance(s, str):
#         print(s)



# 在Python中，一边循环一边计算的机制，称为生成器：generator。
# g = (x * x for x in range(20))
# for n in g:
#     print(n)


# Fibonacci
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#
# f = fib(10)
# print(f)




# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
#
#
# o = odd();
# print(next(o))
# print(next(o))
# print(next(o))


# 用for循环调用generator时，拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 普通函数直接返回结果,而生成器会返回一个对象