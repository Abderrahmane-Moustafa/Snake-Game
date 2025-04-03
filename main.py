from turtle import Screen, Turtle
from snake import Snake
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the window size
screen.bgcolor("black")              # Set background color
screen.title("My snake Game")        # Set window title
screen.tracer(0)                     # Turn off auto screen updates (for smoother animation)

# Create a snake object
snake = Snake()

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

# Close the window when clicked
screen.exitonclick()
