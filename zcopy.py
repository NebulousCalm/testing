import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightgreen")

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.shape("square")
sprite.goto(-1000,1000)

running = False

snake = []

def update():
    if running:
        screen.ontimer(update, 350) # call update again after 350 milliseconds

def create_body(x,y):
    body = sprite.clone() # create a body from the sprite object
    body.goto(x,y)
    snake.append(body) # add the body segment to snake list

def start_game():
    global running
    running = True
    create_body(0,0) # add this line to create a body at (0,0)
    update()

dir = "Right" # snake initially points right
def move():
    first = snake[0] # get the head of the snake
    last = snake[len(snake)-1] # get the tail of the snake
    x = first.xcor() 
    y = first.ycor()
    size = 22 # length of the snake
    last.goto((x + (size)),y) # place the tail in front of the head
    snake.insert(0,last) # make the tail the new head
    snake.pop() # remove the tail
def update():
    if running:
        move() # add this line
        screen.ontimer(update, 350)
def up():
    global dir
    if(not dir == "Down"):
        dir = "Up"
def down():
    global dir
    if(not dir == "Up"):
        dir = "Down"
def left():
    global dir
    if(not dir == "Right"):
        dir = "Left"
def right():
    global dir
    if(not dir == "Left"):
        dir = "Right"
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
if(dir == "Down"):
        last.goto(x, y - (size))  # move downward, codetract from y
elif(dir == "Left"):
        last.goto((x - (size)),y) # move left, codetract from x
elif(dir == "Up"):
        last.goto(x, y + (size))  # move upward, add to y
def move():
    last = snake[len(snake)-1]
    first = snake[0]
    x = first.xcor()
    y = first.ycor()
    size = 22
    if(dir == "Down"):
        last.goto(x, y - (size))
    elif(dir == "Left"):
        last.goto((x - (size)),y)
    elif(dir == "Up"):
        last.goto(x, y + (size))
    else:
        last.goto((x + (size)),y)
    snake.insert(0,last)
    snake.pop()
food = None
def create_food():
    global food
    food = sprite.clone()             # create the food object
    food.color("red")                 # change it to red
    randX = random.randint(-8,8) * 22 # choose a random location
    randY = random.randint(-8,8) * 22
    food.goto(randX,randY)            # go to the location
    first = snake[0]
    x = first.xcor()
    y = first.ycor()
    if(x == food.xcor() and y == food.ycor()):
            create_body(x, y)
            food.hideturtle()
            create_food()
    else:
        last.goto((x + (size)),y) # move right, add to x

start_game()
