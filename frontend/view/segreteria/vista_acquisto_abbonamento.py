#######################################################
# 
# VistaAcquistoAbbonamento.py
# Python implementation of the Class VistaAcquistoAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaAcquistoAbbonamento(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/CompraAbbonamento.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getNomeLineEdit(self) -> QLineEdit:
        return self.nomeLineEdit

    def getCognomeLineEdit(self) -> QLineEdit:
        return self.cognomeLineEdit

    def getCodiceFiscaleLineEdit(self) -> QLineEdit:
        return self.codiceFiscaleLineEdit

    def getProvenienzaLineEdit(self) -> QLineEdit:
        return self.provenienzaLineEdit

    def getDataNascitaLineEdit(self) -> QLineEdit:
        return self.dataNascitaLineEdit

    def getSessoComboBox(self) -> QComboBox:
        return self.sessoComboBox

    def getDurataComboBox(self) -> QComboBox:
        return self.durataComboBox

    def getCostoLabel(self) -> QLabel:
        return self.costoLabel

    def getConfermaButton(self) -> QPushButton:
        return self.confermaButton