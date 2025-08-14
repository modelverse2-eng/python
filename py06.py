import tkinter as tk
import random
from collections import deque
import tkinter.messagebox

# ---------------- 游戏参数 ----------------
CELL_SIZE = 50
ROWS, COLS = 10, 10
OBSTACLE_COUNT = 20

# ---------------- 游戏状态 ----------------
player_row, player_col = 0, 0
goal_row, goal_col = None, None
obstacles = []
path = []
planned_path = []

# ---------------- 地图生成 ----------------
def generate_goal():
    """生成终点位置，不与玩家起点或障碍物重合"""
    global goal_row, goal_col
    available_cells = [(r, c) for r in range(ROWS) for c in range(COLS)
                       if (r, c) != (player_row, player_col) and (r, c) not in obstacles]
    goal_row, goal_col = random.choice(available_cells)

def generate_obstacles():
    """生成障碍物，不与玩家起点重合"""
    global obstacles
    all_cells = [(r, c) for r in range(ROWS) for c in range(COLS)
                 if (r, c) != (player_row, player_col)]
    obstacles = random.sample(all_cells, OBSTACLE_COUNT)

def is_path_exists():
    """BFS 检查从起点到终点是否存在可行路径"""
    visited = set()
    queue = deque([(player_row, player_col)])
    visited.add((player_row, player_col))
    while queue:
        r, c = queue.popleft()
        if (r, c) == (goal_row, goal_col):
            return True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in obstacles and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    return False

def generate_map():
    """生成地图，保证存在可达路径"""
    while True:
        generate_obstacles()
        generate_goal()
        if is_path_exists():
            break

# ---------------- 绘制地图 ----------------
def draw_board():
    """绘制地图"""
    canvas.delete("all")

    # 网格
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c*CELL_SIZE, r*CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="red")

    # 障碍物
    for r, c in obstacles:
        x1, y1 = c*CELL_SIZE, r*CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    # 已走路径
    for r, c in path:
        x1, y1 = c*CELL_SIZE, r*CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")

    # 规划路径
    for r, c in planned_path:
        x1, y1 = c*CELL_SIZE, r*CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")

    # 终点
    x1, y1 = goal_col*CELL_SIZE, goal_row*CELL_SIZE
    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill="green")
    canvas.create_text((x1+x2)/2, (y1+y2)/2, text="终点", fill="white", font=("Arial",16,"bold"))

    # 玩家
    px, py = player_col*CELL_SIZE + CELL_SIZE/2, player_row*CELL_SIZE + CELL_SIZE/2
    radius = CELL_SIZE/2.5
    canvas.create_oval(px-radius, py-radius, px+radius, py+radius, fill="red")

# ---------------- 自动寻路 ----------------
def find_path(start, goal):
    """BFS 寻路"""
    queue = deque([start])
    visited = {start: None}
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            path_list = []
            cur = goal
            while cur is not None:
                path_list.append(cur)
                cur = visited[cur]
            return path_list[::-1]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in obstacles and (nr, nc) not in visited:
                visited[(nr, nc)] = (r, c)
                queue.append((nr, nc))
    return []

def auto_move():
    """自动移动到终点"""
    path_to_goal = find_path((player_row, player_col), (goal_row, goal_col))
    if not path_to_goal:
        tk.messagebox.showinfo("提示", "没有路径可以到达终点！")
        return
    def step(i):
        global player_row, player_col
        if i < len(path_to_goal):
            player_row, player_col = path_to_goal[i]
            if (player_row, player_col) not in path:
                path.append((player_row, player_col))
            draw_board()
            root.after(200, lambda: step(i+1))
        else:
            tk.messagebox.showinfo("胜利", "自动寻路到达终点！")
    step(0)

# ---------------- 手动移动 ----------------
def move_player(event):
    global player_row, player_col
    dr, dc = 0, 0
    if event.keysym == "Up": dr = -1
    elif event.keysym == "Down": dr = 1
    elif event.keysym == "Left": dc = -1
    elif event.keysym == "Right": dc = 1
    new_r, new_c = player_row + dr, player_col + dc
    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in obstacles:
        player_row, player_col = new_r, new_c
        if (player_row, player_col) not in path:
            path.append((player_row, player_col))
        draw_board()
        if (player_row, player_col) == (goal_row, goal_col):
            tk.messagebox.showinfo("胜利", "你到达了终点！")

# ---------------- 规划路径 ----------------
def plan_path(event):
    global planned_path
    c = event.x // CELL_SIZE
    r = event.y // CELL_SIZE
    if not planned_path:
        planned_path.append((player_row, player_col))
    if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in obstacles:
        last_r, last_c = planned_path[-1]
        if abs(r - last_r) + abs(c - last_c) == 1:
            planned_path.append((r, c))
    draw_board()

def follow_planned_path():
    global player_row, player_col
    if not planned_path:
        tk.messagebox.showinfo("提示", "请先规划路径！")
        return
    def step(i):
        global player_row, player_col
        if i < len(planned_path):
            r, c = planned_path[i]
            if (r, c) in obstacles or not (0 <= r < ROWS and 0 <= c < COLS):
                tk.messagebox.showinfo("提示", f"规划路径无效！第{i+1}步碰到障碍物或越界")
                return
            player_row, player_col = r, c
            if (player_row, player_col) not in path:
                path.append((player_row, player_col))
            draw_board()
            root.after(300, lambda: step(i+1))
        else:
            if (player_row, player_col) == (goal_row, goal_col):
                tk.messagebox.showinfo("胜利", "到达终点！")
            else:
                tk.messagebox.showinfo("提示", "规划路线没有到达终点！")
    step(0)

# ---------------- 重置 ----------------
def restart_game():
    global player_row, player_col, path, planned_path
    player_row, player_col = 0, 0
    path = [(player_row, player_col)]
    planned_path = []
    generate_map()
    draw_board()

# ---------------- 窗口 ----------------
root = tk.Tk()
root.title("走格子小游戏")

canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
canvas.pack()
canvas.bind("<Button-1>", plan_path)
canvas.bind("<B1-Motion>", plan_path)
root.bind("<Key>", move_player)

tk.Button(root, text="自动寻路", command=auto_move).pack(pady=5)
tk.Button(root, text="按规划路线走", command=follow_planned_path).pack(pady=5)
tk.Button(root, text="重新开始", command=restart_game).pack(pady=5)

restart_game()
root.mainloop()
