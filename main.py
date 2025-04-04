from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the window size
screen.bgcolor("black")              # Set background color
screen.title("My snake Game")        # Set window title
screen.tracer(0)                     # Turn off auto screen updates (for smoother animation)

# Create a snake object
snake = Snake()
food = Food()
score = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")     # Move snake up
screen.onkey(snake.down, "Down") # Move snake down
screen.onkey(snake.left, "Left") # Move snake left
screen.onkey(snake.right, "Right")# Move snake right

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()          # Manually update the screen
    time.sleep(0.1)          # Pause to control the speed of the game
    snake.move()             # Move the snake forward

    #Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() <-280:
        game_is_on = False
        score.clear()
        score.game_over()

    # Detect collision with wall
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

# Close the window when clicked
screen.exitonclick()
