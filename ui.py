import tkinter as tk
import tkinter.font

def display_result():
    string = txt_display.get()
    try:
        result = eval(string)
    except:
        result = "ERROR"

    txt_display.delete(0, tk.END)
    txt_display.insert(0, str(result))

root = tk.Tk()
root.title("Basic Calculator")

font_buttons = tkinter.font.Font(root, family='Arial', size=20, weight='bold')

for i in range(5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

txt_display = tk.Entry(root, font="Courier 40 bold", justify='right')
txt_display.grid(row=0, column=0, columnspan=5, sticky='NESW')
for num in range(1,10):
    btn = tk.Button(
        root,

        text=str(num),
        font=font_buttons,
        command=lambda x=num: txt_display.insert(tk.END, str(x)))

    btn.grid(column=(num-1)%3, row=(num-1)//3+1, sticky = 'NESW')

btn_0 = tk.Button(root, text="0", font=font_buttons,
    command=lambda: txt_display.insert(tk.END, "0"))
btn_0.grid(row=4, column=0, columnspan=2, sticky='NESW')

btn_dot = tk.Button(root, text=".", font=font_buttons,
    command=lambda: txt_display.insert(tk.END, "."))
btn_dot.grid(row=4, column=2, sticky='NESW')

btn_plus = tk.Button(root, text="+", font=font_buttons,
    command=lambda: txt_display.insert(tk.END, "+"))
btn_plus.grid(row=1, column=3, sticky='NESW')

btn_minus = tk.Button(root, text="-", font=font_buttons,
    command=lambda: txt_display.insert(tk.END, "-"))
btn_minus.grid(row=2, column=3, sticky='NESW')

btn_mul = tk.Button(root, text="*", font=font_buttons,
    command=lambda: txt_display.insert(tk.END, "*"))
btn_mul.grid(row=3, column=3, sticky='NESW')

btn_div = tk.Button(root, text="/", font=font_buttons,
    command=lambda: txt_display.insert(tk.END, "/"))
btn_div.grid(row=4, column=3, sticky='NESW')

btn_back = tk.Button(root, text="C", font=font_buttons,
    command=lambda: txt_display.delete(0, tk.END))
btn_back.grid(row=1,column=4, sticky='NESW')

btn_equal = tk.Button(root, text="=", font=font_buttons,
    command=display_result)
btn_equal.grid(row=2,column=4, rowspan=3, sticky='NESW')


root.mainloop()
