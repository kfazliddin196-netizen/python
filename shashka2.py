from tkinter import *

GRID_SIZE = 8
CELL_SIZE = 60
BOARD_COLOR_1 = "#DDB88C"
BOARD_COLOR_2 = "#A66D4F"
PIECE_COLOR_1 = "black"
PIECE_COLOR_2 = "white"
class CheckersGame:
    def __init__(self, a):
        self.canvas = Canvas(a, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()
        self.draw_board()
    def draw_board(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
a=Tk()
game = CheckersGame(a)
a.mainloop()