#######################################################
# 
# VistaOpera.py
# Python implementation of the Class VistaOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaOpera(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaOpera.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getImmagineLabel(self) -> QLabel:
        return self.immagineLabel

    def getTitoloLabel(self) -> QLabel:
        return self.titoloLabel_2

    def getAutoreLabel(self) -> QLabel:
        return self.autoreLabel

    def getDimensioniLabel(self) -> QLabel:
        return self.dimensioniLabel

    def getTipoLabel(self) -> QLabel:
        return self.tipoLabel

    def getPeriodoLabel(self) -> QLabel:
        return self.periodoLabel

    def getUbicazioneLabel(self) -> QLabel:
        return self.ubicazioneLabel

    def getCambiaUbicazioneButton(self) -> QPushButton:
        return self.cambiaUbicazioneButton

    def getCostoLabel(self) -> QLabel:
        return self.costoLabel

    def getEliminaButton(self) -> QPushButton:
        return self.eliminaButton
