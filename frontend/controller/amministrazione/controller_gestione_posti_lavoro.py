#######################################################
# 
# ControllerGestionePostiLavoro.py
# Python implementation of the Class ControllerGestionePostiLavoro
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
import Museo
from frontend.controller.controller import Controller
from frontend.view import VistaGestionePostiLavoro
from frontend.controller.controller import ControllerWidgetDipendente
from frontend.controller.controller import ControllerWidgetAggiungiAllaLista

class ControllerGestionePostiLavoro(Controller):
    m_ControllerWidgetDipendente= ControllerWidgetDipendente()

    m_ControllerWidgetAggiungiAllaLista= ControllerWidgetAggiungiAllaLista()

    m_VistaGestionePostiLavoro= VistaGestionePostiLavoro()

    def __gotoPrevious(self) -> None:
        pass

    def __init__(self,view : VistaGestionePostiLavoro, previous : Controller, model : Museo):
        pass

    def gotoVistaModificaPostoLavoro(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def __renderizzaPostiLavoro(self) -> ControllerWidgetPostoLavoro []:
        pass

    def initializeUi(self) -> None:
        pass