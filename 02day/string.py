print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

multiline="""
Life is too short
You need python
"""

print(multiline)

head = "Python"
tail = " is fun!"
print(head + tail)
print(head*2)
print("=" * 50)
print("My Program")
print("=" * 50)

print("=" * 50)
print('문자열 인덱싱 활용 슬라이싱')
print("=" * 50)
a = "Life is too short, You need Python"
print(a[3])
print(a[0:4])
# 0<= a < 4
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:])
print(a[19:-7])


print("=" * 50)
print(' 자주 사용하게 되는 슬라이싱 기법 ')
print("=" * 50)

a = "20010331Rainy"
print(a)
date = a[:8]
weather = a[8:]
print(date)

print(weather)

print("=" * 50)
print('문자열 포맷팅')
print("=" * 50)
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("I eat {0} apples".format(3))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
x = 1
y = 2
print(f"{x} + {y}는 {x + y}입니다.")
word = "Python"
print(f"{word}는 {len(word)}글자입니다.")
print(f"대문자로는 {word.upper()}이고, 소문자로는 {word.lower()}입니다.")


print("=" * 50)
print('왼쪽 정렬')
print("=" * 50)
print("{0:<10}".format("hi"))
print("{0:<10}".format("hello"))
print("{0:<10}".format("world"))

print("=" * 50)
print('오른쪽 정렬')
print("=" * 50)
print("{0:>10}".format("hi"))
print("{0:>10}".format("hello"))
print("{0:>10}".format("world"))

print("=" * 50)
print('가운데 정렬')
print("=" * 50)
print("{0:^10}".format("hi"))
print("{0:^10}".format("hello"))
print("{0:^10}".format("world"))

print("=" * 50)
print('공백채우기 정렬')
print("=" * 50)
print("{0:=^10}".format("hi"))
print("{0:=^10}".format("hello"))
print("{0:=^10}".format("world"))

print("=" * 50)
print('소수점 표현')
print("=" * 50)
y = 3.42134234
print("{0:0.4f}".format(y))

print("=" * 50)
print('f 문자열 포매팅')
print("=" * 50)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

print("=" * 50)
print('문자열 관련 함수')
print("=" * 50)

print('- count 문자 개수 세기(일치하는 문자 개수)')
a = 'hobby'
print(a.count('b'))
print('- find 위치 알려주기')

a = "Python is the best choice"
print(a.find('b'))
print(a.find('P'))
print(a.find('e'))
print(a.find('k'))

print('- index 위치 알려주기')
a = "Life is too short"
print(a.index('t'))

print('- join 문자열 삽입')
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

print('- upper 소문자를 대문자로 바꾸기')
print(a.upper())
print('- lower 대문자를 소문자로 바꾸기')
print(a.lower())

print('- strip 공백지우기 (왼쪽\오른쪽\양쪽)')
a = " hi "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

print('- replace 문자열 바꾸기')
a = "Life is too short"
print(a.replace("Life", "Your leg"))

print('- split 문자열 나누기')
a = "Life is too short"
print(a.split())
print(a)
b = "a:b:c:d"
print(b.split(':'))
