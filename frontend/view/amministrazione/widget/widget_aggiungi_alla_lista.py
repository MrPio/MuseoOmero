#######################################################
# 
# WidgetAggiungiAllaLista.py
# Python implementation of the Class WidgetAggiungiAllaLista
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
import StrategyAggiungiAllaLista
import QWidget
import StrategyTurniGuide

class WidgetAggiungiAllaLista(QWidget):
    m_StrategyTurniGuide= StrategyTurniGuide()

    def __init__(self,action : StrategyAggiungiAllaLista):
        pass

    def __onClicked(self) -> None:
        pass

class WidgetAggiungiAllaLista(QWidget):
    def getIcon(self) -> QLabel:
        pass