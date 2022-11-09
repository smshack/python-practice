s1 = set([1,2,3])
print('s1',s1)
s2 = set("Hello")
print('s2',s2)
# 집합 자료형의 특징
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('='*50)
print('교집합 , 합집합, 차집합')
print('='*50)
print('s1',s1)
print('s2',s2)
print(' - 교집합 &')
print('s1 & s2', s1 & s2)
print(' - 합집합 |')
print('s1 | s2', s1 | s2)
print(' - 합집합 -')
print('s1 - s2', s1 - s2)

print('='*50)
print('집합 자료형 관련 함수들')
print('='*50)
s1 = set([1, 2, 3])
print('s1',s1)
print( s1.add(4))
print('- add 값 한개 추가')
print('s1',s1)

print('- update 값 여러개 추가')
s1.update([4, 5, 6])
print('s1',s1)

print('- remove 특정 값 제거하기')
s1.remove(2)
print('s1',s1)
