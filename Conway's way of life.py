import tkinter as tk
import random
import math
from tkinter import Canvas

def generate_board():
        for x in range(0, resolution):
            for y in range(0, resolution):
                newx = x * cell
                newy = y * cell
                if grid1[x][y] == 1:
                    draw_cell(newx, newy, cell)

def draw_cell(x, y, size):
        c.create_rectangle(x, y, x+size, y+size, fill='black', outline='black')
        create_neighbours()

root=tk.Tk()
root.title("Conway's way of life ")
c=Canvas(root, bg="yellow", height=300, width=300)
c.grid(row=0,column=0)

width=500
height=500
resolution=100

cell= width/resolution

b=tk.Button(root, text="Game of life",command=generate_board)
b.grid(row=1,column=0)

grid1= [[0 for x in range(resolution)] for y in range(resolution)]

for x in range(0, resolution):
        for y in range(0, resolution):
              grid1[x][y] = random.randint(0, 1) 


def create_neighbours():
        new_grid = [[0 for x in range(resolution)] for y in range(resolution)]
        for x in range(0, resolution):
            for y in range(0, resolution):
                neighbours = count_neighbours(x, y)
                if grid1[x][y] == 1:            
                    if neighbours < 2:                        
                        new_grid[x][y] = 0
                    elif neighbours == 2 or neighbours == 3:
                        new_grid[x][y] = 1
                    elif neighbours > 3:
                       new_grid[x][y] = 0
                else:
                    if neighbours == 3:
                        new_grid[x][y] = 1
        return new_grid

def count_neighbours(x, y):
        count = 0
        xrange = [x-1, x, x+1]
        yrange = [y-1, y, y+1]
        for x1 in xrange:
            for y1 in yrange:
                if x1 == x and y1 == y:
                    continue
                try:
                     if grid1[x1][y1] == 1:
                          count += 1
                except IndexError:
                     continue
        return count

root.mainloop()