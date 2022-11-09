try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
finally:
    print('오류 일경우 그냥 넘어갔습니다')



class Bird:
    def fly(self):
        raise NotImplementedError # 오류를 일으킬 때 사용

class Eagle(Bird):
    pass


# eagle = Eagle()
# eagle.fly()

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")