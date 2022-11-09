import turtle as t
import random
# 터틀 클래스 생성 변수에 저장 거북이 생성 기본으로 가운데 생성됨
tim = t.Turtle()

color = ["red","orange",'yellow','green',"blue",'white']

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(color))
    draw_shape(shape_side_n)

# 창이 켜짐
screan = t.Screen()

# 창을 클릭했을 경우 꺼짐
screan.exitonclick()