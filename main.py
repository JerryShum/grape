#!/usr/bin/env python3

from tkinter import Tk, BOTH, Canvas
from maze import Maze
from graphics import Window

def main():
    window = Window(1900, 1000)
    # Create cells
    maze = Maze(20, 20, 20,30, 40, 40, window, 100)
    maze.solve()

    window.wait_for_close()

main()

