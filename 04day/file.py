import numpy as np
import pandas as pd
import os 
# print(np)
# print(pd)
# f = open("새파일.txt", 'w')
# f.close()

print('='*50)
print('파일 이름, 파일 경로')
print('='*50)

print('현재 파일 전체 경로 이름\n',__file__)
print('realpath()는 심볼릭 링크 등의 실제 경로\n',os.path.realpath(__file__))
print('abspath는 파일의 절대경로를 리턴\n',os.path.abspath(__file__))

print('='*50)
print('현재 파일의 디렉토리(폴더) 경로')
print('='*50)

print('현재 파일의 디렉터리 경로(작업 폴더 기준)\n',os.getcwd())
print('os.path.dirname()는 파일의 폴더 경로를 리턴\n',os.path.dirname(os.path.realpath(__file__)))

print('='*50)
print('현재 디렉토리에 있는 파일 리스트')
print('='*50)
print(os.listdir(os.getcwd()))
print(os.listdir(os.path.dirname(os.path.realpath(__file__))))

print('='*50)
print('현재 디렉터리에 파일 쓰기')
print('='*50)
nowpath = os.path.dirname(os.path.realpath(__file__))
print('nowpath: ',nowpath)

print('='*50)
print('원하는 파일 읽기 readline, read')
print('='*50)
f = open(f"{nowpath}\\새파일.txt", 'w',encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open(f"{nowpath}\\새파일.txt", 'r',encoding='utf-8')
line = f.readline()
print(line)

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open(f"{nowpath}\\새파일.txt", 'r',encoding='utf-8')
data = f.read()
print(data)
f.close()

print('='*50)
print('파일에 새로운 내용 추가')
print('='*50)
f = open(f"{nowpath}\\새파일.txt", 'a',encoding='utf-8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
f = open(f"{nowpath}\\새파일.txt", 'r',encoding='utf-8')
data = f.read()
print(data)
f.close()

print('='*50)
print('with문과 함께 사용하기')
print('='*50)

f = open(f"{nowpath}\\새파일2.txt", 'w',encoding='utf-8')
f.write("Life is too short, you need python")
f.close()

with open(f"{nowpath}\\새파일3.txt", 'w',encoding='utf-8') as f:
    f.write("Life is too short, you need python")

