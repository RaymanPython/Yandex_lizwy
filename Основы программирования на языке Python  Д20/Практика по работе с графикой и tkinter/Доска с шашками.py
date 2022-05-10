import tkinter

s = 600
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=s, width=s)
k = s / 8
for i in range(1, 8):
    x = i * k
    canvas.create_line((x, 0), (x, s), fill='red')
    canvas.create_line((0, x), (s, x), fill='red')
canvas.pack()
master.mainloop()
