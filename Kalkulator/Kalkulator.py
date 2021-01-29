from tkinter import *
from tkinter.font import *

root = Tk()   # Główny obiekt, w którym umieszczone są wszystkie pozostałe elementy interfejsu
root.title("Kalkulator")

if getattr(sys, 'frozen', False):   # w przypadku uruchamiania po kompilacji
    running_dir = sys._MEIPASS + "./"
else: 
    running_dir = "./"
icon_file_name = running_dir + "calc_icon.png"
if os.path.isfile(icon_file_name):
    root.iconphoto(True, PhotoImage(file=icon_file_name))   # Dodanie ikonki do aplikacji
    
root.geometry("300x400")   # rozmiar aplikacji 300px szerokości, 400px wysokości

Grid.rowconfigure(root, 0, weight=1)   # skalowanie wierszy z wagą 1
Grid.columnconfigure(root, 0, weight=1)   # skalowanie kolumn z wagą 1

# Dane aplikacji
hist_val = StringVar()   # zmienna odpowiadająca za zawartość ekranu z historią operacji
hist_val.set("")         # ustawienie wartości na pusty string
present_val = StringVar()   # zmienna odpowiadająca za zawartość ekranu akutalnie wprowadzanej wartości
present_val.set("")         # ustawienie wartości na pusty string
oper_var = StringVar()   # zmienna pamiętająca ostani naciśnięty przycisko z operacją
oper_var.set("")         # ustawienie wartości na pusty string
global num1
num1 = 0
global num2
num2 = 0

# główna ramka, która została podpięta pod obiekt root
frame = Frame(root)
# umieszczenie ramki w siatce(grid) o współrzędnych (0, 0)
# opcja sticky przykleja do wskazanych krawędzi okna (zapewnia skalowanie do rozmiaru okna)
frame.grid(row=0, column=0, sticky=N+S+W+E)

# ustawienie wag do skalowania wierszy i kolumn na 5 dla siatki wewnątrz głównej ramki(frame)
for k in range(6):
    Grid.rowconfigure(frame, k, weight=5)
for k in range(5):
    Grid.columnconfigure(frame, k, weight=5)
# zerowy rząd ma mniejszą wagę (z projektu graficznego wynika, że ma być niższy od pozostałych)
Grid.rowconfigure(frame, 0, weight=2)

# Czcionki
font_num = Font(family="consolas", size=14)

# Tworzenie elementów interfejsu. Wszystkie elementy interfejsu znajdują się wewnątrz głównej ramki (frame)
# Etykiety (nieedytowalny tekst). Pełnią role ekranów.
# Opcja textvariable pozwala na ustawianie tekstu zgodnie z wartością zmiennej
# Konfiguracja elementów może odbywać się przy ich tworzeniu. Po przecinku należy wpisać parametr=wartość
label_hist = Label(frame, textvariable=hist_val, bg="#282a36", fg="#f8f8f2", font=font_num)
label_present = Label(frame, textvariable=present_val, bg="#282a36", fg="#f8f8f2", font=font_num)

# Tworzenie obiektów odpowiedzialnych za przycyski numeryczne
button_0 = Button(frame, text="0")
button_1 = Button(frame, text="1")
button_2 = Button(frame, text="2")
button_3 = Button(frame, text="3")
button_4 = Button(frame, text="4")
button_5 = Button(frame, text="5")
button_6 = Button(frame, text="6")
button_7 = Button(frame, text="7")
button_8 = Button(frame, text="8")
button_9 = Button(frame, text="9")

# Lista wszystkich przycisków numerycznych (ułatwia wspólną konfigurację)
list_button_num = [
    button_0,
    button_1,
    button_2,
    button_3,
    button_4,
    button_5,
    button_6,
    button_7,
    button_8,
    button_9]

# Zmiana parametrów przycisków. Wszystkie przyciski mają tą taką samą konfigurację.
# Parametry można zmienić również tak samo jak wartość kluczy dla słównika
# ElementInterfejsu["nazwaParametru"] = wartość
for bt in list_button_num:
    bt["bg"] = "#282a36"
    bt["fg"] = "#f8f8f2"
    bt["activebackground"] = "#282a36"
    bt["activeforeground"] = "#f8f8f2"
    bt["font"] = font_num

# Tworzenie obiektów odpowiedzialnych za operacje matemtyczne
button_pls = Button(frame, text="+")
button_min = Button(frame, text="-")
button_mul = Button(frame, text="*")
button_div = Button(frame, text="/")
button_p_m = Button(frame, text=u"\u00B1")

# Lista wszystkich przycisków operacji matematycznych (ułatwia wspólną konfigurację)
list_button_oper = [
    button_pls,
    button_min,
    button_mul,
    button_div,
    button_p_m]

# Zmiana parametrów przycisków. Wszystkie przyciski mają tą taką samą konfigurację.
# Przyciski odpowiedzialne za operację mają inny kolor niż przyciski numeryczne
for bt in list_button_oper:
    bt["bg"] = "#44475a"
    bt["fg"] = "#f8f8f2"
    bt["activebackground"] = "#44475a"
    bt["activeforeground"] = "#f8f8f2"
    bt["font"] = font_num

