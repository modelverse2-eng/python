import tkinter as tk      # 导入 Tkinter 库，用来做图形界面
import random             # 导入 random 库，用来生成随机数
import time               # 导入 time 库，用来计时

# ---------------- 随机数据生成函数 ----------------
def generate_random_data(data_type="int", size=10, start=0, end=1000000):
    if data_type == "int":  # 如果指定类型是整数
        return [random.randint(start, end) for _ in range(size)]  # 返回一个随机整数列表
    elif data_type == "float":  # 如果指定类型是浮点数
        return [random.uniform(start, end) for _ in range(size)]  # 返回一个随机浮点数列表
    return None  # 其他情况返回 None

# ---------------- 手写冒泡排序函数 ----------------
def bubble_sort_desc(arr):
    """手写冒泡排序，降序"""
    n = len(arr)
    for i in range(n):  # 外层循环控制轮数
        for j in range(0, n-i-1):  # 内层循环控制每轮比较次数
            if arr[j] < arr[j+1]:  # 如果前面的元素小于后面的元素
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 交换位置，让大数“冒到前面”
    return arr

# ---------------- 点击按钮时更新显示的数据 ----------------
def update_data():
    groups = 5        # 要生成多少组随机数据，为了演示生成 5 组
    group_size = 1000 # 每组里有多少个数据
    results = []      # 用来存放最终显示结果的列表

    for i in range(groups):  # 循环生成每一组数据
        data = generate_random_data("int", size=group_size, start=1, end=1000000)  # 生成一组随机整数

        start_time = time.perf_counter()      # 记录排序前的时间（高精度计时）
        sorted_data = bubble_sort_desc(data)  # 使用手写冒泡排序，降序
        end_time = time.perf_counter()        # 记录排序后的时间

        duration = (end_time - start_time) * 1000  # 计算排序耗时，单位毫秒
        # 把每组的前10个数据和排序用时拼成字符串，放到 results 列表里
        results.append(f"第{i+1}组: {sorted_data[:10]}... 用时 {duration:.4f} ms")

    # 把 results 里的多行结果合并成字符串，更新到窗口的 label 上显示
    label.config(text="随机数据(降序, 显示前10个):\n" + "\n".join(results))

# --------------------- 创建窗口部分 ---------------------
root = tk.Tk()                            # 创建 Tkinter 根窗口
root.title("随机数据生成器（手写冒泡排序 + 计时）")  # 设置窗口标题

w, h = 710, 400                           # 窗口的宽度和高度
screen_w = root.winfo_screenwidth()       # 获取屏幕的宽度
screen_h = root.winfo_screenheight()      # 获取屏幕的高度
x = (screen_w - w) // 2                   # 计算窗口左上角 x 坐标（居中）
y = (screen_h - h) // 2                   # 计算窗口左上角 y 坐标（居中）
root.geometry(f"{w}x{h}+{x}+{y}")         # 设置窗口的大小和位置

# 标签：用来显示随机数据和排序用时
label = tk.Label(root, text="点击按钮生成随机数据", font=("Arial", 12), justify="left")
label.pack(pady=20)  # 把标签放到窗口上，并设置上下间距

# 按钮：点击后调用 update_data()，生成新的随机数据
button = tk.Button(root, text="生成随机数据", command=update_data)
button.pack(pady=10)  # 把按钮放到窗口上

root.mainloop()  # 运行 Tkinter 主循环
