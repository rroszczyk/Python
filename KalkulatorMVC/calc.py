from calcModel import CalculatorModel
from calcView import CalculatorView
from calcController import CalculatorController


class Calculator:

    def __init__(self,
                 model: CalculatorModel = CalculatorModel(),
                 view: CalculatorView = CalculatorView()):
        # zapis calculatorModel: model = CalculatorModel() oznacza,
        # że argument wejściowy model będzie typu CalculatorModel, jeżeli nie zostanie przekazany
        # przy wywołaniu konstruktora to zostanie stworzony nowy model ( wywołanie konstruktora CalculatorModel() )
        self._model = model
        self._view = view
        self._controller = CalculatorController(self._model, self._view)

    def StartCalculator(self):
        self._view.startGui()
