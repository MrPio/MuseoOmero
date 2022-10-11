#######################################################
# 
# ControllerWidgetTurnoGuida.py
# Python implementation of the Class ControllerWidgetTurnoGuida
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.clientela.biglietto import Biglietto
from backend.high_level.gestione_interna.turno_guida import TurnoGuida
from frontend.controller.controller import Controller
from frontend.controller.reception.strategy_turni_guide.strategy_turni_guide import StrategyTurniGuide
from frontend.view.reception.widget.widget_turno_guida import WidgetTurnoGuida


class ControllerWidgetTurnoGuida(Controller):

    def __init__(self, view: WidgetTurnoGuida, model: TurnoGuida, biglietto: Biglietto):
        super().__init__(view)

    def __onSelezionaClicked(self) -> None:
        pass

    def __onRimuoviButton(self) -> None:
        pass

    def __onModificaButton(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def initializeUi(strategy : StrategyTurniGuide) -> None:
        pass