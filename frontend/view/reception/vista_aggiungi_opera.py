#######################################################
# 
# VistaAggiungiOpera.py
# Python implementation of the Class VistaAggiungiOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaAggiungiOpera(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/RiceviDonazione.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getTitloloLineEdit(self) -> QLineEdit:
        return self.titoloLineEdit

    def getAutoreLineEdit(self) -> QLineEdit:
        return self.autoreLineEdit

    def getDimensioniLineEdit(self) -> QLineEdit:
        return self.dimensioniLineEdit

    def getTipoComboBox(self) -> QComboBox:
        return self.tipoComboBox

    def getPeriodoStoricoComboBox(self) -> QComboBox:
        return self.periodoStoricoComboBox

    def getUbicazioneButton(self) -> QPushButton:
        return self.ubicazioneButton

    def getFotoLabel(self) -> QLabel:
        return self.fotoLabel

    def getDropZoneLabel(self) -> QLabel:
        return self.dropZoneLabel

    def getConfermaButton(self) -> QPushButton:
        return self.confermaButton