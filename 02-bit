mport tkinter as tk
root = tk.Tk()
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        if height > 3:        label_result.config(text="不是哥们你阿斯塔特啊")
        return
        bmi = weight / (height ** 2)
        label_result.config(text=f"BMI是：{bmi:.2f}")
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
