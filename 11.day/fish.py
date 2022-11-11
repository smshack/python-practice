from test.animal import Animal
class Fish(Animal):
    # 상속
    def __init__(self):
        super().__init__()

    # 오버라이딩
    def breathe(self):
        super().breathe()
        print('물 밖에서는 안되')

    def swim(self):
        print('헤엄친다 해엄쳐')


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)