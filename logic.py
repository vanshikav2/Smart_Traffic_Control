import random
import tkinter as tk
import time


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


def spawn_circle(event):
    global last_spawn_time

    # Get the current time
    current_time = time.time()

    # Check if at least 1 second has passed since the last spawn
    if current_time - last_spawn_time >= 0.2:
        # Update the last spawn time
        last_spawn_time = current_time

        # Generate random coordinates for the circle
        x = -50
        y = 200

        # Create the circle
        circle = canvas.create_oval(x, y, x + 50, y + 50, fill="red")

        # Move the circle from left to right
        def move_circle():
            nonlocal x
            canvas.move(circle, 5, 0)
            x += 5
            if x < 400:
                canvas.after(1, move_circle)
            else:
                canvas.delete(circle)

        # Start moving the circle
        move_circle()


# Bind the 'o' key to the spawn_circle function
window.bind("<Left>", spawn_circle)

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


def spawn_car(event):
    global last_spawn_time

    # Get the current time
    current_time = window.winfo_toplevel().time()

    # Check if at least 1 second has passed since the last spawn
    if current_time - last_spawn_time >= 1000:
        # Update the last spawn time
        last_spawn_time = current_time

        # Generate random coordinates for the circle
        x = 0
        y = 200

        # Create the circle
        circle = canvas.create_oval(x, y, x + 50, y + 50, fill="green")

        # Move the circle from left to right
        def move_circle():
            nonlocal x
            canvas.move(circle, 5, 0)
            x += 5
            if x < 400:
                canvas.after(5, move_circle)
            else:
                canvas.delete(circle)

        # Start moving the circle
        move_circle()


# Bind the 'o' key to the spawn_car function
window.bind("o", spawn_car)

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
