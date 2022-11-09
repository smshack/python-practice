# 불 자료형이란?
# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형
# - True - 참
# - False - 거짓
a = True
b = False

print(type(a))
print(type(b))
print('1 == 1', 1 == 1)
print('2 < 1',2 < 1)
print('python',bool('python'))
print('',bool(''))
print('[1,2,3]',bool(''))
print('[]',bool('[]'))
print(0,bool(0))
print(3,bool(3))

a = [1, 2, 3, 4]
while a:
     print(a.pop())