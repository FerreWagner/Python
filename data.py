# py中列表可以修改，而字符串和元组不能


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])




vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])


# 列表推导式可以使用复杂表达式或嵌套函数：
print([str(round(355/113, i)) for i in range(1, 6)])



# 嵌套列表解析
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])


# del语句：按照列表的索引来删除列表中的元素
kkk = [-1, 1, 66.25, 333, 331, 1234.5]
del kkk[2:4]
print(kkk)


# 也可以用 del 删除实体变量：
del kkk
# print(kkk)   此时打印会报错：kkk is not defined

# -----------------------------------------------------------------------------------

# 元组和序列   元组由若干逗号分隔的值组成
t = 12345, 54321, 'hello!'
print(t)

tt = t, (9,8,7)
print(tt)
# 元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的

# ----------------------------------------------------------------------------------

# 集合 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)


aa = set('abracadabra')
bb = set('alacazam')

print(aa - bb) # 在 sa 中的字母，但不在 bb 中
print(aa | bb) # 在 sa 或 bb 中的字母
print(aa & bb) # 在 aa 和 bb 中都有的字母
print(aa ^ bb) #在 aa 或 bb 中的字母，但不同时在 aa 和 bb 中

# 集合也支持推导式
sun = {x for x in 'abracadabra' if x not in 'abc'}
print(sun)

# 字典 在同一个字典之内，关键字必须是互不相同
tel = {'sape': 40198, 'jake': 4139}
print(list(tel.keys()))
print(sorted(tel.keys()))

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
dict_name = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict_name)

poem = {x: x**2 for x in (2, 4, 6)}
print(poem)

str_dict = dict(sape=4139, guido=4127, jack=4098)
print(str_dict)

forea = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in forea.items():    #在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
     print(k, v)


# -----------------------------------------------------------------------------------------------------------

for i, v in enumerate(['tic', 'tac', 'toe']):     #在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
     print(i, v)



# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))


# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 10, 2)):
     print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
babyb = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(babyb)):
     print(f)