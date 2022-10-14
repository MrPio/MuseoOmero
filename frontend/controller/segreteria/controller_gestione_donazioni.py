#######################################################
# 
# ControllerGestioneDonazioni.py
# Python implementation of the Class ControllerGestioneDonazioni
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.controller.segreteria.widget.controller_widget_richiesta_donazione import \
    ControllerWidgetRichiestaDonazione
from frontend.view.segreteria.vista_gestione_donazioni import VistaGestioneDonazioni


class ControllerGestioneDonazioni(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaGestioneDonazioni, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaGestioneDonazioni = view
        self.previous = previous
        self.model = model

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        #TODO listView

    def __renderizzaRichiestaDonazioni(self) -> list[ControllerWidgetRichiestaDonazione]:
        pass

    def initializeUi(self) -> None:
        #TODO
        pass