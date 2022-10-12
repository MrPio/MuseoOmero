#######################################################
# 
# VistaReportIncassi.py
# Python implementation of the Class VistaReportIncassi
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QFrame

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaReportIncassi(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaReportIncassi.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getMeseLineEdit(self) -> QLineEdit:
        return self.meseLineEdit

    def getRightArrowIcon(self) -> QLabel:
        return self.rightArrowIcon

    def getLeftArrowIcon(self) -> QLabel:
        return self.leftArrowIcon

    def getVisualizzaButton(self) -> QPushButton:
        return self.visualizzaButton

    def getAcquistoOpereLabel(self) -> QLabel:
        return self.acquistoOpereLabel

    def getVenditaOpereLabel(self) -> QLabel:
        return self.venditaOpereLabel

    def getAbbonamentiLabel(self) -> QLabel:
        return self.abbonamentiLabel

    def getBigliettiLabel(self) -> QLabel:
        return self.bigliettiLabel

    def getRisultatoLabel(self) -> QLabel:
        return self.risultatoLabel

    def getGraficoFrame(self) -> QFrame:
        return self.graficoFrame