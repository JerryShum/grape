#!/usr/bin/env python3

from tkinter import Tk, BOTH, Canvas
from maze import Maze
from graphics import Window

def main():
    window = Window(800, 600)
    # Create cells
    maze = Maze(100, 100, 4,4, 100, 100, window)

    window.wait_for_close()

main()

