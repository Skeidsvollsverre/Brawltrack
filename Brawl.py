import tkinter as tk

root = tk.Tk()
root.title("BRAWLTRACKER")

def add_to_list():
    text=entry.get()
    if text:
        text_list.insert(tk.END,text)
        entry.delete(0,tk.END)
"""""
def on_click():
    lbl.config(text="Button clicked")

lbl = tk.Label(root, text="label 1")
lbl.grid(row=1, column=0)

print(lbl.config().keys())

btn=tk.Button (root, text="Matches", command=on_click)
btn.grid(row=0, column=2) 

btn=tk.Button (root, text="Stats")
btn.grid(row=0, column=1) 
"""

frame=tk.Frame(root)
frame.grid(row=0, column=0) 

entry =tk.Entry(frame)
entry.grid(row=0,column=0)

entry.bind()

entry_btn = tk.Button(frame, text="enter text here",  command=add_to_list)
entry_btn.grid(row=0,column=1)

text_list=tk.Listbox(frame)
text_list.grid(row=1, column=0)

root. mainloop()

