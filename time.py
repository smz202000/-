import turtle as t

import datetime as dt

import time

#画出背景

game=t.Screen()

game.bgcolor('black')

game.setup(600,600)

game.tracer(0)

#画圈

pen=t.Turtle()

pen.ht()

pen.speed(0)

pen.up()

pen.pensize(5)

def draw_clock(h,m,s):

    pen.clear()

    pen.up()

    pen.color('green')

    pen.goto(0,-210)

    pen.down()

    pen.seth(0)

    pen.circle(210)

    #画刻度

    pen.up()

    pen.goto(0,0)

    pen.seth(90)

    

    for _ in range(12):

        pen.forward(190)

        pen.down()

        pen.fd(20)

        pen.up()

        pen.goto(0,0)

        pen.rt(30)

    #画时针

    pen.up()

    pen.goto(0,0)

    pen.down()

    pen.seth(90)

    pen.rt(h/12*360)

    pen.color('white')

    pen.fd(80)

    #画分针和秒针

    pen.up()

    pen.goto(0,0)

    pen.down()

    pen.seth(90)

    pen.rt(m/60*360)

    pen.rt(30)

    pen.color('yellow')

    pen.fd(120)

 

    pen.up()

    pen.goto(0,0)

    pen.down()

    pen.seth(90)

    pen.rt(s/60*360)

    pen.rt(30)

    pen.color('blue')

    pen.fd(160)

 

    font=('Arial',20,'bold')

    hello='这个假期真长，今天都是{}年{}月{}日了。'.format(now.year,now.month,now.day)

    pen.up()

    pen.goto(-250,250)

    pen.color('red')

    pen.write(hello,'center',font=font)



 

now=dt.datetime.now()

draw_clock(now.hour,now.minute,now.second)

while True:

    game.update()

    time.sleep(1)

    now=dt.datetime.now()

    draw_clock(now.hour,now.minute,now.second)  

 

game.mainloop()
