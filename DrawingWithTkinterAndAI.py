# Project: Drawing with Tkinter and AI

"""Objective
Create a program that uses the Tkinter graphics library to draw shapes or patterns, enhanced with a simple AI algorithm for generating patterns."""

"""Tools and Libraries
- Python
- Tkinter graphics library
- Random library (for AI pattern generation)"""

"""Steps

Step 1: Set Up the Environment
1. Install Python: Make sure Python is installed on your computer. You can download it from [python.org](https://www.python.org/).

Step 2: Import Libraries and Set Up the Turtle
Create a new Python file (e.g., "turtle_ai.py") and start by importing the necessary libraries and setting up the Turtle."""

from tkinter import *
import random
import time

# Create a tkinter object
tk = Tk()
tk.title("Drawing with Tkinter and AI")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

# Create a canvas object
canvas = Canvas(tk, width = 800, height = 800, bd = 0, highlightthickness = 0)
canvas.pack()

"""Step 3: Create Basic Drawing Functions
Implement basic functions to draw shapes like squares, triangles, and circles."""

def draw_square(x1, y1, size):
    canvas.create_rectangle(x1, y1,  x1 + size, y1 + size)

def draw_triangle(x1, y1, x2, y2, x3, y3):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = "", outline = "black")

def draw_circle(x1, y1, size):
    canvas.create_oval(x1, y1, x1 + size, y1 + size)

"""Step 4: Implement AI Pattern Generation
Write a function that uses a simple AI algorithm to generate random patterns. This function can randomly choose shapes and their sizes to create unique patterns."""

def generate_pattern():
    while True:  # Draw shapes until the user presses the spacebar
        shape = random.choice(["square", "triangle", "circle"])
        
        if shape == "square":
            size = random.randint(1, 100)
            x1 = random.randint(0, 800 - size)
            y1 = random.randint(0, 800 - size)
            draw_square(x1, y1, size)
        elif shape == "triangle":
            x1 = random.randint(0, 800)
            y1 = random.randint(0, 800)
            x2 = random.randint(0, 800)
            y2 = random.randint(0, 800)
            x3 = random.randint(0, 800)
            y3 = random.randint(0, 800)
            draw_triangle(x1, y1, x2, y2, x3, y3)
        elif shape == "circle":
            size = random.randint(1, 100)
            x1 = random.randint(0, 800 - size)
            y1 = random.randint(0, 800 - size)
            draw_circle(x1, y1, size)

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

# Clear the screen before drawing a new pattern
def clear_screen():
    canvas.delete("all")
    tk.update_idletasks()
    tk.update()
    time.sleep(1)

"""Step 5: Add User Interaction
Allow users to generate new patterns by pressing a key. This will make the program more interactive and fun."""

def on_spacebar_press(event): # Listen for the spacebar press even
    clear_screen()

canvas.bind_all("<space>", on_spacebar_press) # Call the on_spacebar_press function when the user presses the spacebar
print("Press the spacebar to generate a new pattern.")
generate_pattern()
