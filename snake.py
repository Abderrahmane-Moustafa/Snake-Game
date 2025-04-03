from turtle import Turtle, Screen

# Constants for the game
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20                                # Distance the snake moves per step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []     # List to hold all segments of the snake
        self.create_snake()    # Initialize the snake on creation

    def create_snake(self):
        # Create the initial snake by adding segments at defined positions
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")  # Create a square-shaped turtle segment
            new_segment.color("white")      # Set segment color to white
            new_segment.penup()             # Prevent drawing lines when the segment moves
            new_segment.goto(position)      # Move the segment to the starting position
            self.segments.append(new_segment)

    def move(self):
        # Move the snake by shifting each segment to the position of the one in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        # Change direction to UP unless currently moving DOWN
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        # Change direction to DOWN unless currently moving UP
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        # Change direction to LEFT unless currently moving RIGHT
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        # Change direction to RIGHT unless currently moving LEFT
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
