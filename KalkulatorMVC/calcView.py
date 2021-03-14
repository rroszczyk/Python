from tkinter import *
from tkinter.font import *
from typing import Callable    # pozwala na zdefiniowane wejść i wyjść dla funkcji, które podowane są jako parametry
from calcOperation import CalculatorOperation


class CalculatorView:

    def __init__(self):
        self._root = Tk()
        self._root.title("Kalkulator")
        self._root.geometry("300x400")
        self.argumentTextLabel = StringVar()
        self.argumentTextLabel.set("")
        self.operationTextLabel = StringVar()
        self.operationTextLabel.set("")
        self._createGuiElements()
        self._placeGuiElements()

    def _createGuiElements(self):
        font_num = Font(family="consolas", size=14)

        # Tworzenie trzech głównych ramek interfejsu
        self._frame_Screen = Frame(self._root)         # ramka dla ekranów
        self._frame_NumPad = Frame(self._root)         # ramka dla przycisków numerycznych
        self._frame_OperationPad = Frame(self._root)   # ramka dla podstawowych operacji

        # Tworzenie obiektów ramki ekranów
        self._operationLabel = Label(self._frame_Screen, textvariable=self.operationTextLabel,
                                     bg="#282a36", fg="#f8f8f2", font=font_num)
        self._argumentLabel = Label(self._frame_Screen, textvariable=self.argumentTextLabel,
                                    bg="#282a36", fg="#f8f8f2", font=font_num)

        # Tworzenie obiektów ramki przycisków numerycznych
        self._button_0 = Button(self._frame_NumPad, text="0")
        self._button_1 = Button(self._frame_NumPad, text="1")
        self._button_2 = Button(self._frame_NumPad, text="2")
        self._button_3 = Button(self._frame_NumPad, text="3")
        self._button_4 = Button(self._frame_NumPad, text="4")
        self._button_5 = Button(self._frame_NumPad, text="5")
        self._button_6 = Button(self._frame_NumPad, text="6")
        self._button_7 = Button(self._frame_NumPad, text="7")
        self._button_8 = Button(self._frame_NumPad, text="8")
        self._button_9 = Button(self._frame_NumPad, text="9")

        # Lista wszystkich przycisków numerycznych (ułatwia wspólną konfigurację)
        self._list_button_numeric = [
            self._button_0,
            self._button_1,
            self._button_2,
            self._button_3,
            self._button_4,
            self._button_5,
            self._button_6,
            self._button_7,
            self._button_8,
            self._button_9]

        for bt in self._list_button_numeric:
            bt["bg"] = "#282a36"
            bt["fg"] = "#f8f8f2"
            bt["activebackground"] = "#282a36"
            bt["activeforeground"] = "#f8f8f2"
            bt["font"] = font_num
            bt["width"] = 1
            bt["height"] = 1

        self._button_p_m = Button(self._frame_NumPad, text=u"\u207A/\u208B ",
                                  bg="#44475a", fg="#f8f8f2",
                                  activebackground="#44475a",
                                  activeforeground="#f8f8f2",
                                  width=1,
                                  height=1,
                                  font=font_num)

        self._button_com = Button(self._frame_NumPad, text=",",
                                  bg="#44475a", fg="#f8f8f2",
                                  activebackground="#44475a",
                                  activeforeground="#f8f8f2",
                                  width=1,
                                  height=1,
                                  font=font_num)

        # Tworzenie obiektów ramki podstawowych operacji
        self._button_pls = Button(self._frame_OperationPad, text="+")
        self._button_min = Button(self._frame_OperationPad, text="-")
        self._button_mul = Button(self._frame_OperationPad, text=CalculatorOperation.MULTIPLICATION.getCharacter())
        self._button_div = Button(self._frame_OperationPad, text=CalculatorOperation.DIVISION.getCharacter())

        self._list_button_operation = [
            self._button_pls,
            self._button_min,
            self._button_mul,
            self._button_div]

        for bt in self._list_button_operation:
            bt["bg"] = "#44475a"
            bt["fg"] = "#f8f8f2"
            bt["activebackground"] = "#44475a"
            bt["activeforeground"] = "#f8f8f2"
            bt["font"] = font_num
            bt["width"] = 1
            bt["height"] = 1

        self._button_eql = Button(self._frame_OperationPad, text="=",
                                  bg="#009933", fg="#f8f8f2",
                                  activebackground="#009933",
                                  activeforeground="#f8f8f2",
                                  width=1, height=1,
                                  font=font_num)

        self._button_cls = Button(self._frame_OperationPad, text="CE",
                                  bg="#990000", fg="#f8f8f2",
                                  activebackground="#990000",
                                  activeforeground="#f8f8f2",
                                  width=1, height=1,
                                  font=font_num)

        # Tutaj należy dodać tworzenie przycisków dla nowych operacji np.:
        # self._button_sin = Button(self._frame_OperationPad, text="sin",
        #                           bg="#990000", fg="#f8f8f2",
        #                           activebackground="#990000",
        #                           activeforeground="#f8f8f2",
        #                           font=font_num)

    def _placeGuiElements(self):
        # Konfiguracja skalowania obiektów w głównym oknie root
        Grid.rowconfigure(self._root, 0, weight=2)
        Grid.rowconfigure(self._root, 1, weight=4)
        Grid.columnconfigure(self._root, 0, weight=3)
        Grid.columnconfigure(self._root, 1, weight=2)

        # Konfiguracja rozmieszczenia ramek w głównym oknie root
        self._frame_Screen.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)
        self._frame_NumPad.grid(row=1, column=0, sticky=N+S+E+W)
        self._frame_OperationPad.grid(row=1, column=1, sticky=N+S+E+W)

        # Konfiguracja skalowania obiektów znajdujących się w ramce dla ekranu
        Grid.rowconfigure(self._frame_Screen, 0, weight=2)
        Grid.rowconfigure(self._frame_Screen, 1, weight=4)
        Grid.columnconfigure(self._frame_Screen, 0, weight=1)

        # Konfiguracja skalowania obiektów znajdujących się w ramce dla przycisków numerycznych
        for k in range(4):
            Grid.rowconfigure(self._frame_NumPad, k, weight=1)
        for k in range(3):
            Grid.columnconfigure(self._frame_NumPad, k, weight=1)

        # Konfiguracja skalowania obiektów znajdujących się w ramce dla podstawowych operacji
        for k in range(4):
            Grid.rowconfigure(self._frame_OperationPad, k, weight=1)
        for k in range(2):
            Grid.columnconfigure(self._frame_OperationPad, k, weight=1)

        # Rozmieszczenie obiektów wewnątrz ramki dla ekranu
        self._operationLabel.grid(row=0, column=0, sticky=N+S+E+W)
        self._argumentLabel.grid(row=1, column=0, sticky=N+S+E+W)

        # Rozmieszczenie obiektów wewnątrz ramki numerycznej
        self._button_7.grid(row=0, column=0, sticky=N+S+E+W)
        self._button_8.grid(row=0, column=1, sticky=N+S+E+W)
        self._button_9.grid(row=0, column=2, sticky=N+S+E+W)
        self._button_4.grid(row=1, column=0, sticky=N+S+E+W)
        self._button_5.grid(row=1, column=1, sticky=N+S+E+W)
        self._button_6.grid(row=1, column=2, sticky=N+S+E+W)
        self._button_1.grid(row=2, column=0, sticky=N+S+E+W)
        self._button_2.grid(row=2, column=1, sticky=N+S+E+W)
        self._button_3.grid(row=2, column=2, sticky=N+S+E+W)
        self._button_0.grid(row=3, column=0, sticky=N+S+E+W)
        self._button_com.grid(row=3, column=1, sticky=N+S+E+W)
        self._button_p_m.grid(row=3, column=2, sticky=N+S+E+W)

        # Rozmieszczenie obiektów wewnątrz ramki dla operacji
        self._button_cls.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)   # przycisk CE ma długość 2 kolumn

        self._button_pls.grid(row=1, column=1, rowspan=2, sticky=N+S+E+W)  # przycisk + ma wysokość 2 rzędów (rowspan)
        self._button_eql.grid(row=3, column=1, sticky=N+S+E+W)

        self._button_mul.grid(row=1, column=0, sticky=N+S+E+W)
        self._button_div.grid(row=2, column=0, sticky=N+S+E+W)
        self._button_min.grid(row=3, column=0, sticky=N+S+E+W)

        # należało by zmodyfikować rozmieszczenie przycisków wewnątrz tej ramki przy wprowadzeniu nowych przycisków

    def setClearButtonCommand(self, command: Callable[[], None]):
        # command jest metodą, która nie przyjmuje żadnych argunetów [] i nie zwraca żadnych argumentów None
        self._button_cls['command'] = lambda: command()

    def setNumberButtonCommand(self, command: Callable[[str], None]):
        # command jest metodą, która nie przyjmuje żadnych jeden argument(sting) [str] i nie zwraca żadnych argumentów None
        for bt in self._list_button_numeric:
            bt["command"] = lambda x=bt["text"]: command(x)

    def setPlusButtonCommand(self, command: Callable[[CalculatorOperation], None]):
        self._button_pls["command"] = lambda: command(CalculatorOperation.ADDITION)

    def setMinusButtonCommand(self, command: Callable[[CalculatorOperation], None]):
        self._button_min["command"] = lambda: command(CalculatorOperation.SUBTRACTION)

    def setMultiplyButtonCommand(self, command: Callable[[CalculatorOperation], None]):
        self._button_mul["command"] = lambda: command(CalculatorOperation.MULTIPLICATION)

    def setDivideButtonCommand(self, command: Callable[[CalculatorOperation], None]):
        self._button_div["command"] = lambda: command(CalculatorOperation.DIVISION)

    def setEqualButtonCommand(self, command: Callable[[], None]):
        self._button_eql["command"] = lambda: command()

    def setCommaButtonCommand(self, command: Callable[[], None]):
        self._button_com["command"] = lambda: command()

    def setChangeSignButtonCommand(self, command: Callable[[], None]):
        self._button_p_m["command"] = lambda: command()

    # tutaj można dopisać metody przpisujące metody z kontrolera, które przycisk ma wykonywać, np.:
    # def setSinusButtonCommand(self, command: Callable[[CalculatorOperation], None]):
    #     self._button_sin["command"] = lambda: command(CalculatorOperation.SINUS)

    def appendInputNumber(self, digit: str):
        oldNumber = self.argumentTextLabel.get()
        if oldNumber == "0" and not digit == ".":
            self.argumentTextLabel.set(f"{digit}")
        else:
            self.argumentTextLabel.set(f"{oldNumber}{digit}")

    def getArgumentAsFloat(self) -> float:
        return float(self.argumentTextLabel.get())

    def resetView(self):
        self.operationTextLabel.set("")
        self.argumentTextLabel.set("")

    def startGui(self):
        self._root.mainloop()
