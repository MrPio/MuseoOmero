#######################################################
# 
# ControllerWidgetRichiestaDonazione.py
# Python implementation of the Class ControllerWidgetRichiestaDonazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.personale.richiesta_donazione import RichiestaDonazione
from frontend.controller.controller import Controller
from frontend.view.segreteria.widget.widget_richiesta_donazione import WidgetRichiestaDonazione


class ControllerWidgetRichiestaDonazione(Controller):

    def __gotoVistaOpera(self) -> None:
        pass

    def __init__(self, view: WidgetRichiestaDonazione, model: RichiestaDonazione):
        super().__init__(view)

    def __onRifiutaClicked(self) -> None:
        pass

    def __onAccettaClicked(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass