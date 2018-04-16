import os   #操作系统模块
import shutil
import glob #文件通配符  glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import re   #字符串正则匹配
import math #数学
import random   #random提供了生成随机数的工具。
from urllib.request import urlopen
import smtplib  #访问 互联网
from datetime import date   #日期和时间
import zlib #数据压缩

import doctest  #测试模块


print(os.getcwd())
# print(dir(os))

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:  shutil

print(glob.glob('*.py'))

# re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
print('tea for too'.replace('too', 'two'))


# math模块为浮点运算提供了对底层C函数库的访问:
print(math.cos(math.pi / 5))
print(math.log(1024, 2))

print(random.choice(['apple', 'pear', 'banana']))


#日期
now = date.today()
print(now)


#数据压缩
s = b'witch which has which witches wrist watch'
print(s.__len__())
print(len(s))


#测试模块
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

print(doctest.testmod())   # 自动验证嵌入测试