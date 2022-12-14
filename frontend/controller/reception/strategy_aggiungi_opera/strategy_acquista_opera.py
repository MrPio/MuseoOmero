#######################################################
# 
# StrategyAcquistaOpera.py
# Python implementation of the Class StrategyAcquistaOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from frontend.controller.reception.strategy_aggiungi_opera.strategy_aggiungi_opera import StrategyAggiungiOpera


class StrategyAcquistaOpera(StrategyAggiungiOpera):
    def initializeUi(self, c: 'ControllerAggiungiOpera') -> None:
        c.view.getHeaderLabel().setText('HomeAmministrazione ➜ AcquistaOpera')

    def onConfermaClicked(self, c: 'ControllerAggiungiOpera') -> None:
        museo = Museo.getInstance()
        if c.model not in museo.opere:
            museo.opere.append(c.model)
