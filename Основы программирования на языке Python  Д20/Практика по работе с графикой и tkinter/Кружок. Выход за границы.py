import tkinter
import random


def prepare_and_start():
    global player, exit, fires
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]),
        (player_pos[0] + step, player_pos[1] + step),
        fill='green')
    exit = canvas.create_oval(
        (exit_pos[0], exit_pos[1]),
        (exit_pos[0] + step, exit_pos[1] + step),
        fill='yellow')
    N_FIRES = 20  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]),
            (fire_pos[0] + step, fire_pos[1] + step),
            fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])


def do_nothing(x):
    pass


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    if event.keysym == 'Down':
        move_wrap(player, (0, +step))
    if event.keysym == 'Right':
        move_wrap(player, (+step, 0))
    if event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    check_move()


step = 60  # Размер клетки
N_X = 14
N_Y = 26  # Размер сетки
master = tkinter.Tk()
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='blue',
                        height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()
# сделано неверно по мнению учителя