# Pozostałe przyciski. Nie należą do żadnej kategorii, więc są konfigurowane indywidualnie przy tworzeniu.
button_com = Button(frame, text=",", bg="#44475a", fg="#f8f8f2", activebackground="#44475a", activeforeground="#f8f8f2", font=font_num)
button_eql = Button(frame, text="=", bg="#009933", fg="#f8f8f2", activebackground="#009933", activeforeground="#f8f8f2", font=font_num)
button_cls = Button(frame, text="CE", bg="#990000", fg="#f8f8f2", activebackground="#007722", activeforeground="#f8f8f2", font=font_num)


# Rozmieszczanie elementów na siadkce ramki głównej. Współrzędne(0,0) liczone są od lewego górnego rogu.
# Ekrany mają szerkość 5 kolumn (columnspan)
label_hist.grid(row=0, column=0, columnspan=5, sticky=N+S+W+E)
label_present.grid(row=1, column=0, columnspan=5, sticky=N+S+W+E)

button_7.grid(row=2, column=0, sticky=N+S+E+W)
button_8.grid(row=2, column=1, sticky=N+S+E+W)
button_9.grid(row=2, column=2, sticky=N+S+E+W)
button_cls.grid(row=2, column=3, columnspan=2, sticky=N+S+E+W)   # przycisk CE ma długość 2 kolumn

button_4.grid(row=3, column=0, sticky=N+S+E+W)
button_5.grid(row=3, column=1, sticky=N+S+E+W)
button_6.grid(row=3, column=2, sticky=N+S+E+W)
button_mul.grid(row=3, column=3, sticky=N+S+E+W)
button_div.grid(row=3, column=4, sticky=N+S+E+W)

button_1.grid(row=4, column=0, sticky=N+S+E+W)
button_2.grid(row=4, column=1, sticky=N+S+E+W)
button_3.grid(row=4, column=2, sticky=N+S+E+W)
button_pls.grid(row=4, column=3, rowspan=2, sticky=N+S+E+W)  # przycisk + ma wysokość 2 rzędów (rowspan)
button_min.grid(row=4, column=4, sticky=N+S+E+W)

button_0.grid(row=5, column=0, sticky=N+S+E+W)
button_com.grid(row=5, column=1, sticky=N+S+E+W)
button_p_m.grid(row=5, column=2, sticky=N+S+E+W)
button_eql.grid(row=5, column=4, sticky=N+S+E+W)


# Logika aplikacji
# Funkcja czyszcząca ekran
def clear_screen():
    hist_val.set("")
    present_val.set("")
    oper_var.set("")


# Funkcja dodająca znak do ekranu
def add_char(c):
    if oper_var.get() == "=":
        clear_screen()
    hist_val.set(hist_val.get()+c)
    present_val.set(present_val.get()+c)


# Funkcja dodająca przecinek do liczby.
# Uwaga 1: Dla języka polskiego separatorem dziesiętym jest ","
#          Natomiast dla Pythona jest to "."
# Uwaga 2: Przycisk ma zachowuje się inaczej w zależności czy zawartość ekranu jest pusta.
# Z powodu 1 i 2, można zastosować metody add_char w przypadku dodania przecinka
def add_coma():
    if present_val.get() == "":
        add_char("0.")
    else:
        add_char(".")


# Metoda wywołana po naciśnięciu przycisku z operacją matematyczną
def perform_oper(c):
    # Jeżeli ekran jest pusty to nic się nie dzieje (odpowiada naciśnięcu przycisku CE)
    if present_val.get() != "":
        # Jeżeli ostatnia wykonana operacja to pusty string to odczytaj liczbę z ekranu i zapamiętaj operację matematyczną
        if oper_var.get() == "":
            global num1
            num1 = float(present_val.get())
            hist_val.set(hist_val.get() + c)
            present_val.set("")
        # jeżęli ostatnia wykonana operacja to "=" ustaw wynik poprzedniej iteracji jako pierwszą liczbę
        elif oper_var.get() == "=":
            hist_val.set(f"{num1}{c}")
            present_val.set("")
        # W każdym innym wypadku (+, -, *, /). Odpowiada to wprowadzeniu kilku operatorów bez znaku "=" np. 1+2-3
        # Kalkulator nie rozpoznje kolejności wykonywania działań więc po wprowadzeniu drugiej operacji najpierw należy obliczyć wynik
        else:
            get_result()
            present_val.set("")
        oper_var.set(c)
    hist_val.set(f"{num1}{c}")
    oper_var.set(c)


# Metoda wyliczająca wynik
def cal_result():
    global num1
    global num2

    if oper_var.get() == "+":
        res = num1+num2
        present_val.set(res)
        num1 = res
    elif oper_var.get() == "-":
        res = num1-num2
        present_val.set(res)
        num1 = res
    elif oper_var.get() == "*":
        res = num1*num2
        present_val.set(res)
        num1 = res
    elif oper_var.get() == "/":
        res = num1/num2
        present_val.set(res)
        num1 = res


