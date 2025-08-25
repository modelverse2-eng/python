import tkinter as tk
import random
import time

# ---------------- 稀疏排序 ----------------
def sparse_index_mapping_sort(arr):#函数名是 sparse_index_mapping_sort，接受一个列表 arr
    """
    利用稀疏桶（字典）索引映射数字进行排序
    arr: 待排序数组
    """
    # 创建稀疏桶，只为出现过的数字创建桶
    buckets = {} #字典里的每个 key 会对应一个数字，每个 value 是一个列表，存放所有出现过这个数字的元素
    for num in arr:#遍历数组里的每个元素 num
        if num not in buckets:
            buckets[num] = 0
        buckets[num] += 1  # 重复数字直接追加
    
    # 按索引顺序展开，得到排序结果
    sorted_arr = [] #创建一个空列表 sorted_arr 用来存放最终结果
    for key in sorted(buckets.keys()): #buckets.keys() 是字典里所有的数字，然后 sorted(buckets.keys()) 会把这些数字从小到大排序
        for i in range(buckets[key]): 
            sorted_arr.append(key)  # 将每个桶里的元素添加到结果中，extend 会把列表里的每个元素拆开添加，而不是整个列表作为一个元素添加

    return sorted_arr

# ---------------- 归并排序 ----------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# ---------------- 内存预热函数 ----------------
def memory_warmup(size=500000):
    """
    简单内存预热：创建一个大数组并进行简单操作
    """
    temp = [0] * size  # 分配内存
    for i in range(size):
        temp[i] = i % 10  # 简单写入
    del temp  # 删除临时数组释放内存

# ---------------- 点击按钮时执行对比 ----------------
def update_data():
    # 内存预热
    memory_warmup()  # 可以在排序前调用

    size = 100000  # 数据量
    max_val = 100 # 最大随机数值
    data = [random.randint(1, max_val) for _ in range(size)]
    results = []

    # 稀疏索引映射排序
    arr = data[:]
    start = time.perf_counter()
    sorted_sparse = sparse_index_mapping_sort(arr)
    end = time.perf_counter()
    results.append(f"稀疏映射排序: {sorted_sparse[:10]}... 用时 {(end-start)*1000:.2f} ms")

    # 归并排序
    arr = data[:]
    start = time.perf_counter()
    sorted_ms = merge_sort(arr)
    end = time.perf_counter()
    results.append(f"归并排序: {sorted_ms[:10]}... 用时 {(end-start)*1000:.2f} ms")

    # Python 内置排序
    arr = data[:]
    start = time.perf_counter()
    sorted_py = sorted(arr)
    end = time.perf_counter()
    results.append(f"Python sorted(): {sorted_py[:10]}... 用时 {(end-start)*1000:.2f} ms")

    label.config(text="排序算法对比 (升序，显示前10个):\n" + "\n".join(results))

# ---------------- Tkinter 窗口 ----------------
root = tk.Tk()
root.title("排序算法对比 (稀疏映射 vs 归并排序 vs Python 内置)")

w, h = 900, 400
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
