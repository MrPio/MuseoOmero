#######################################################
# 
# VistaRicercaOpera.py
# Python implementation of the Class VistaRicercaOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QGridLayout

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaRicercaOpera(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VendiOpera.ui')

    def getHeaderLabel(self) -> QLabel:
        return self.titoloLabel

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getParametroRicercaLineEdit(self) -> QLineEdit:
        return self.parametroRicercaLineEdit

    def getTipoRicercaComboBox(self) -> QComboBox:
        return self.tipoRicercaComboBox

    def getRicercaButton(self) -> QPushButton:
        return self.ricercaButton

    def getRisultatiGridLayout(self) -> QGridLayout:
        return self.risultatiGridLayout
