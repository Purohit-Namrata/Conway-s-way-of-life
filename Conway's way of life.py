import tkinter as tk
import random
import time

# Constants
CELL_SIZE = 10
WIDTH, HEIGHT = 600, 400
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
DELAY = 0.1

# Initialize the grid
grid = [[0] * COLS for _ in range(ROWS)]
next_grid = [[0] * COLS for _ in range(ROWS)]

# Initialize tkinter
root = tk.Tk()
root.title("Conway's Game of Life")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()

# Function to draw the grid
def draw_grid():
    canvas.delete("rect")
    for i in range(ROWS):
        for j in range(COLS):
            x0, y0 = j * CELL_SIZE, i * CELL_SIZE
            x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
            if grid[i][j] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="black", tags="rect")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white", tags="rect")

# Function to update the grid
def update_grid():
    global grid, next_grid
    for i in range(ROWS):
        for j in range(COLS):
            state = grid[i][j]
            neighbors = count_neighbors(i, j)
            if state == 0 and neighbors == 3:
                next_grid[i][j] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                next_grid[i][j] = 0
            else:
                next_grid[i][j] = state

    grid = [row[:] for row in next_grid]

# Function to count neighbors
def count_neighbors(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                nrow, ncol = (row + i) % ROWS, (col + j) % COLS
                count += grid[nrow][ncol]
    return count

# Function to initialize random cells
def randomize_grid():
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j] = random.choice([0, 1])

# Function to start the simulation
def start_simulation():
    global running
    running = True
    while running:
        update_grid()
        draw_grid()
        root.update()
        time.sleep(DELAY)

# Function to stop the simulation
def stop_simulation():
    global running
    running = False

# Function to handle mouse click events
def handle_click(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        grid[row][col] = 1 - grid[row][col]  # Toggle cell state
        draw_grid()

# Initialize random cells
randomize_grid()
draw_grid()

# Bind mouse click event to handle_click function
canvas.bind("<Button-1>", handle_click)

# Start/Stop button
start_button = tk.Button(root, text="Start", command=start_simulation)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(root, text="Stop", command=stop_simulation)
stop_button.pack(side=tk.LEFT, padx=10)

# Main loop
running = False
root.mainloop()
