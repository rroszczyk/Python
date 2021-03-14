from enum import Enum


class CalculatorOperation(Enum):
    NONE = 0
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4
    X_SQUARED = 6
    SQUARE_ROOT = 7
    # tutaj należy dodać nazwy nowych operacji np.:
    # SINUS = 8

    def getCharacter(self):
        if self == CalculatorOperation.ADDITION:
            return "+"
        elif self == CalculatorOperation.SUBTRACTION:
            return "-"
        elif self == CalculatorOperation.MULTIPLICATION:
            return u"\u00D7"
        elif self == CalculatorOperation.DIVISION:
            return u"\u00F7"
        elif self == CalculatorOperation.X_SQUARED:
            return u"\u2082"
        elif self == CalculatorOperation.SQUARE_ROOT:
            return u"\u221A"
        # tutaj należy dodać znaki dla nowych operacji np.:
        # elif self == CalculatorOperation.SINUS:
        #     return "sin"

