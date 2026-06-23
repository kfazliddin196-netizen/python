from tkinter import *

# O'yin taxtasi uchun asosiy o'lchamlar
GRID_SIZE = 8
CELL_SIZE = 60
BOARD_COLOR_1 = "#DDB88C"
BOARD_COLOR_2 = "#A66D4F"
PIECE_COLOR_1 = "black"
PIECE_COLOR_2 = "white"

class CheckersGame:
    def __init__(self, root):
        self.canvas = Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()
        self.board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.draw_board()
        self.place_pieces()

    def draw_board(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def place_pieces(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if (row + col) % 2 != 0:  # Faqat qora kvadratlarga
                    if row < 3:  # Birinchi uchta qatorni to'ldirish
                        self.board[row][col] = self.canvas.create_oval(
                            col * CELL_SIZE + 5, row * CELL_SIZE + 5,
                            (col + 1) * CELL_SIZE - 5, (row + 1) * CELL_SIZE - 5,
                            fill=PIECE_COLOR_1)
                    elif row > 4:  # So'nggi uchta qatorni to'ldirish
                        self.board[row][col] = self.canvas.create_oval(
                            col * CELL_SIZE + 5, row * CELL_SIZE + 5,
                            (col + 1) * CELL_SIZE - 5, (row + 1) * CELL_SIZE - 5,
                            fill=PIECE_COLOR_2)

# Dastur oynasini yaratish
a=Tk()
game = CheckersGame(a)
a.mainloop()
