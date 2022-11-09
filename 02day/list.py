odd = [1, 3, 5, 7, 9]
print(odd)

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a)
print(b)
print(c)
print(d)
print(e)

print("=" * 50)
print('리스트의 슬라이싱')
print("=" * 50)
a = [1, 2, 3, 4, 5]
print(a[0:2])

a = [1, 2, 3]
b = [4, 5, 6]
print('- 리스트 더하기(+) [] + []')
print(a + b)

print('- 리스트 반복하기(*)')
print(a * 3)

print('- len 리스트 길이 구하기')
print(len(a))


print("=" * 50)
print('리스트의 수정과 삭제')
print("=" * 50)
a = [1, 2, 3]
a[2] = 4
print(a)
del a[1]
print(a)
a = [1, 2, 3, 4, 5]
print(a)
del a[2:]
print(a)

print("=" * 50)
print('리스트 관련 함수')
print("=" * 50)

print('- append 리스트에 요소 추가-------')
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)
print('- sort 리스트에 정렬 추가-------')
a = [1, 4, 3, 2]
print(a)
a.sort()
print(a)
print('- reverse 리스트 뒤집기-----')
a = ['a', 'c', 'b']
a.reverse()
print(a)

print('- index 위치 반환-------')
a = [1,2,3]
print(a.index(3))

print('- insert 리스트에 요소 삽입-------')
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

print('- remove 리스트에 요소 제거------- 값을 2개 가지고 있을 경우 첫 번째 검색된 값만 제거')
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

print('- pop 리스트 요소 끄집어내기-------')
a = [1,2,3]
b = a.pop()
print(a)
print(b)
a = [1,2,3]
b = a.pop(1)
print(a)
print(b)

print('- pop 리스트에 포함된 요소 x의 개수 세기-------')
a = [1,2,3,1]
print(a.count(1))

print('- extend 리스트의 확장-------')
a = [1,2,3]
a.extend([4,5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
