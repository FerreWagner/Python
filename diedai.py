# 可以直接作用于for循环的数据类型有以下几种：一类：list、tuple、dict、set、str等
# 另一类：generator,包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


# 简单点理解生成器就是一个迭代器
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行