#######################################################
# 
# VistaGestioneDipendenti.py
# Python implementation of the Class VistaGestioneDipendenti
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaGestioneDipendenti(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaGestisciDipendenti.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getTurniGuideListView(self) -> QWidget:
        return self.scrollAreaWidgetContents

    def getAssumiButton(self) -> QPushButton:
        return self.assumiButton

    def getHeaderLabel(self) -> QLabel:
        return self.titoloLabel
