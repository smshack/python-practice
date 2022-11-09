def add(a, b): 
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

# 입력값 ---> 함수 ----> 결괏값


def say(): 
     return 'Hi' 

a = say()
print(a)

def add2(a, b): 
     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점

## 입력 값이 여러개가 될수 있을 경우
def add_many(*args): 
     result = 0 
     for i in args: 
         result = result + i 
     return result 

result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_mul(choice, *args): 
     if choice == "add": 
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
     return result 

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)


add = lambda a, b: a+b
result = add(3, 4)
print(result)