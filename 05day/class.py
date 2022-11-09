print('Calculator','='*50)
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print('FourCal','='*50)

class FourCal:
    # 생성자
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def setdata(self, first, second):
        self.first = first
        self.second = second
     def add(self):
        result = self.first + self.second
        return result
     def mul(self):
        result = self.first * self.second
        return result
     def sub(self):
        result = self.first - self.second
        return result
     def div(self):
        result = self.first / self.second
        return result
a = FourCal(4, 2)
print(a.first)
print(a.second)
print('더하기',a.add())
print('곱하기',a.mul())
print('빼기',a.sub())
print('나누기',a.div())

print('클래스의 상속','='*50)
print('기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.')
class MoreFourCal(FourCal):
     def pow(self):
         result = self.first ** self.second
         return result

b = MoreFourCal(4, 2)
print(b.pow())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
print('메서드 오버라이딩','='*50)
class SafeFourCal(FourCal):
     def div(self):
         if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
             return 0
         else:
             return self.first / self.second


a = SafeFourCal(4, 0)
print(a.div())