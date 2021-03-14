from enum import Enum


class CalculatorState(Enum):
    WAIT_FOR_NUM1 = 1   # oczekuje na rozpoczęcie wprowadzania pierwszej liczby
    WAIT_FOR_NUM2 = 2   # oczekuje na rozpoczęcie wprowadzania drugiej liczby
    GETTING_NUM1 = 3    # wprowadzanie pierwszej liczby
    GETTING_NUM2 = 4    # wprowadzanie drugirj liczby
    SHOWING_RES = 5     # prezentuje wynik