# Metoda odpowiedzialna za wyświetlenie wyniku (Odpowiada naciśnięcu "=")
def get_result():
    # Jeżeli ekran jest pusty lub już został naciśnięty przycisk "=" nic się nie dzieje
    if present_val.get() != "" and oper_var.get() != "=":
        global num2
        num2 = float(present_val.get())
        hist_val.set(hist_val.get() + "=")
        cal_result()
        oper_var.set("=")


# Metoda odpowiedzialna za wykonanie operacji +/- (zmiana znaku)
def change_sign():
    # Dla pustego ekranu nic się nie dzieje
    if present_val.get() != "":
        # Jeżeli ostatnia operacja to "=" lub pusty string to zmień znak pierwszej liczby
        # Odpwiada to sytuacji, w której kalkulator oczekuje na wprowadzenie piewrszej liczby
        if oper_var.get() == "" or oper_var.get() == "=":
            tmp_num = float(present_val.get())
            tmp_num = -tmp_num
            hist_val.set(f"{tmp_num}")
            present_val.set(tmp_num)
        # W pozostałym wypadku to ...
        # Odpwiada to sytuacji, w której kalkulator oczekuje na wprowadzenie drugiej liczby
        else:
            tmp_num = float(present_val.get())
            tmp_num = -tmp_num
            hist_val.set(f"{num1}{oper_var.get()}{tmp_num}")
            present_val.set(tmp_num)


# Przypisanie opracowanych metod do odpowiednich przycisków
# Metody przypisuje się przez parametr "command", którego wartością powinna być funkcja lambda
# Definicja funkcji lambfa wygląda następująco lambda wejsce: metoda(wejście)
# Zapis labnda wejscie=cos: metoda(wejscie) oznacza, że do wejście przypisana zostania wartość zmiennej cos

button_cls["command"] = lambda: clear_screen()

for bt in list_button_num:
    bt["command"] = lambda x=bt: add_char(x["text"])

for bt in list_button_oper:
    bt["command"] = lambda x=bt: perform_oper(x["text"])

button_eql["command"] = lambda: get_result()
button_com["command"] = lambda: add_coma()
button_p_m["command"] = lambda: change_sign()


# Bonus - Zmiana koloru po najechaniu myszką na przycisk
# Biblioteka tkinter udostępnia obługę zdarzeń(events). Przykładowe zdarzenia to
# naciśnięcie określonego przycisku myszki, klawiatury, najechanie na dany elemnt itp...
# Do zmiany koloru po najechaniu wykorzystane zostały dwa rodzaje zdarzeń:
# - <Enter> wejście kurosrem w powieszchnie danego elemntu
# - <Leave> wyjśćie kursora z powieszchni danego elemntu

# Metoda zmieniająca kolor przycisku.
# Biblioteka tkinter jako pierwszy parametr zawsze przekazuje informacje o zdarzeniu,
# pozostałe parametry mogą być zefiniowane dowolnie
def set_button_color(event, bg_hex_color):
    # bg_hex_color jest to kodowanie koloru przy pomocy kodu heksadecymalnego
    # kod ten określa nasycenie poszczególnych barw składowych czerwony, zielony, niebieski, z przedziału 0-255
    # np. #{wartość czerwonego}{wartość zielnego}{wartość niebieskiego}
    # wartość jest zapisywana w kodzie szestnastkowym czyli do zapisania 255 wartości wystarczyą tylko dwa znaki 255=ff
    # np. #000000 - czarny, #ffffff - biały, #ff0000 - czerwony, #00ffff - zielony+niebieski=zółty
    button = event.widget   # jedną z informacji o zdarzeniu jest element dla którego wystąpiło zdarzenie
    button["bg"] = bg_hex_color   # przycisk posiada parametr bg, któremu zmieniamy wartość


# Przypisanie zdarzeń do danego elementu odbywa się przy pomocy metody bind.
# Metoda ta posiada dwa parametry wejściowe:
# - 1 -> rodzaj zdarzenia
# - 2 -> metoda, która ma być wykonana kiedy dane zdarzenie wystąpi

# przypisanie metod do przycisków numerycznych
for bt in list_button_num:
    bt.bind("<Enter>", lambda x: set_button_color(x, "#6272a4"))
    bt.bind("<Leave>", lambda x: set_button_color(x, "#282a36"))

# przypisanie metod do przycisków operacyjnych
for bt in list_button_oper + [button_com]:
    bt.bind("<Enter>", lambda x: set_button_color(x, "#758fe0"))
    bt.bind("<Leave>", lambda x: set_button_color(x, "#44475a"))

# przypisanie metod do pozostałych przycisków
button_eql.bind("<Enter>", lambda x: set_button_color(x, "#39bf5b"))
button_eql.bind("<Leave>", lambda x: set_button_color(x, "#007722"))
button_cls.bind("<Enter>", lambda x: set_button_color(x, "#cc3939"))
button_cls.bind("<Leave>", lambda x: set_button_color(x, "#990000"))

root.mainloop()   # uruchamia główną pętle interfejsu.
