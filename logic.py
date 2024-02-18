import random
import tkinter as tk
import time


left_random = [(-50, 200, 1, 0), (-50, 250, 1, 0)]
right_random = [(450, 100, -1, 0), (450, 150, -1, 0)]
up_random = [(200, -50, 0, 1), (250, -50, 0, 1)]
down_random = [(100, 450, 0, -1), (150, 450, 0, -1)]


def draw_dotted_lines(canvas):
    # Draw dotted line from top middle to down middle
    canvas.create_line(200, 0, 200, 400, fill="black", width=3)

    # Draw dotted line from left middle to right middle
    canvas.create_line(150, 0, 150, 400, fill="black", dash=(2, 2))

    # Draw dotted line from left middle to right middle
    canvas.create_line(250, 0, 250, 400, fill="black", dash=(2, 2))

    # Draw dotted line from left middle to right middle
    canvas.create_line(0, 200, 400, 200, fill="black", width=3)

    canvas.create_line(0, 150, 400, 150, fill="black", dash=(2, 2))

    canvas.create_line(0, 250, 400, 250, fill="black", dash=(2, 2))


def draw_white_square(canvas):
    # Calculate the new coordinates for the bigger square
    x1 = 100
    y1 = 100
    x2 = 300
    y2 = 300

    # Draw the bigger white square
    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")


def draw_corner_squares(canvas):
    # Draw square in top left corner
    canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="black")

    # Draw square in top right corner
    canvas.create_rectangle(300, 0, 420, 100, fill="white", outline="black")

    # Draw square in bottom left corner
    canvas.create_rectangle(0, 300, 100, 400, fill="white", outline="black")

    # Draw square in bottom right corner
    canvas.create_rectangle(300, 300, 400, 400, fill="white", outline="black")


# Create the main window
window = tk.Tk()
window.title("Traffic Intersection")
window.configure(background="white")


last_spawn_time = 0


def spawn_car(event, direction):
    global last_spawn_time

    # Get the current time
    current_time = time.time()

    # Check if at least 1 second has passed since the last spawn
    if current_time - last_spawn_time >= 0.2:
        # Update the last spawn time
        last_spawn_time = current_time

        def define_direction(direction):
            match direction:
                case "UP":
                    x, y, xMove, yMove = random.choice(up_random)
                case "DOWN":
                    x, y, xMove, yMove = random.choice(down_random)
                case "LEFT":
                    x, y, xMove, yMove = random.choice(left_random)
                case "RIGHT":
                    x, y, xMove, yMove = random.choice(right_random)
            return x, y, xMove, yMove

        # Initial position of the circle
        x, y, xMove, yMove = define_direction(direction)

        # Create the circle
        circle = canvas.create_oval(x, y, x + 50, y + 50, fill="red")

        # Move the circle from left to right

        def move_circle():
            nonlocal x
            canvas.move(circle, xMove, yMove)

            # Smart car logic goes here
            x = xMove
            x += 5
            if x < 400:
                canvas.after(1, move_circle)
            else:
                canvas.delete(circle)

        # Start moving the circle
        move_circle()


window.bind("<Right>", lambda event: spawn_car(event, "LEFT"))
window.bind("<Left>", lambda event: spawn_car(event, "RIGHT"))
window.bind("<Up>", lambda event: spawn_car(event, "DOWN"))
window.bind("<Down>", lambda event: spawn_car(event, "UP"))

# Create the canvas
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# Draw the dotted lines and half squares
draw_dotted_lines(canvas)

draw_white_square(canvas)
draw_corner_squares(canvas)


# Lock the aspect ratio
window.resizable(False, False)
# Start the Tkinter event loop
window.mainloop()
