money = True
if money:
     print("택시를 타고 가라")
else:
     print("걸어 가라")


money = 2000
if money >= 3000:
     print("택시를 타고 가라")
else:
     print("걸어가라")

money = 2000
card = True
if money >= 3000 or card:
     print("택시를 타고 가라")
else:
     print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))

print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money'in pocket:
     print("택시를 타고 가라")
else:
     print("걸어가라")

pocket = ['paper', 'handphone']
card = True
if 'money'in pocket:
     print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
score = 50
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)