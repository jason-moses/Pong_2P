from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import winsound

screen = Screen()
announcer = Turtle()
screen.tracer(0)
screen.colormode(255)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong PvP")

r_paddle = Paddle((350,0),(8,255,8))
l_paddle = Paddle((-350,0),(255,0,0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()


game_on = True

while game_on:
    screen.update()
    ball.move()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    time.sleep(ball.move_speed)

    #Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with each paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.paddle_bounce()
        winsound.Beep(500,100)

    #Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    #Check win conditions
    if scoreboard.l_score == 5:
        game_on = False
        announcer.color((255,0,0))
        announcer.write("Red Player Wins!", align="center", font=("Courier", 30, "normal"))

    if scoreboard.r_score == 5:
        game_on = False
        announcer.color((8,255,8))
        announcer.write("Green Player Wins!", align="center", font=("Courier", 30, "normal"))



screen.exitonclick()


