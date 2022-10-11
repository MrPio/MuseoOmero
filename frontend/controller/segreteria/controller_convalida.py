#######################################################
# 
# ControllerConvalida.py
# Python implementation of the Class ControllerConvalida
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from frontend.controller.controller import Controller
from frontend.controller.segreteria.strategy_convalida.strategy_convalida import StrategyConvalida
from frontend.view.segreteria.vista_convalida import VistaConvalida


class ControllerConvalida(Controller):

    def __gotoPrevious(self) -> None:
        pass

    def __init__(self, view: VistaConvalida, previous: Controller, strategy: StrategyConvalida):
        super().__init__(view)

    def __gotoVistaInserimentoManuale(self) -> None:
        pass

    def __onScannerizzaClicked(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def initializeUi(self) -> None:
        pass

    def finalizza(id : str) -> None:
        pass