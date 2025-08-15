import tkinter as tk
import random
from collections import deque
import tkinter.messagebox

# ---------------- 游戏参数 ----------------
CELL_SIZE = 50
ROWS, COLS = 10, 10
OBSTACLE_COUNT = 20
TIME_LIMIT = 15 * 1000  # 15秒，单位毫秒

# ---------------- 游戏状态 ----------------
player1_row, player1_col = 0, 0
player2_row, player2_col = ROWS - 1, COLS - 1

goal_row, goal_col = None, None
obstacles = []

path1 = []
path2 = []

# ---------------- 地图生成 ----------------
def generate_goal():
    global goal_row, goal_col
    available_cells = [
        (r, c) for r in range(ROWS) for c in range(COLS)
        if (r, c) not in [(player1_row, player1_col), (player2_row, player2_col)]
        and (r, c) not in obstacles
    ]
    goal_row, goal_col = random.choice(available_cells)

def generate_obstacles():
    global obstacles
    all_cells = [
        (r, c) for r in range(ROWS) for c in range(COLS)
        if (r, c) not in [(player1_row, player1_col), (player2_row, player2_col)]
    ]
    obstacles = random.sample(all_cells, OBSTACLE_COUNT)

def is_path_exists():
    visited = set()
    queue = deque([(player1_row, player1_col)])
    visited.add((player1_row, player1_col))
    while queue:
        r, c = queue.popleft()
        if (r, c) == (goal_row, goal_col):
            return True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in obstacles and (nr,nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc))
    return False

def generate_map():
    while True:
        generate_obstacles()
        generate_goal()
        if is_path_exists():
            break

# ---------------- 移动安全检测 ----------------
def can_move(player, new_r, new_c):
    if not (0 <= new_r < ROWS and 0 <= new_c < COLS):
        return False
    if (new_r, new_c) in obstacles:
        return False
    return True

# ---------------- 玩家手动移动 ----------------
def move_player(event):
    global player1_row, player1_col, player2_row, player2_col

    key = event.keysym #把按下的键的名字存到 key 变量里
    # 玩家1
    if key in ["Up","Down","Left","Right"]:
        dr, dc = 0,0
        if key=="Up": dr=-1
        elif key=="Down": dr=1
        elif key=="Left": dc=-1
        elif key=="Right": dc=1
        new_r, new_c = player1_row + dr, player1_col + dc
        if can_move(1,new_r,new_c):
            player1_row, player1_col = new_r, new_c
            if (new_r,new_c) not in path1:
                path1.append((new_r,new_c))
            check_win("玩家1")
        else:
            tk.messagebox.showwarning("警告", "玩家1不能移动到障碍或越界位置！")
    # 玩家2
    elif key.lower() in ["w","a","s","d"]:
        dr, dc = 0,0
        if key.lower()=="w": dr=-1
        elif key.lower()=="s": dr=1
        elif key.lower()=="a": dc=-1
        elif key.lower()=="d": dc=1
        new_r, new_c = player2_row + dr, player2_col + dc
        if can_move(2,new_r,new_c):
            player2_row, player2_col = new_r, new_c
            if (new_r,new_c) not in path2:
                path2.append((new_r,new_c))
            check_win("玩家2")
        else:
            tk.messagebox.showwarning("警告", "玩家2不能移动到障碍或越界位置！")
    draw_board()

# ---------------- 胜利检测 ----------------
def check_win(player):
    if (player1_row, player1_col) == (goal_row, goal_col):
        tk.messagebox.showinfo("胜利", "玩家1 到达终点！")
        restart_game()
    elif (player2_row, player2_col) == (goal_row, goal_col):
        tk.messagebox.showinfo("胜利", "玩家2 到达终点！")
        restart_game()

# ---------------- 绘制地图 ----------------
def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c*CELL_SIZE, r*CELL_SIZE
            x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
            canvas.create_rectangle(x1,y1,x2,y2, outline="red")
    for r, c in obstacles:
        x1, y1 = c*CELL_SIZE, r*CELL_SIZE
        x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
        canvas.create_rectangle(x1,y1,x2,y2, fill="black")
    for r, c in path1:
        canvas.create_rectangle(c*CELL_SIZE, r*CELL_SIZE,
                                c*CELL_SIZE+CELL_SIZE, r*CELL_SIZE+CELL_SIZE,
                                fill="lightblue")
    for r, c in path2:
        canvas.create_rectangle(c*CELL_SIZE, r*CELL_SIZE,
                                c*CELL_SIZE+CELL_SIZE, r*CELL_SIZE+CELL_SIZE,
                                fill="pink")
    canvas.create_rectangle(goal_col*CELL_SIZE, goal_row*CELL_SIZE,
                            goal_col*CELL_SIZE+CELL_SIZE, goal_row*CELL_SIZE+CELL_SIZE,
                            fill="green")
    canvas.create_text(goal_col*CELL_SIZE+CELL_SIZE/2,
                       goal_row*CELL_SIZE+CELL_SIZE/2,
                       text="终点", fill="white", font=("Arial",16,"bold"))
    radius = CELL_SIZE/2.5
    canvas.create_oval(player1_col*CELL_SIZE+CELL_SIZE/2-radius,#圆心的 X 坐标
                       player1_row*CELL_SIZE+CELL_SIZE/2-radius,
                       player1_col*CELL_SIZE+CELL_SIZE/2+radius,
                       player1_row*CELL_SIZE+CELL_SIZE/2+radius,
                       fill="red")
    canvas.create_oval(player2_col*CELL_SIZE+CELL_SIZE/2-radius,
                       player2_row*CELL_SIZE+CELL_SIZE/2-radius,
                       player2_col*CELL_SIZE+CELL_SIZE/2+radius,
                       player2_row*CELL_SIZE+CELL_SIZE/2+radius,
                       fill="blue")

# ---------------- 15秒强制结束 ----------------
def force_end_game():
    tk.messagebox.showinfo("时间到", "15秒到，游戏结束！")
    root.destroy()

# ---------------- 重置游戏 ----------------
def restart_game():
    global player1_row, player1_col, player2_row, player2_col, path1, path2
    player1_row, player1_col = 0, 0
    player2_row, player2_col = ROWS-1, COLS-1
    path1 = [(player1_row, player1_col)]
    path2 = [(player2_row, player2_col)]
    generate_map()
    draw_board()
    # 启动15秒倒计时
    if hasattr(root, 'timer_id') and root.timer_id is not None: #判断 root 对象是否存在属性 timer_id，确保 timer_id 已经有值，如果是 None 就不取消
        root.after_cancel(root.timer_id) #取消上一次的计时任务，防止多个计时叠加
    root.timer_id = root.after(TIME_LIMIT, force_end_game)#启动新的计时任务

# ---------------- 主窗口 ----------------
root = tk.Tk()
root.title("走格子小游戏 - 双人版（15秒限时）")

canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
canvas.pack()

root.bind("<Key>", move_player)
tk.Button(root, text="重新开始", command=restart_game).pack(pady=5)

restart_game()
root.mainloop()
