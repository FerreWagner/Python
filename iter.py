

dt = {'a' : 9, 'b' : 8, 'c' : 7}
for key in dt.values():
    print(key)


for ch in 'Alexa':
    print(ch)



from collections import Iterable

print(isinstance(dt, Iterable))