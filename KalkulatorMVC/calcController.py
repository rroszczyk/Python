from calcModel import CalculatorModel
from calcView import CalculatorView
from calcStateMachine import CalculatorStateMachine
from calcOperation import CalculatorOperation
from calcStates import CalculatorState


class CalculatorController:

    def __init__(self, model: CalculatorModel, view: CalculatorView):
        self._model = model
        self._view = view
        self._stateMachine = CalculatorStateMachine()

        self._stateMachine.bindToModel(model)
        self._stateMachine.bindToView(view)

        self._bindMethodsToView()

    def _bindMethodsToView(self):
        self._view.setClearButtonCommand(self.clearButtonPressed)
        self._view.setNumberButtonCommand(self.numButtonPressed)
        self._view.setPlusButtonCommand(self.twoArgumentOperationButtonPressed)
        self._view.setMinusButtonCommand(self.twoArgumentOperationButtonPressed)
        self._view.setMultiplyButtonCommand(self.twoArgumentOperationButtonPressed)
        self._view.setDivideButtonCommand(self.twoArgumentOperationButtonPressed)
        self._view.setEqualButtonCommand(self.equalButtonPressed)
        self._view.setCommaButtonCommand(self.commaButtonPressed)
        self._view.setChangeSignButtonCommand(self.plusMinusButtonPressed)
        # tutaj należy powiązać metodę kontrolera wykounjącą nową operację z przyciskiem dla tej operacji w widoku, np.:
        # self._view.setXSqueredButtonCommand(self.singleArgumentOperationButtonPressed)
        # self._view.setSinusButtonCommand(self.singleArgumentOperationButtonPress)

    def clearButtonPressed(self) -> None:
        current_state = self._stateMachine.current_state.name

        if current_state == CalculatorState.GETTING_NUM1:
            self._stateMachine.clearGettingNum1()

        elif current_state == CalculatorState.WAIT_FOR_NUM2:
            self._stateMachine.clearWaitForNum2()

        elif current_state == CalculatorState.GETTING_NUM2:
            self._stateMachine.clearGettingNum2()

        elif current_state == CalculatorState.SHOWING_RES:
            self._stateMachine.clearShowingRes()

        print(f"Zmiana stanu {current_state.name} -> {self._stateMachine.current_state.value}")

    def numButtonPressed(self, digit: str) -> None:
        print(f"Naciśnięto cyfrę {digit}")
        current_state = self._stateMachine.current_state.name

        if current_state == CalculatorState.WAIT_FOR_NUM1:
            self._stateMachine.startToReadFirstArgument(digit)

        elif current_state == CalculatorState.GETTING_NUM1:
            self._stateMachine.continueToReadFirstArgument(digit)

        elif current_state == CalculatorState.WAIT_FOR_NUM2:
            self._stateMachine.startToReadSecondArgument(digit)

        elif current_state == CalculatorState.GETTING_NUM2:
            self._stateMachine.continueToReadSecondArgument(digit)

        elif current_state == CalculatorState.SHOWING_RES:
            self._stateMachine.startToReadFirstArgumentForNewCalculation(digit)

        print(f"Zmiana stanu {current_state.name} -> {self._stateMachine.current_state.value}")

    def twoArgumentOperationButtonPressed(self, operation: CalculatorOperation) -> None:
        print(f"Naciśnięta operacja to: {operation.name}")
        current_state = self._stateMachine.current_state.name

        if current_state == CalculatorState.GETTING_NUM1:
            value = self._view.getArgumentAsFloat()
            self._stateMachine.setFirstArgumentForTwoArgumentOperation(value, operation)

        elif current_state == CalculatorState.WAIT_FOR_NUM2:
            self._stateMachine.changeTwoArgumentOperation(operation)

        elif current_state == CalculatorState.GETTING_NUM2:
            value = self._view.getArgumentAsFloat()
            self._stateMachine.continueCalculationWithoutResult(value, operation)

        elif current_state == CalculatorState.SHOWING_RES:
            value = self._view.getArgumentAsFloat()
            self._stateMachine.continueCalculationForCurrentResult(value, operation)

        print(f"Zmiana stanu {current_state.name} -> {self._stateMachine.current_state.value}")

    def equalButtonPressed(self) -> None:
        current_state = self._stateMachine.current_state.name
        if current_state == CalculatorState.GETTING_NUM2:
            value = self._view.getArgumentAsFloat()
            self._stateMachine.getResultOfTwoArgumentOperation(value)
        print(f"Zmiana stanu {current_state.name} -> {self._stateMachine.current_state.value}")

    def commaButtonPressed(self) -> None:
        print(f"Naciśnięto ,")
        current_state = self._stateMachine.current_state.name

        if current_state == CalculatorState.WAIT_FOR_NUM1:
            self._stateMachine.startToReadFirstArgument("0.")

        elif current_state == CalculatorState.GETTING_NUM1:
            if "." not in self._view.argumentTextLabel.get():
                self._stateMachine.continueToReadFirstArgument(".")

        elif current_state == CalculatorState.WAIT_FOR_NUM2:
            self._stateMachine.startToReadSecondArgument("0.")

        elif current_state == CalculatorState.GETTING_NUM2:
            if "." not in self._view.argumentTextLabel.get():
                self._stateMachine.continueToReadSecondArgument(".")

        elif current_state == CalculatorState.SHOWING_RES:
            self._stateMachine.startToReadFirstArgumentForNewCalculation("0.")

        print(f"Zmiana stanu {current_state.name} -> {self._stateMachine.current_state.value}")

    def plusMinusButtonPressed(self) -> None:
        print(f"Naciśnięto +/-")
        current_state = self._stateMachine.current_state.name

        if current_state == CalculatorState.GETTING_NUM1:
            self._stateMachine.changeArgument1Sign()

        elif current_state == CalculatorState.GETTING_NUM2:
            self._stateMachine.changeArgument2Sign()

        print(f"Zmiana stanu {current_state.name} -> {self._stateMachine.current_state.value}")

    def singleOperationButtonPressed(self, operation: CalculatorOperation) -> None:
        # TODO: Do samodzielnego dokończenia
        pass
