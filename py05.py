import tkinter as tk
import random
from collections import deque
import tkinter.messagebox  # 用于胜利提示

CELL_SIZE = 50
ROWS, COLS = 10, 10
OBSTACLE_COUNT = 20 #用于记录障碍物位置

player_row, player_col = 0, 0
goal_row, goal_col = None, None # 终点的位置
obstacles = []
path = []  # 记录已走路径

def generate_goal():
    """生成终点位置（不与起点或障碍物重合）"""
    global goal_row, goal_col #选取合法位置（终点）
    available_cells = [(r, c) for r in range(ROWS) for c in range(COLS)
                       if (r, c) != (player_row, player_col) and (r, c) not in obstacles] #选取随机位置（终点）
    goal_row, goal_col = random.choice(available_cells)

def generate_obstacles():
    """生成障碍物"""
    all_cells = [(r, c) for r in range(ROWS) for c in range(COLS) # 可放障碍物的位置
                 if (r, c) != (player_row, player_col)]
    obstacles.clear()
    chosen = random.sample(all_cells, OBSTACLE_COUNT)
    obstacles.extend(chosen)

def is_path_exists():
    """检查是否存在从起点到终点的路径"""
    visited = set() #已记录的格子
    queue = deque([(player_row, player_col)]) #一个BFS队列首尾都可以修改数据
    visited.add((player_row, player_col))
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == (goal_row, goal_col): # 找到终点
            return True
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: #列出四个方向：上、下、左、右。dr是行变量dc是列变量减上减左
            nr, nc = r + dr, c + dc #n带表新的
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in obstacles and (nr, nc) not in visited:
                visited.add((nr, nc))# 判断是否在地图内、不是障碍物、没访问过
                queue.append((nr, nc))#append() 是把新的格子放到队列的末尾，等到前面所有格子都处理完才会轮到它。
    return False

def generate_map():
    """生成地图并保证有路径"""
    while True:
        generate_obstacles()
        generate_goal()
        if is_path_exists():
            break # 如果有可行路径，停止循环

def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c * CELL_SIZE, r * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="gray")
    
    # 已走路径（浅蓝色）
    for (r, c) in path:
        x1, y1 = c * CELL_SIZE, r * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
    
    # 障碍物
    for (r, c) in obstacles:
        x1, y1 = c * CELL_SIZE, r * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    
    # 终点（绿色方块 + “终”字）
    x1, y1 = goal_col * CELL_SIZE, goal_row * CELL_SIZE
    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill="green")
    canvas.create_text((x1+x2)/2, (y1+y2)/2, text="终点", fill="white", font=("Arial", 16, "bold"))

    # 玩家（红色圆点）
    px, py = player_col * CELL_SIZE + CELL_SIZE/2, player_row * CELL_SIZE + CELL_SIZE/2
    radius = CELL_SIZE / 2.5
    canvas.create_oval(px-radius, py-radius, px+radius, py+radius, fill="red")

def move_player(event):
    global player_row, player_col
    dr, dc = 0, 0
    if event.keysym == "Up":
        dr = -1
    elif event.keysym == "Down":
        dr = 1
    elif event.keysym == "Left":
        dc = -1
    elif event.keysym == "Right":
        dc = 1
    
    new_r = player_row + dr
    new_c = player_col + dc
    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in obstacles:
        player_row, player_col = new_r, new_c
        if (player_row, player_col) not in path:
            path.append((player_row, player_col))
        draw_board()
        # 到达终点
        if (player_row, player_col) == (goal_row, goal_col):
            tk.messagebox.showinfo("胜利", "你到达了终点！")

def restart_game():
    global player_row, player_col, path
    player_row, player_col = 0, 0
    path = [(player_row, player_col)]
    generate_map()
    draw_board()

root = tk.Tk()
root.title("走格子小游戏 - 升级版")

canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
canvas.pack()
restart_game()
root.bind("<Key>", move_player)

btn_restart = tk.Button(root, text="重新开始", command=restart_game)
btn_restart.pack(pady=10)

root.mainloop()
