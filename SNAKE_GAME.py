import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating Screen
screen = turtle.Screen()
screen.title("Snake Game 🐍")
screen.bgcolor("#2F4F4F")
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating Snake Head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")
snake_head.color("red")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Creating Snake Food
snake_food = turtle.Turtle()
snake_food.shape("circle")
snake_food.color("pink")  # Change food color to pink
snake_food.penup()
snake_food.goto(0, 100)

segments = []

# Creating Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Function to move the snake
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != 'up':
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != 'right':
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != 'left':
        snake_head.direction = "right"

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Check for a collision with the border
    if (snake_head.xcor() > 290) or (snake_head.xcor() < -290) or (snake_head.ycor() > 290) or (snake_head.ycor() < -290):
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset the score
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with snake food
    if snake_head.distance(snake_food) < 20:
        # Move snake food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        if len(segments) % 2 == 0:
            new_segment.color("white")
        else:
            new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head-body collision
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

screen.mainloop()
