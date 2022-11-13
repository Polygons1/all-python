import tkinter
tk = tkinter.Tk()

tk.title("nicehash next paymant countdown")
text = tkinter.Text(tk, height=8)
text.pack()
tk.mainloop()
print(text.get("1.0", "end"))