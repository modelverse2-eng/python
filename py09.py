import tkinter as tk
import tkinter.messagebox
from path_lib1 import player1_paths
from path_lib2 import player2_paths

CELL_SIZE = 50
ROWS, COLS = 9, 9
TIME_LIMIT = 15000

# ---------------- 游戏状态 ----------------
player1_row, player1_col = 0, 0
player2_row, player2_col = ROWS-1, COLS-1
goal_row, goal_col = ROWS//2, COLS//2
game_over = False

# 选择路径库里的第一条路径
path1 = player1_paths[0]
path2 = player2_paths[0]
index1 = 0
index2 = 0
moving = False

# ---------------- Tkinter ----------------
root = tk.Tk()
root.title("双人对战 - 路径库版")
canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
canvas.pack()
timer_label = tk.Label(root, text="剩余时间: 15 秒", font=("Arial",14))
timer_label.pack()

# ---------------- 绘制 ----------------
def draw_grid():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1,y1 = c*CELL_SIZE, r*CELL_SIZE
            x2,y2 = x1+CELL_SIZE, y1+CELL_SIZE
            canvas.create_rectangle(x1,y1,x2,y2, outline="gray")
    gx1,gy1 = goal_col*CELL_SIZE, goal_row*CELL_SIZE
    gx2,gy2 = gx1+CELL_SIZE, gy1+CELL_SIZE
    canvas.create_rectangle(gx1,gy1,gx2,gy2, fill="green")
    canvas.create_oval(player1_col*CELL_SIZE, player1_row*CELL_SIZE,
                       player1_col*CELL_SIZE+CELL_SIZE, player1_row*CELL_SIZE+CELL_SIZE,
                       fill="red")
    canvas.create_oval(player2_col*CELL_SIZE, player2_row*CELL_SIZE,
                       player2_col*CELL_SIZE+CELL_SIZE, player2_row*CELL_SIZE+CELL_SIZE,
                       fill="blue")

# ---------------- 自动移动 ----------------
def auto_move():
    global player1_row, player1_col, player2_row, player2_col
    global index1, index2, game_over, moving

    if game_over or not moving:
        return

    if index1 < len(path1):
        player1_row, player1_col = path1[index1]
        index1 += 1
    if index2 < len(path2):
        player2_row, player2_col = path2[index2]
        index2 += 1

    draw_grid()
    check_win()

    if not game_over and moving:
        root.after(500, auto_move)

# ---------------- 启动按钮 ----------------
def start_movement():
    global moving
    if not moving:
        moving = True
        auto_move()
        update_timer(15)

# ---------------- 胜利检测 ----------------
def check_win():
    global game_over, moving
    if (player1_row, player1_col) == (goal_row, goal_col):
        game_over = True
        moving = False
        tk.messagebox.showinfo("游戏结束", "玩家1胜利！")
    elif (player2_row, player2_col) == (goal_row, goal_col):
        game_over = True
        moving = False
        tk.messagebox.showinfo("游戏结束", "玩家2胜利！")

# ---------------- 倒计时 ----------------
def update_timer(time_left):
    global game_over
    if game_over or not moving:
        return
    if time_left <= 0:
        tk.messagebox.showinfo("游戏结束","时间到！平局！")
        game_over = True
        return
    timer_label.config(text=f"剩余时间: {time_left} 秒")
    root.after(1000, update_timer, time_left-1)

# ---------------- 按钮 ----------------
tk.Button(root, text="启动预设路径移动", command=start_movement).pack(pady=5)

# ---------------- 主体 ----------------
draw_grid()
root.mainloop()
