from statemachine import StateMachine, State
from calcModel import CalculatorModel
from calcView import CalculatorView
from calcStates import CalculatorState
from calcOperation import CalculatorOperation


class CalculatorStateMachine(StateMachine):
    ### Definicja nazw stanów
    WAIT_FOR_NUM1 = State(CalculatorState.WAIT_FOR_NUM1, initial=True)
    WAIT_FOR_NUM2 = State(CalculatorState.WAIT_FOR_NUM2)
    GETTING_NUM1 = State(CalculatorState.GETTING_NUM1)
    GETTING_NUM2 = State(CalculatorState.GETTING_NUM2)
    SHOWING_RES = State(CalculatorState.SHOWING_RES)

    ### Definicja nazw przejść (patrz prezentacja)

    ## przejścia przy wciśnięciu CE (czerwone na prezentacji)
    # przejście WAIT_FOR_NUM1 -> WAIT_FOR_NUM1 przy CE nie jest definiowane, bo przy naciśnięcu CE dla tego stanu nic się nie dzieje (aplikacja jest już zresetowana)
    clearWaitForNum2 = WAIT_FOR_NUM2.to(WAIT_FOR_NUM1)
    clearGettingNum1 = GETTING_NUM1.to(WAIT_FOR_NUM1)
    clearGettingNum2 = GETTING_NUM2.to(WAIT_FOR_NUM1)
    clearShowingRes = SHOWING_RES.to(WAIT_FOR_NUM1)

    ## przejścia przy wprowadzaniu cyfr (niebieskie na prezentacji)
    startToReadFirstArgument = WAIT_FOR_NUM1.to(GETTING_NUM1)
    startToReadSecondArgument = WAIT_FOR_NUM2.to(GETTING_NUM2)
    continueToReadFirstArgument = GETTING_NUM1.to(GETTING_NUM1)
    continueToReadSecondArgument = GETTING_NUM2.to(GETTING_NUM2)
    startToReadFirstArgumentForNewCalculation = SHOWING_RES.to(GETTING_NUM1)

    ## przejścia przy operacjach dwuargumentowych (pomarańczowe na prezentacji)
    # przejście WAIT_FOR_NUM1 -> WAIT_FOR_NUM1 przy wciśnięcu operacji dwuargumentowej(+,-,*,/) nie jest definiowane, bo po resecie(CE) nie ma pierwszego argumentu, więc nie można zdefiniować operacji
    changeTwoArgumentOperation = WAIT_FOR_NUM2.to(WAIT_FOR_NUM2)
    setFirstArgumentForTwoArgumentOperation = GETTING_NUM1.to(WAIT_FOR_NUM2)
    continueCalculationWithoutResult = GETTING_NUM2.to(WAIT_FOR_NUM2)
    continueCalculationForCurrentResult = SHOWING_RES.to(WAIT_FOR_NUM2)

    ## przejścia przy operacjach jednoargumentowych (fioletowe na prezentacji)
    # przejście WAIT_FOR_NUM1 -> WAIT_FOR_NUM1 przy wciśnięcu operacji jednoargumentowej nie jest definiowane, bo po resecie(CE) nie ma pierwszego argumentu, więc nie można zdefiniować operacji
    changeToOneArgumentOperationAndGetResult = WAIT_FOR_NUM2.to(SHOWING_RES)
    getResultOfOneArgumentOperationFromFirstArgument = GETTING_NUM1.to(SHOWING_RES)
    getResultOfOneArgumentOperationFromCurrentCalculation = GETTING_NUM2.to(SHOWING_RES)
    getResultOfOneArgumentOperationFromPreviousResult = SHOWING_RES.to(SHOWING_RES)

    ## przejście przy wprowadzeniu znaku równości (zielone na prezentacji)
    # przejście WAIT_FOR_NUM1 -> WAIT_FOR_NUM1, nie jest definiowane, bo nic się nie dzieje
    # przejście WAIT_FOR_NUM2 -> WAIT_FOR_NUM2, nie jest definiowane, bo nic się nie dzieje
    # przejście GETTING_NUM1 -> GETTING_NUM1, nie jest definiowane, bo nic się nie dzieje
    getResultOfTwoArgumentOperation = GETTING_NUM2.to(SHOWING_RES)
    # przejście SHOWING_RES -> SHOWING_RES, nie jest definiowane, bo nic się nie dzieje


    ## przejścia przy zmianie znaku liczby (rożowe na prezentacji)
    # przejście WAIT_FOR_NUM1 -> WAIT_FOR_NUM1, nie jest definiowane, nie ma liczby, więc nie można zmienić znaku
    # przejście WAIT_FOR_NUM1 -> WAIT_FOR_NUM1, nie jest definiowane, nie ma liczby, więc nie można zmienić znaku
    changeArgument1Sign = GETTING_NUM1.to(GETTING_NUM1)
    changeArgument2Sign = GETTING_NUM2.to(GETTING_NUM2)
    # przejście SHOWING_RES -> SHOWING_RES, nie jest definiowane, bo zmiana znaku nie ma w tym miejscu zastosowania

    # dodaje model do obiektu maszyny stanów, co pozwala na wywoływanie publicznych metod modelu
    def bindToModel(self, model: CalculatorModel) -> None:
        self._model = model

    # dodaje vidok do obiektu maszyny stanów, co pozwala na wywołanie publicznych metod widoku
    def bindToView(self, view: CalculatorView) -> None:
        self._view = view

    ### Definicja metod, które będą wykonywane przy przejściach z poszczególnych stanów
    ### Wykorzystana paczka Pythona pozwala na definiowanie metod przy przejściu o następujących nazwach „on_{NazwaPrzejścia}”
    ## przejścia przy wciśnięciu CE
    def on_clearWaitForNum2(self) -> None:
        self._model.resetModel()
        self._view.resetView()

    def on_clearGettingNum1(self) -> None:
        self._model.resetModel()
        self._view.resetView()

    def on_clearGettingNum2(self) -> None:
        self._model.resetModel()
        self._view.resetView()

    def on_clearShowingRes(self) -> None:
        self._model.resetModel()
        self._view.resetView()

    ## przejścia przy wprowadzaniu cyfr
    def on_startToReadFirstArgument(self, digit: str) -> None:
        self._view.argumentTextLabel.set("")
        self._view.appendInputNumber(digit)

    def on_continueToReadFirstArgument(self, digit: str) -> None:
        self._view.appendInputNumber(digit)

    def on_startToReadSecondArgument(self, digit: str) -> None:
        self._view.argumentTextLabel.set("")
        self._view.appendInputNumber(digit)

    def on_continueToReadSecondArgument(self, digit: str) -> None:
        self._view.appendInputNumber(digit)

    def on_startToReadFirstArgumentForNewCalculation(self, digit: str) -> None:
        self._model.resetModel()
        self._view.resetView()
        self._view.appendInputNumber(digit)

    ## przejścia przy operacjach dwuargumentowych
    def on_setFirstArgumentForTwoArgumentOperation(self, value: float, operation: CalculatorOperation) -> None:
        self._model.setArg1(value)
        self._model.setOperation(operation)
        self._view.operationTextLabel.set(f"{value} {operation.getCharacter()}")

    def on_changeTwoArgumentOperation(self, operation: CalculatorOperation) -> None:
        self._model.setOperation(operation)
        operationTextLabel = self._view.operationTextLabel.get()
        operationTextLabel = operationTextLabel[:-1]     # usunięcie ostatniego znaku (znak operacji)
        self._view.operationTextLabel.set(f"{operationTextLabel}{operation.getCharacter()}")

    def on_continueCalculationWithoutResult(self, value: float, operation: CalculatorOperation) -> None:
        self._model.setArg2(value)
        result = self._model.getOperationResult()
        self._model.setArg1(result)
        self._model.setOperation(operation)
        self._view.operationTextLabel.set(f"{result} {operation.getCharacter()}")
        self._view.argumentTextLabel.set("")

    def on_continueCalculationForCurrentResult(self, value: float, operation: CalculatorOperation) -> None:
        self._model.setArg1(value)
        self._model.setOperation(operation)
        self._view.operationTextLabel.set(f"{value} {operation.getCharacter()}")
        self._view.argumentTextLabel.set("")

    ## przejścia przy operacjach jednoargumentowych
    def on_getResultOfOneArgumentOperationFromFirstArgument(self, value: float, operation: CalculatorOperation) -> None:
        # TODO: Do samodzielnego dokończenia
        pass

    def on_getResultOfOneArgumentOperationFromCurrentCalculation(self, value: float, operation: CalculatorOperation) -> None:
        # TODO: Do samodzielnego dokończenia
        pass

    def on_changeToOneArgumentOperationAndGetResult(self, operation: CalculatorOperation) -> None:
        # TODO: Do samodzielnego dokończenia
        pass

    def on_getResultOfOneArgumentOperationFromPreviousResult(self, value: float, operation: CalculatorOperation) -> None:
        # TODO: Do samodzielnego dokończenia
        pass

    ## przejście przy wprowadzeniu znaku równości
    def on_getResultOfTwoArgumentOperation(self, value: float) -> None:
        self._model.setArg2(value)
        result = self._model.getOperationResult()
        self._view.operationTextLabel.set(f"{self._model.getArg1()} {self._model.getOperation().getCharacter()} {self._model.getArg2()} =")
        self._view.argumentTextLabel.set(result)

    # przejścia przy zmianie znaku
    def on_changeArgument1Sign(self) -> None:
        arg = self._view.argumentTextLabel.get()
        if "-" in arg:
            self._view.argumentTextLabel.set(arg[1:])
        else:
            self._view.argumentTextLabel.set("-" + arg)

    def on_changeArgument2Sign(self) -> None:
        arg = self._view.argumentTextLabel.get()
        if "-" in arg:
            self._view.argumentTextLabel.set(arg[1:])
        else:
            self._view.argumentTextLabel.set("-" + arg)


