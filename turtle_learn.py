import turtle
import winsound
import random

wn = turtle.Screen()
wn.title("Pong by kevin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
your_score = 0
Computer_score = 0

# LEft pad
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.shapesize(stretch_wid=4, stretch_len=1)
left_pad.color("white")
left_pad.penup()
left_pad.goto(-380, 0)

# right pad
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.shapesize(stretch_wid=4, stretch_len=1)
right_pad.color("white")
right_pad.penup()
right_pad.goto(380, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#score board
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0,270)
score_board.write("your score = {} Computer score = {}".format(your_score,Computer_score),align="center",font=("Arial",18,"normal"))


# function

def left_pad_up():
    y = left_pad.ycor()
    y += 10
    left_pad.sety(y)


def left_pad_down():
    y = left_pad.ycor()
    y -= 10
    left_pad.sety(y)


# keyboard intetrpritation
wn.listen()
wn.onkeypress(left_pad_up, "Up")
wn.onkeypress(left_pad_down, "Down")

# Main
while True:
    wn.update()
    # movie ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if(ball.xcor()>(random.randint(0,10)*100)):
        right_pad.sety(ball.ycor())


    # wall define
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 380 ):
        ball.setx(0)
        ball.sety(0)
        your_score += 1
        ball.dx *= -1
        score_board.clear()
        score_board.write("your score = {} Computer score = {}".format(your_score, Computer_score), align="center",
                          font=("Arial", 18, "normal"))
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)


    if (ball.xcor() < -380 ):
        ball.setx(0)
        ball.sety(0)
        Computer_score += 1
        ball.dx *= -1
        score_board.clear()
        score_board.write("your score = {} Computer score = {}".format(your_score, Computer_score), align="center",
                          font=("Arial", 18, "normal"))
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)

    #pad & ball collisation

    if((ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor()<right_pad.ycor() + 50  and ball.ycor()>right_pad.ycor() - 50)):
        ball.setx(360)
        winsound.PlaySound("attack.wav", winsound.SND_ASYNC)
        ball.dx *= -1

    if ((ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() - 50)):
        ball.setx(-360)
        winsound.PlaySound("attack.wav", winsound.SND_ASYNC)
        ball.dx *= -1
