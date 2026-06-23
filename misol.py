import tkinter as tk
import math

class DrumSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Baraban Simulation")
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.angle = 0
        self.center_x = 200
        self.center_y = 200
        self.size = 100
        self.animate()
    def draw_star(self, angle):
        self.canvas.delete("all")
        points = []
        for i in range(5):
            outer_angle = math.radians(angle + i * 72)
            inner_angle = math.radians(angle + i * 72 + 36)

            outer_x = self.center_x + self.size * math.cos(outer_angle)
            outer_y = self.center_y + self.size * math.sin(outer_angle)
            inner_x = self.center_x + (self.size / 2.5) * math.cos(inner_angle)
            inner_y = self.center_y + (self.size / 2.5) * math.sin(inner_angle)

            points.append(outer_x)
            points.append(outer_y)
            points.append(inner_x)
            points.append(inner_y)

        self.canvas.create_polygon(points, fill='yellow', outline='black')

    def animate(self):
        self.draw_star(self.angle)
        self.angle += 5
        self.root.after(100, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrumSimulation(root)
    root.mainloop()
