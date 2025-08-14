import tkinter as tk
import random
from collections import deque
import tkinter.messagebox

CELL_SIZE = 50
ROWS, COLS = 10, 10
OBSTACLE_COUNT = 20  # 障碍物数量

# 玩家初始位置
player_row, player_col = 0, 0
# 终点位置
goal_row, goal_col = None, None
# 障碍物列表
obstacles = []
# 已走路径
path = []

def generate_goal():
    """生成终点位置（不与起点或障碍物重合）"""
    global goal_row, goal_col
    available_cells = [(r, c) for r in range(ROWS) for c in range(COLS)
                       if (r, c) != (player_row, player_col) and (r, c) not in obstacles]
    goal_row, goal_col = random.choice(available_cells)

def generate_obstacles():
    """生成障碍物"""
    all_cells = [(r, c) for r in range(ROWS) for c in range(COLS)
                 if (r, c) != (player_row, player_col)]
    obstacles.clear()
    obstacles.extend(random.sample(all_cells, OBSTACLE_COUNT))

def is_path_exists():
    """检查是否存在从起点到终点的路径"""
    visited = set()
    queue = deque([(player_row, player_col)])
    visited.add((player_row, player_col))
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == (goal_row, goal_col):
            return True
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in obstacles and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    return False

def generate_map():
    """生成地图并保证有可行路径"""
    while True:
        generate_obstacles()
        generate_goal()
        if is_path_exists():
            break

def draw_board():
    """绘制整个地图，包括网格、障碍物、路径、终点和玩家"""
    canvas.delete("all")
    # 绘制网格
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c * CELL_SIZE, r * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="red")
    # 绘制障碍物
    for r, c in obstacles:
        x1, y1 = c * CELL_SIZE, r * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    # 绘制已走路径（浅蓝色）
    for r, c in path:
        x1, y1 = c * CELL_SIZE, r * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
    # 绘制终点（绿色方块 + 文字）
    x1, y1 = goal_col * CELL_SIZE, goal_row * CELL_SIZE
    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill="green")
    canvas.create_text((x1+x2)/2, (y1+y2)/2, text="终点", fill="white", font=("Arial",16,"bold"))
    # 绘制玩家（红色圆点）
    px, py = player_col * CELL_SIZE + CELL_SIZE/2, player_row * CELL_SIZE + CELL_SIZE/2
    radius = CELL_SIZE / 2.5
    canvas.create_oval(px-radius, py-radius, px+radius, py+radius, fill="red")

def find_path(start, goal):
    """使用 BFS 寻找从 start 到 goal 的路径"""
    queue = deque([start])
    visited = {start: None}  # 记录前驱节点
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            # 回溯路径
            path_list = []
            cur = goal
            while cur is not None:
                path_list.append(cur)
                cur = visited[cur]
            return path_list[::-1]  # 反转路径
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in obstacles and (nr, nc) not in visited:
                visited[(nr, nc)] = (r, c)
                queue.append((nr, nc))
    return []

def auto_move():
    """自动寻路到终点，并显示动画"""
    path_to_goal = find_path((player_row, player_col), (goal_row, goal_col))
    if not path_to_goal:
        tk.messagebox.showinfo("提示", "没有路径可以到达终点！")
        return

    def step(i):
        global player_row, player_col
        if i < len(path_to_goal): #索引（Index）就是 列表或序列中每个元素的位置编号
            player_row, player_col = path_to_goal[i]
            if (player_row, player_col) not in path:
                path.append((player_row, player_col))
            draw_board()
            root.after(200, lambda: step(i+1))
        else:
            tk.messagebox.showinfo("胜利", "自动寻路到达终点！")
    
    step(0)

def move_player(event):
    """手动移动玩家"""
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

def restart_game():
    """重新开始游戏"""
    global player_row, player_col, path
    player_row, player_col = 0, 0
    path = [(player_row, player_col)]
    generate_map()
    draw_board()

# 创建主窗口
root = tk.Tk()
root.title("走格子小游戏 - 升级版")

# 创建画布
canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
canvas.pack()

# 初始化游戏
restart_game()

# 绑定按键事件
root.bind("<Key>", move_player)

# 创建按钮
btn_auto = tk.Button(root, text="自动寻路", command=auto_move)
btn_auto.pack(pady=10)
btn_restart = tk.Button(root, text="重新开始", command=restart_game)
btn_restart.pack(pady=10)

root.mainloop()
