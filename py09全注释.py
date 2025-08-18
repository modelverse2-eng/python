import tkinter as tk
import tkinter.messagebox
from path_lib1 import player1_paths  # 玩家1的路径库（列表形式，每条路径是坐标元组列表）
from path_lib2 import player2_paths  # 玩家2的路径库

# ---------------- 常量 ----------------
CELL_SIZE = 50        # 每个格子的像素大小
ROWS, COLS = 9, 9     # 游戏地图的行数和列数
TIME_LIMIT = 15       # 游戏倒计时（秒）

# ---------------- 游戏状态变量 ----------------
player1_row, player1_col = 0, 0  # 玩家1当前行列坐标
player2_row, player2_col = ROWS-1, COLS-1  # 玩家2当前行列坐标
goal_row, goal_col = ROWS//2, COLS//2      # 终点坐标
game_over = False          # 游戏是否结束标志
moving = False             # 是否开始沿路径移动

# 路径索引变量
index1 = 0  # 玩家1当前路径索引
index2 = 0  # 玩家2当前路径索引

# 选择路径库里的第一条路径
path1 = player1_paths[0]  # 玩家1的预设路径（列表，每个元素是元组 (row, col)）
path2 = player2_paths[0]  # 玩家2的预设路径

# ---------------- Tkinter 初始化 ----------------
root = tk.Tk()
root.title("双人对战 - 路径库版")

# 画布：显示地图格子和玩家
canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
canvas.pack(padx=10, pady=10)

# 计时器标签
timer_label = tk.Label(root, text=f"剩余时间: {TIME_LIMIT} 秒", font=("Arial", 14))
timer_label.pack(pady=5)

# 启动按钮
start_button = tk.Button(root, text="启动预设路径移动")
start_button.pack(pady=5)

# ---------------- 绘制函数 ----------------
def draw_grid():
    """
    绘制整个游戏网格，包括背景格子、终点和玩家
    """
    canvas.delete("all")  # 清空画布
    # 绘制格子
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c*CELL_SIZE, r*CELL_SIZE
            x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="gray")
    draw_goal()     # 绘制终点
    draw_players()  # 绘制玩家

def draw_goal():
    """
    绘制终点格子（绿色）
    """
    gx1, gy1 = goal_col*CELL_SIZE, goal_row*CELL_SIZE
    gx2, gy2 = gx1+CELL_SIZE, gy1+CELL_SIZE
    canvas.create_rectangle(gx1, gy1, gx2, gy2, fill="green")

def draw_players():
    """
    绘制两个玩家的当前位置
    """
    canvas.create_oval(player1_col*CELL_SIZE, player1_row*CELL_SIZE,
                       player1_col*CELL_SIZE+CELL_SIZE, player1_row*CELL_SIZE+CELL_SIZE,
                       fill="red")  # 玩家1
    canvas.create_oval(player2_col*CELL_SIZE, player2_row*CELL_SIZE,
                       player2_col*CELL_SIZE+CELL_SIZE, player2_row*CELL_SIZE+CELL_SIZE,
                       fill="blue")  # 玩家2

# ---------------- 移动逻辑 ----------------
def auto_move():
    """
    按预设路径自动移动玩家，每0.5秒调用一次
    """
    global player1_row, player1_col, player2_row, player2_col
    global index1, index2, game_over, moving

    if game_over or not moving:
        return

    # 玩家1沿路径移动一步
    if index1 < len(path1):
        player1_row, player1_col = path1[index1]
        index1 += 1

    # 玩家2沿路径移动一步
    if index2 < len(path2):
        player2_row, player2_col = path2[index2]
        index2 += 1

    draw_grid()
    check_win()

    # 如果游戏未结束且移动中，0.5秒后继续调用 auto_move
    if not game_over and moving:
        root.after(500, auto_move)

# ---------------- 启动按钮 ----------------
def start_movement():
    """
    点击按钮启动路径移动和倒计时
    """
    global moving
    if not moving:
        moving = True
        auto_move()           # 开始移动
        update_timer(TIME_LIMIT)  # 启动倒计时

start_button.config(command=start_movement)

# ---------------- 胜利检测 ----------------
def check_win():
    """
    检查玩家是否到达终点
    """
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
    """
    每秒更新一次倒计时，时间为0则平局
    """
    global game_over
    if game_over or not moving:
        return
    if time_left <= 0:
        tk.messagebox.showinfo("游戏结束", "时间到！平局！")
        game_over = True
        return
    timer_label.config(text=f"剩余时间: {time_left} 秒")
    root.after(1000, update_timer, time_left-1)

# ---------------- 主体 ----------------
draw_grid()
root.mainloop()
