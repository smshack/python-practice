from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b)

print('변수를 만드는 여러 가지 방법')

a, b = ('python', 'life')
print('a,b',a,b)
(a, b) = 'python', 'life'
print('a,b',a,b)
[a,b] = ['python', 'life']
print('a,b',a,b)
a = b = 'python'
print('a,b',a,b)

print('변수값 교환')
a=1
b=2
print('a,b',a,b)
a, b = b, a
print('a,b',a,b)
