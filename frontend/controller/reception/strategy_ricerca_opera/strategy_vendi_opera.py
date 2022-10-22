#######################################################
# 
# StrategyVendiOpera.py
# Python implementation of the Class StrategyVendiOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from backend.low_level.pagamenti.nexi_api import NexiApi
from frontend.controller.reception.strategy_ricerca_opera.strategy_ricerca_opera import StrategyRicercaOpera
from frontend.ui.location import UI_DIR


class StrategyVendiOpera(StrategyRicercaOpera):
    def initializeUi(self, c: 'ControllerRicercaOpera') -> None:
        c.view.getHeaderLabel().setText('HomeReception ➜ VendiOpera')

    def onOperaClicked(self, c: 'ControllerWidgetOpera') -> None:
        # c.parent.previous --> ControllerAllestisciMostra
        if not c.model.isVendibile():
            c.notifica('Opera non vendibile', 'L\'opera non è vendibile in quanto non facente parte di alcuna mostra')
            return
        if c.model.vendi(NexiApi()):
            c.parent.previous.enableView()
            c.parent.closeView()
        else:
            c.notifica('Attenzione', 'Si è verificato un errore nel pagamento, si prega di riprovare...')

    def initializeWidgetUi(self, c: 'ControllerWidgetOpera'):
        if not c.model.isVendibile():
            # c.view.setEnabled(False)
            c.view.getOperaLabel().setStyleSheet(open(UI_DIR + '/css/widgetOperaOff.css', 'r').read())

