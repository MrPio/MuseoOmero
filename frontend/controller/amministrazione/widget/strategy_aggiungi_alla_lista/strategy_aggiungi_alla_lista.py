#######################################################
# 
# StrategyAggiungiAllaLista.py
# Python implementation of the Interface StrategyAggiungiAllaLista
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtGui import QPixmap

import abc


class StrategyAggiungiAllaLista(abc.ABC):
    @abc.abstractmethod
    def onClicked(self) -> None:
        pass

    @abc.abstractmethod
    def getIcon(self) -> QPixmap:
        pass
