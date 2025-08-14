import tkinter as tk
from path_library import paths
root = tk.Tk()
root.title("固定路径行走")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()#把画布放进窗口
ROWS, COLS = 10, 10
CELL_SIZE = 40
for r in range(ROWS):
    for c in range(COLS):
        x1 = c * CELL_SIZE
        y1 = r * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, outline="black")
player = canvas.create_rectangle(0, 0, CELL_SIZE, CELL_SIZE, fill="red")
path = paths[1]
#接下来搞定位
def move_step(index):
    if index < len(path):
        r, c = path[index]
        x1 = c * CELL_SIZE
        y1 = r * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.coords(player, x1, y1, x2, y2)#方块移动就靠它
        root.after(1145, lambda: move_step(index+1))#格1145就动一次
move_step(0)#从第零步开始
root.mainloop()
