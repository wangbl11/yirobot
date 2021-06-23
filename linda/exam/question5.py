import turtle

#初始化
turtle.setup()
turtle.clear()
turtle.color
turtle.fillcolor('blue')
turtle.speed(1)

#脸
turtle.pu()
turtle.goto(0,-200)
turtle.pd()
turtle.circle(200)

#左眼
turtle.pu()
turtle.goto(-100,50)
turtle.begin_fill()
turtle.pd()
turtle.circle(20)
turtle.end_fill()

#右眼
turtle.pu()
turtle.goto(100,50)
turtle.pd()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

#鼻子
turtle.pu()
turtle.goto(0,50)
turtle.pd()
turtle.circle(-50,360,3)

#嘴
turtle.pu()
turtle.goto(-150,-70)
turtle.pd()
turtle.goto(0,-170)
turtle.goto(150,-70)

turtle.exitonclick()