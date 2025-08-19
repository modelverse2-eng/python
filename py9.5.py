import tkinter as tk
import tkinter.messagebox
import random
import time
import os
from collections import deque

# ---------------- 游戏参数 ----------------
CELL_SIZE = 50
ROWS, COLS = 10, 10
OBSTACLE_COUNT = 20
RECORDS_FILE = "records.txt"

# ---------------- 游戏状态 ----------------
player_row, player_col = 0, 0
goal_row, goal_col = None, None
obstacles = []
start_time = None
records = []

# ---------------- 排行榜功能 ----------------
def load_records():
    global records
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, "r") as f:
            records = [float(line.strip()) for line in f]
    else:
        records = []

def save_records():
    with open(RECORDS_FILE, "w") as f:
        for r in records:
            f.write(f"{r:.2f}\n")

def add_record(elapsed):
    global records
    records.append(elapsed)
    records.sort()
    records = records[:5]
    save_records()
    update_records_display()

def update_records_display():
    records_label.config(
        text="排行榜 (前5):\n" + "\n".join(f"{i+1}. {t:.2f} 秒" for i, t in enumerate(records))
        if records else "排行榜为空"
    )

# ---------------- 游戏逻辑 ----------------
def find_path(start, goal):
    """BFS 寻路（最短路径）"""
    q, visited, parent = deque([start]), {start}, {start: None}
    while q:
        r, c = q.popleft()
        if (r, c) == goal:
            path = []
            cur = (r, c)
            while cur:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in obstacles and (nr,nc) not in visited:
                visited.add((nr,nc))
                parent[(nr,nc)] = (r,c)
                q.append((nr,nc))
    return None

def generate_map():
    """生成障碍物和合法终点"""
    global obstacles, goal_row, goal_col
    obstacles = []
    while len(obstacles) < OBSTACLE_COUNT:
        r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if (r, c) != (player_row, player_col) and (r, c) not in obstacles:
            obstacles.append((r, c))
    # 生成可达终点
    for _ in range(100):
        r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if (r, c) != (player_row, player_col) and (r, c) not in obstacles:
            if find_path((player_row, player_col), (r, c)):
                goal_row, goal_col = r, c
                return
    goal_row, goal_col = ROWS-1, COLS-1  # 默认终点

def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c*CELL_SIZE, r*CELL_SIZE
            x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
            fill = "white"
            if (r,c) in obstacles: fill="black"
            elif (r,c)==(goal_row,goal_col): fill="green"
            elif (r,c)==(player_row,player_col): fill="red"
            canvas.create_rectangle(x1,y1,x2,y2,fill=fill,outline="gray")

def game_victory(msg):
    global start_time
    if start_time:
        elapsed = time.time()-start_time
        add_record(elapsed)
        tk.messagebox.showinfo("胜利", f"{msg}\n用时 {elapsed:.2f} 秒！")
    else:
        tk.messagebox.showinfo("胜利", msg)

def move_player(dr, dc):
    global player_row, player_col
    nr, nc = player_row+dr, player_col+dc
    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in obstacles:
        player_row, player_col = nr, nc
        draw_board()
        if (nr,nc)==(goal_row,goal_col):
            game_victory("手动到达终点！")

def auto_move():
    route = find_path((player_row, player_col), (goal_row, goal_col))
    if not route:
        tk.messagebox.showinfo("提示","没有路径可到终点！")
        return
    def step(i):
        global player_row, player_col
        if i < len(route):
            player_row, player_col = route[i]
            draw_board()
            if (player_row,player_col) == (goal_row,goal_col):
                game_victory("自动寻路完成！")
            else:
                root.after(300, step, i+1)
    step(0)

def restart_game():
    global player_row, player_col, start_time
    player_row, player_col = 0,0
    generate_map()
    draw_board()
    start_time = time.time()

# ---------------- UI ----------------
root = tk.Tk()
root.title("迷宫寻路游戏")

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame,width=COLS*CELL_SIZE,height=ROWS*CELL_SIZE)
canvas.grid(row=0,column=0)

records_label = tk.Label(frame,text="排行榜为空",justify="left",font=("Arial",12))
records_label.grid(row=0,column=1,padx=20,sticky="n")

tk.Button(root,text="自动寻路",command=auto_move).pack(fill="x")
tk.Button(root,text="重新开始",command=restart_game).pack(fill="x")

root.bind("<Up>",lambda e: move_player(-1,0))
root.bind("<Down>",lambda e: move_player(1,0))
root.bind("<Left>",lambda e: move_player(0,-1))
root.bind("<Right>",lambda e: move_player(0,1))

load_records()
update_records_display()
restart_game()
root.mainloop()
