#######################################################
# 
# VistaAcquistoBiglietto.py
# Python implementation of the Class VistaAcquistoBiglietto
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox
from frontend.view.my_main_window import MyMainWindow


class VistaAcquistoBiglietto(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaCompraBiglietto.ui')


    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getTipoBigliettoComboBox(self) -> QPushButton:
        return self.tipoBigliettoComboBox

    def getTariffaComboBox(self) -> QComboBox:
        return self.tariffaComboBox

    def getCercaGuidaButton(self) -> QPushButton:
        return self.cercaGuidaButton

    def getVerificaAbbonamentoButton(self) -> QPushButton:
        return self.verificaAbbonamentoButton

    def getCostoLabel(self) -> QLabel:
        return self.costoLabel

    def getConfermaButton(self) -> QPushButton:
        return self.confermaButton

