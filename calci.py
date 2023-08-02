import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def scientific_calc():
    global entry 
    root = tk.Tk()
    root.title("Scientific Calculator")
    
    entry = tk.Entry(root, font=("Helvetica", 20), bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '+', '='),
        ('sin', 'cos', 'tan', 'C'),
        ('sqrt', 'log', 'exp', '^'),
        ('(', ')', 'pi', 'e')
    ]

    row_num = 1
    for row in buttons:
        col_num = 0
        for button_text in row:
            button = tk.Button(root, text=button_text, font=("Helvetica", 16), padx=20, pady=10)
            button.grid(row=row_num, column=col_num, padx=5, pady=5)
            button.bind("<Button-1>", on_click)
            col_num += 1
        row_num += 1

    root.mainloop()

if __name__ == "__main__":
    scientific_calc()
