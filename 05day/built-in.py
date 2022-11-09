print('='*50)
print('abs 절대값 반환')
print('abs(-4)',abs(-4))
print('abs(5)',abs(5))
print('abs(0)',abs(0))
print('='*50)
print('all 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준')
print('all([1, 2, 3])',all([1, 2, 3]))
print('all((1, 2, 3))',all((1, 2, 3)))
print('all([1, 2, 3,0])',all([1, 2, 3,0]))
print('all([])',all([]))
print('='*50)
print('any  반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False')
print('any([1, 2, 3])',any([1, 2, 3]))
print('any((1, 2, 3))',any((1, 2, 3)))
print('any([1, 2, 3,0])',any([1, 2, 3,0]))
print('any([])',any([]))
print('='*50)
print('chr 유니코드(Unicode) 값을 입력받아 그 코드에 해당하는 문자를 출력')
print('chr(97)',chr(97))
print('chr(44032)',chr(44032))
print('='*50)
print('dir 객체가 자체적으로 가지고 있는 변수나 함수를 보여 줌')
print('dir([1, 2, 3])\n',dir([1, 2, 3]))
print("dir({'1':'a'})\n",dir({'1':'a'}))
print('='*50)
print('divmod divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수')
print('몫','나머지')
print("divmod(7, 3)")
print(divmod(7, 3))
print('='*50)
print('enumerate 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다')
print('※ 보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용한다.')
print("['body', 'foo', 'bar']",['body', 'foo', 'bar'])
print("enumerate(['body', 'foo', 'bar'])",enumerate(['body', 'foo', 'bar']))
for i, name in enumerate(['body', 'foo', 'bar']):
     print(i, name)
print('for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할때 enumerate 함수를 사용하면 매우 유용')
print('='*50)
print("eval 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수")
print("eval('1+2')",eval('1+2'))
print("eval("'hi' + 'a'")",eval("'hi' + 'a'"))
print("eval('divmod(4, 3)')",eval('divmod(4, 3)'))
print('='*50)
print("filter 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려줌")
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
print('='*50)
print('hex 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수')
print('hex(234)',hex(234))
print('hex(3)',hex(3))

print('='*50)
print('id 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수')
a = 3
b = a
print('id(3)',id(3))
print('id(a)',id(a))
print('id(b)',id(b))

print('='*50)
print('input 사용자 입력을 받는 함수이다. 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.')
# b = input("Enter: ")
# print(b)

print('='*50)
print('int  문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.')
print(int('3'))
print(int(3.4))
print(int(3.12345))

print('='*50)
print('isinstance   첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름')
print('입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.')
class Person: pass
a = Person()
print('isinstance(a, Person)',isinstance(a, Person))
print('isinstance(b, Person)',isinstance(b, Person))

print('='*50)
print('len(s)  입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수')
print('len("python")',len("python"))
print('len([1,2,3])',len([1,2,3]))
print('len((1, "a"))',len((1, 'a')))

print('='*50)
print('list   반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수')
print('list("python")',list("python"))

print('='*50)
print('map(f, iterable)   함수(f)와 반복 가능한(iterable) 자료형을 입력')
print('입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수')
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)
def two_times(x): 
     return x*2
list(map(two_times, [1, 2, 3, 4]))

print(list(map(lambda a: a*2, [1, 2, 3, 4])),'list(map(lambda a: a*2, [1, 2, 3, 4]))')

print('='*50)
print('max 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수')
print('max([1, 2, 3])',max([1, 2, 3]))
print('max("python")',max("python"))

print('='*50)
print('min max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수')
print('min([1, 2, 3])',min([1, 2, 3]))
print('min("python")',min("python"))

print('='*50)
print('ord 문자의 유니코드 값을 돌려주는 함수')
print('※ ord 함수는 chr 함수와 반대이다.')
print("ord('a')",ord('a'))
print("ord('가')",ord('가'))

print('='*50)
print('pow(x, y) x의 y 제곱한 결괏값을 돌려주는 함수')
print('pow(3, 3)',pow(3, 3))
print('pow(2, 4)',pow(2, 4))
print('2**4',2**4)

print('='*50)
print('range  range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. ')
print('이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.')
print('list(range(5))',list(range(5)))
print('list(range(5, 10))',list(range(5, 10)))
print('list(range(1, 10, 2))',list(range(1, 10, 2)))

print('='*50)
print('round(number[, ndigits])  숫자를 입력받아 반올림해 주는 함수')
print('round(4.6)',round(4.6))
print('round(3.2)',round(3.2))
print('round(-3.2)',round(-3.2))

print('='*50)
print('sorted(iterable) 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수')
print('sorted([3, 1, 2])',sorted([3, 1, 2]))
print("sorted(['a', 'c', 'b']",sorted(['a', 'c', 'b']))
print('sorted("zero")',sorted("zero"))

print('='*50)
print('str 문자열 형태로 객체를 변환하여 돌려주는 함수')
print('str(3)',str(3))
print('type(str(3))',type(str(3)))

print('='*50)
print('str 문자열 형태로 객체를 변환하여 돌려주는 함수')
print('sum([1,2,3])',sum([1,2,3]))
print('sum((4,5,6))',sum((4,5,6)))

print('='*50)
print('tuple 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수')
print('tuple("abc")',tuple("abc"))
print('tuple([1, 2, 3])',tuple([1, 2, 3]))
print('tuple((1, 2, 3))',tuple((1, 2, 3)))

print('='*50)
print('type 입력값의 자료형이 무엇인지 알려 주는 함수')
print('type("abc")',type("abc"))
print('type([ ])',type([ ]))
print('type(open("test", "w"))',type(open("test", "w")))


print('='*50)
print('zip(*iterable) 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수')
print('※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미')
print('list(zip([1, 2, 3], [4, 5, 6]))',list(zip([1, 2, 3], [4, 5, 6])))
print('list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))',list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print('list(zip("abc", "def"))',list(zip("abc", "def")))