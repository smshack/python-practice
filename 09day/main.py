from turtle import Turtle, Screen

# 터틀 클래스 생성 변수에 저장 거북이 생성 기본으로 가운데 생성됨
timmy_the_turtle = Turtle()
# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”. 모양
timmy_the_turtle.shape("turtle")
# 모양의 색상
timmy_the_turtle.color("red","green")

# 모양의 진행 방향
for i in range(2,18):
    timmy_the_turtle.forward(50*i)
    timmy_the_turtle.right(90)
    

# 창이 켜짐
screan = Screen()

# 창을 클릭했을 경우 꺼짐
screan.exitonclick()