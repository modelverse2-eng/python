import tkinter as tk
import random
import time
import sys

# ---------------- 插入排序 ----------------我个人感觉和冒泡长得很像
def insertion_sort(arr):
    for i in range(1, len(arr)): #从第二个元素开始（索引 1），因为第一个元素默认“左边有序”，不需要动
        key = arr[i] #把当前要插入的值存到 key 里，这里key相当于一个临时变量
        j = i - 1 #j 指向左边有序部分的最后一个元素，用来找到 key 应该插入的位置
        while j >= 0 and arr[j] > key: #只要左边的元素比 key 大，就往右移动，让 key 有地方插入
            arr[j + 1] = arr[j] # 大的元素往右移一格
            j -= 1 # 往左继续比较
        arr[j + 1] = key #当 while 循环结束，key 找到合适位置，插入进去
    return arr

# ---------------- 归并排序 ----------------先把数组拆成小块再，从小块开始合并，每次合并都会挑出最小的元素放到新数组，通过不停的比对筛选来排序跑起来就像一个漏斗只不过是倒过来的（小的在上）
def merge_sort(arr):
    if len(arr) <= 1: #如果数组长度为 0 或 1，就已经有序，不需要排序防止卡死
        return arr #这是递归的终止条件
    mid = len(arr) // 2 #mid 就是 数组的中间索引，它告诉程序：数组从哪里切开成 左半部分 和 右半部分
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])#用：的左右来定义左右两部分
    
    merged = [] #merged → 用来存放最终合并后的有序数组
    i = j = 0 #i → 左边数组的索引，j → 右边数组的索引
    while i < len(left) and j < len(right): #比较左边 left[i] 和右边 right[j] 的大小
        if left[i] < right[j]:
            merged.append(left[i])#小的那个放入 merged
            i += 1
        else:
            merged.append(right[j])#小的那个放入 merged
            j += 1 #对应索引往右移动（i += 1 或 j += 1），这样保证 merged 里元素是升序的
    merged.extend(left[i:])
    merged.extend(right[j:])#处理剩余元素
    return merged

# ---------------- 点击按钮时执行对比 ----------------
def update_data():
    size = 100000  # 数据量
    data = [random.randint(1, 1000000) for _ in range(size)] # 生成一个长度为 size 的随机整数列表，范围 1 到 1000000
    results = []# 用来存放每种排序的结果和耗时信息

    # 插入排序
    arr = data[:]  # 拷贝一份，避免修改原数据
    start = time.perf_counter() # 记录开始时间
    sorted_is = insertion_sort(arr)# 调用插入排序
    end = time.perf_counter()# 记录结束时间
    results.append(f"插入排序: {sorted_is[:10]}... 用时 {(end-start)*1000:.2f} ms")# 保存排序结果前 10 个元素和耗时

    # 归并排序
    arr = data[:]
    start = time.perf_counter()
    sorted_ms = merge_sort(arr)# 调用归并排序
    end = time.perf_counter()
    results.append(f"归并排序: {sorted_ms[:10]}... 用时 {(end-start)*1000:.2f} ms")

    # Python 内置排序
    arr = data[:]
    start = time.perf_counter()
    sorted_py = sorted(arr)# 调用 Python 内置 sorted() 函数排序
    end = time.perf_counter()
    results.append(f"Python sorted(): {sorted_py[:10]}... 用时 {(end-start)*1000:.2f} ms")

    label.config(text="排序算法对比 (升序，显示前10个):\n" + "\n".join(results))

# ---------------- Tkinter 窗口 ----------------老生常谈
root = tk.Tk()
root.title("排序算法对比 (插入排序 vs 归并排序 vs Python 内置)")

w, h = 750, 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w - w) // 2
y = (screen_h - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")

label = tk.Label(root, text="点击按钮生成随机数据并排序", font=("Arial", 12), justify="left")
label.pack(pady=20)

button = tk.Button(root, text="运行排序对比", command=update_data)
button.pack(pady=10)

root.mainloop()
