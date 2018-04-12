import math

# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现

# #  repr() 函数可以转义字符串中的特殊字符

hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

# # repr() 的参数可以是 Python 的任何对象
for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 另一个方法 zfill(), 它会在数字的左边填充 0
print('123'.zfill(5))

# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('heater', 'heater.fsociaty.com'))

# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
print('{0} 和 {1}'.format('me', 'u'))
print('{1} 和 {0}'.format('me', 'u'))

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{you}网址： {me}'.format(you='你', me='我'))

print('pi的值为：{0:.3f}asd'.format(math.pi))



table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:40} ==> {1:2d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))


# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串
print('常量 PI 的值近似为：%5.3f。' % math.pi)


# --------------------------------------------------------------------------------


# 读和写文件
# 打开一个文件
f = open("1.txt", "r+", encoding='utf-8')
# ut_str = 'leileleile'
# ut_str.encode('utf-8')
# f.write(ut_str)


# read_f = f.read()
# print(read_f)
# 关闭打开的文件
# f.close()


# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# str = f.readline()
# print(str)
# print(f.readlines())
for line in f:
    print(line, end='')

# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:使用str(value)函数
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数


# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。