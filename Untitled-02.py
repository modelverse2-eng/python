import tkinter as tk
import os
history_file = "bmi_history.txt"
bmi_history = []
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            for line in f:
                try:
                    bmi = float(line.strip())
                    bmi_history.append(bmi)
                except ValueError:
                    continue
def save_bmi_to_file(bmi):
    with open(history_file, "a") as f: f.write(f"{bmi}\n")
load_history()
root = tk.Tk()
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        if height > 3:        
         label_result.config(text="不是哥们你阿斯塔特啊") 
         return
        bmi = weight / (height ** 2)
        bmi_history.append(bmi)
        save_bmi_to_file(bmi)
        label_result.config(text=f"BMI是：{bmi:.2f}")
        avg_bmi = sum(bmi_history) / len(bmi_history)
        label_result.config(text=f"BMI是：{bmi:.2f}\n历史平均值：{avg_bmi:.2f}")
    except ValueError:
        label_result.config(text="请输入正确的数字！")
root.title("BMI 计算器")
root.geometry("300x200")
tk.Label(root, text="身高（米）:").pack()
entry_height = tk.Entry(root)
entry_height.pack()
tk.Label(root, text="体重（公斤）:").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()
tk.Button(root, text="计算 BMI", command=calculate_bmi).pack()
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()
