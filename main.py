from tkinter import *
w = Tk()
w.geometry('300x500')
w.configure(bg="#141414")


def bttn(x, y, text, bcolor, fcolor, cmd):

    def on_enter(e):
        monBouton['background'] = bcolor
        monBouton['foreground'] = fcolor

    def on_leave(e):
        monBouton['background'] = fcolor
        monBouton['foreground'] = bcolor

    monBouton = Button(w, width=42, height=2, text=text,
                       fg=fcolor,
                       bg=bcolor,
                       border=0,
                       activeforeground=fcolor,
                       activebackground=bcolor,
                       command=cmd,)

    monBouton.bind("<Enter>", on_enter)
    monBouton.bind("<Leave>", on_leave)

    monBouton.place(x=x, y=y)


def cmd():
    print('Your clicked A C E R')


def cmd1():
    print('Your clicked A P P E L')
    # monBouton.place(x=0,y=0)


bttn(0, 0, "A C E R", '#ffcc66', "#141414", cmd)
bttn(0, 37, "A P P E L", '#25dae9', "#141414", cmd1)
w.mainloop()
