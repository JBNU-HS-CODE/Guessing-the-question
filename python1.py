import turtle

vector=input("벡터의 X좌표, Y좌표를 입력하세요.").split()
X =int(vector[0])
Y =int(vector[1])

a = int(input("벡터의 속도를 입력하세요."))

t = turtle.Turtle()
t.speed(a)

scale=20

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("blue") #색 상관 없음.
t.goto(X *scale, Y *scale)

t.penup()
t.goto(X *scale +5, Y *scale +5)
t.write(f"({X}, {Y})")

turtle.done()