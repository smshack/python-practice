import sys # 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import pickle # 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import os # 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
import shutil # 파일을 복사해주는 모듈
import glob # 특정 디렉터리에 있는 파일 이름 모두를 알아야 할경우
import tempfile # 파일을 임시로 만들어서 사용할 때 유용한 모듈 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
import time # 시간과 관련된 time 모듈에는 함수가 광장히 많음 
import calendar # 달력을 볼수 있게 해주는 모듈
import random # 난수를 발생시키는 모듈
import webbrowser # 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
import threading # 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행 가능
print('sys.argv',sys.argv)
for i in sys.path:
    print(i)
sys.path.append("c:\\Users\\jerry\\Documents\\python\\audio_streaming_google\\pythonpractice\\04day")
print('='*50)
print('sys # 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈')
from module import *
print(add(4,5))
print(sub(4,5))

a= Math()
print(a.solv(4))
nowpath = os.path.dirname(os.path.realpath(__file__))
print('='*50)
print('# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈')
f = open(f"{nowpath}\\test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open(f"{nowpath}\\test.txt", 'rb')
data = pickle.load(f)
print(data)

# print('os.environ',os.environ)
for key, value in os.environ.items():
    print('{}: {}'.format(key, value))

print('='*50)
print('os # 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈')
print('='*50)
print("shutil # 파일을 복사해주는 모듈")
shutil.copy(f"{nowpath}\\test.txt", f"{nowpath}\\test2.txt")
print('='*50)
print("glob # 특정 디렉터리에 있는 파일 이름 모두를 알아야 할경우")
print('glob.glob(f"{nowpath}")',glob.glob(f"{nowpath}"))
for idx, val in enumerate(glob.glob(f"{nowpath}\\*")):
    print(idx, val)
print('='*50)
print("tempfile # 파일을 임시로 만들어서 사용할 때 유용한 모듈 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌")
print('tempfile.mkstemp()',tempfile.mkstemp())
print('='*50)
print("time # 시간과 관련된 time 모듈에는 함수가 광장히 많음 ")
print('time.time()',time.time())
print('time.localtime(time.time())',time.localtime(time.time()))
print('time.asctime(time.localtime(time.time()))',time.asctime(time.localtime(time.time())))
print('time.ctime()',time.ctime())
print("time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))")
import time
for i in range(10):
    print(i)
    time.sleep(0.01)
print('='*50)
print("calendar # 달력을 볼수 있게 해주는 모듈")
print('calendar.calendar(2015)',calendar.calendar(2015))
print('calendar.weekday(2015, 12, 31)',calendar.weekday(2015, 12, 31))
print('calendar.monthrange(2015,12)',calendar.monthrange(2015,12))
print('='*50)
print("random # 난수를 발생시키는 모듈")
print('random.random()',random.random())
print('random.randint(1, 10)',random.randint(1, 10))
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    print(number)
    return number
random_pop([1, 2, 3, 4, 5])

print('='*50)
print("webbrowser # 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈")
webbrowser.open("http://google.com")
print('='*50)
print("threading # 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행 가능")
def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
            time.sleep(1)  # 1초간 대기한다.
            print("working:%s\n" % i)

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")