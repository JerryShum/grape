#!/usr/bin/env python3

from tkinter import Tk, BOTH, Canvas
from maze import Maze
from graphics import Window

def main():
    window = Window(1920, 1080)
    # Create cells
    maze = Maze(20, 20, 20,30, 50, 50, window)

    window.wait_for_close()

main()

