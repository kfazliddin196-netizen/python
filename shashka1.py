import tkinter as tk

# O'yin taxtasi uchun asosiy o'lchamlar
GRID_SIZE = 8
CELL_SIZE = 60
BOARD_COLOR_1 = "#DDB88C"
BOARD_COLOR_2 = "#A66D4F"
PIECE_COLOR_1 = "black"
PIECE_COLOR_2 = "white"

class CheckersGame:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()
        self.board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.turn = PIECE_COLOR_1  # Qora o'yinchi birinchi boshlaydi
        self.selected_piece = None
        self.selected_position = None
        self.draw_board()
        self.place_pieces()
        self.canvas.bind("<Button-1>", self.on_click)  # Klik harakati uchun bog'lash

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
                        self.board[row][col] = self.create_piece(row, col, PIECE_COLOR_1)
                    elif row > 4:  # So'nggi uchta qatorni to'ldirish
                        self.board[row][col] = self.create_piece(row, col, PIECE_COLOR_2)

    def create_piece(self, row, col, color):
        x1 = col * CELL_SIZE + 5
        y1 = row * CELL_SIZE + 5
        x2 = (col + 1) * CELL_SIZE - 5
        y2 = (row + 1) * CELL_SIZE - 5
        return self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        piece = self.board[row][col]

        if self.selected_piece:
            if (row + col) % 2 != 0 and not piece:  # Bo'sh joyga yurish
                self.move_piece(row, col)
        elif piece:  # Shashka tanlash
            self.select_piece(row, col)

    def select_piece(self, row, col):
        piece = self.board[row][col]
        piece_color = self.canvas.itemcget(piece, "fill")

        if piece_color == self.turn:  # O'yinchining navbati mos kelishi kerak
            self.selected_piece = piece
            self.selected_position = (row, col)
            self.canvas.itemconfig(piece, outline="yellow", width=3)  # Belgilash

    def move_piece(self, new_row, new_col):
        old_row, old_col = self.selected_position
        piece = self.selected_piece

        # Eski joyni bo'shatish
        self.board[old_row][old_col] = None
        self.canvas.coords(piece, new_col * CELL_SIZE + 5, new_row * CELL_SIZE + 5,
                           (new_col + 1) * CELL_SIZE - 5, (new_row + 1) * CELL_SIZE - 5)

        # Yangi joyni to'ldirish
        self.board[new_row][new_col] = piece

        # Turnni o'zgartirish
        self.turn = PIECE_COLOR_2 if self.turn == PIECE_COLOR_1 else PIECE_COLOR_1

        # Tanlangan shashkani bekor qilish
        self.canvas.itemconfig(piece, outline="", width=0)
        self.selected_piece = None
        self.selected_position = None

# Dastur oynasini yaratish
root = tk.Tk()
game = CheckersGame(root)
root.mainloop()
