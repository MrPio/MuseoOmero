#######################################################
# 
# VistaInsericiUbicazione.py
# Python implementation of the Class VistaInsericiUbicazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QSpinBox

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaInsericiUbicazione(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/InserisciUbicazione.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getPianoSpinBox(self) -> QSpinBox:
        return self.pianoSpinBox

    def getNumeroMagazzinoSpinBox(self) -> QSpinBox:
        return self.numeroMagazzinoSpinBox

    def getScaffaleSpinBox(self) -> QSpinBox:
        return self.scaffaleSpinBox

    def getPosizioneSpinBox(self) -> QSpinBox:
        return self.posizioneSpinBox

    def getConfermaButton(self) -> QPushButton:
        return self.confermaButton
