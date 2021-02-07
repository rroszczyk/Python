from tkinter import *
from tkinter.font import *

root = Tk()

tekst = StringVar()
tekst.set("etykieta_P1")

root.title("Moja aplikacja")
root.geometry("400x400")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

cz1 = Font(family="Segoe Print", size=28)

fr1 = Frame(root)
fr1.grid(row=0, column=0, sticky=N+S+E+W)
fr1.columnconfigure(0, weight=1)
fr1.columnconfigure(1, weight=2)
fr1.rowconfigure(0, weight=1)

fr2 = Frame(root)
fr2.grid(row=1, column=0, sticky=N+S+E+W)
# fr2.columnconfigure(0, weight=1)
# fr2.columnconfigure(1, weight=2)
# fr2.rowconfigure(0, weight=1)

fr3 = Frame(root)
fr3.grid(row=1, column=0, sticky=N+S+E+W)
name = StringVar()
name.set("__")
pole_tekstowe_wartosc = StringVar()
pole_tekstowe_wartosc.set("")
etykieta2 = Label(fr3, textvariable=name, font=cz1)
etykieta2.grid(row=0, column=0)
pole_tekstowe = Entry(fr3, textvariable=pole_tekstowe_wartosc)
pole_tekstowe.grid(row=1, column=0)

przycisk1 = Button(fr1, text="P1", font=cz1)
przycisk1.grid(row=0, column=0, sticky=N+S+E+W)

przycisk2 = Button(fr1, text="P2")
przycisk2["font"] = cz1
przycisk2.grid(row=0, column=1, sticky=N+S+E+W)

etykieta1 = Label(fr2, textvariable=tekst, font=cz1)
etykieta1.grid(row=0, column=0)

cb1 = Checkbutton(fr2, text="opcja1", font=cz1)
cb2 = Checkbutton(fr2, text="opcja2", font=cz1)
cb3 = Checkbutton(fr2, text="opcja3", font=cz1)
cb1.grid(row=1, column=0)
cb2.grid(row=2, column=0)
cb3.grid(row=3, column=0)


def akcja1():
    tekst.set("Etykieta p1")


def akcja2():
    tekst.set("Etykieta p2")


def akcja(t):
    tekst.set(f"Etykieta {t}")


def witam(ptw):
    name.set(f"Witam {ptw.get()}")


def p1():
    fr3.grid_remove()
    fr2.grid()


def p2():
    fr2.grid_remove()
    fr3.grid()


przycisk1["command"] = lambda: p1()
przycisk2["command"] = lambda: p2()

# przycisk1["command"] = lambda x=przycisk1: akcja(x["text"])
# przycisk2["command"] = lambda x=pole_tekstowe_wartosc: witam(x)


def e1_p1(event):
    print(event)
    w = event.widget
    w["font"] = Font(size=12)


def set_color_red(event):
    event.widget["fg"] = "#ff0000"


def set_color_black(event):
    event.widget["fg"] = "#000000"


# etykieta1.bind("<Button-1>", e1_p1)

etykieta1.bind("<Enter>", set_color_red)
etykieta1.bind("<Leave>", set_color_black)

przycisk1.bind("<Enter>", set_color_red)
przycisk1.bind("<Leave>", set_color_black)


root.mainloop()
