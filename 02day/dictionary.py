# 대응 관계를 나타낼 수 있는 자료형
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)

a = {1: 'a'}
print(a)
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3]
print(a)
ex = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
print(ex)
print(ex['김연아'])
print(ex['류현진'])

print('='*50)
print('딕셔너리 관련 함수')
print('='*50)

print('- keys key 리스트 만들기')
print(ex.keys())
print(list(ex.keys()))
for k in ex.keys():
    print(k)

print('- values value 리스트 만들기')
print(ex.values())
print(list(ex.values()))

print('- items  Key, Value 쌍 얻기')
print(ex.items())
print(list(ex.items()))

print('- get  Key로 Value얻기')
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nokey'))
print(a.get('foo', 'bar'))

print('- in 해당 key가 딕셔너리 안에 있는지 조사하기')
print('name' in a)