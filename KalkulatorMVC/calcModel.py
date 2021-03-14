from calcOperation import CalculatorOperation
import math


class CalculatorModel:

    def __init__(self):
        self._arg1 = None
        self._arg2 = None
        self._operation = CalculatorOperation.NONE

    def getArg1(self) -> float:
        return self._arg1

    def setArg1(self, value: float) -> None:
        self._arg1 = value

    def getArg2(self) -> float:
        return self._arg2

    def setArg2(self, value: float) -> None:
        self._arg2 = value

    def getOperation(self) -> CalculatorOperation:
        return self._operation

    def setOperation(self, value: CalculatorOperation) -> None:
        self._operation = value

    def getOperationResult(self) -> float:
        if self._operation == CalculatorOperation.ADDITION:
            return self._arg1 + self._arg2
        elif self._operation == CalculatorOperation.SUBTRACTION:
            return self._arg1 - self._arg2
        elif self._operation == CalculatorOperation.MULTIPLICATION:
            return self._arg1 * self._arg2
        elif self._operation == CalculatorOperation.DIVISION:
            return self._arg1 / self._arg2
        elif self._operation == CalculatorOperation.X_SQUARED:
            return self._arg1 * self._arg1
        elif self._operation == CalculatorOperation.SQUARE_ROOT:
            return math.sqrt(self._arg1)
        # tutaj należy dodać obsługę dodatkowych operacji np.:
        # elif self._operation == CalculatorOperation.SINUS:
        #     return math.sin(self._arg1)
        
    def resetModel(self):
        self._arg1 = None
        self._arg2 = None
        self._operation = CalculatorOperation.NONE
