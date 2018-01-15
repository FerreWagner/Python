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

L = ['Hello', 'World', 18, 'Apple', None]
for s in L:
    if isinstance(s, str):
        print(s)