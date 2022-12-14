#######################################################
# 
# WidgetAggiungiAllaLista.py
# Python implementation of the Class WidgetAggiungiAllaLista
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QLabel

from frontend.ui.location import UI_DIR
from frontend.view.my_widget import MyWidget


class WidgetAggiungiAllaLista(MyWidget):

    def __init__(self, parent):
        super().__init__(UI_DIR + '/aggiungiAllaListaWidget.ui', parent)

    def getIcon(self) -> QLabel:
        return self.iconLabel
