#######################################################
# 
# VistaTurniGuide.py
# Python implementation of the Class VistaTurniGuide
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QListView

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaTurniGuide(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaCercaGuida(2in1).ui')

    def getHeaderLabel(self) -> QLabel:
        return self.headerLabel

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getDataLineEdit(self) -> QLineEdit:
        return self.dataLineEdit

    def getRicercaButton(self) -> QPushButton:
        return self.ricercaButton

    def getFrecciaSinistra(self) -> QLabel:
        return self.frecciaSinistra

    def getFrecciaDestra(self) -> QLabel:
        return self.frecciaDestra

    def getTurniGuideListView(self) -> QListView:
        return self.turniGuideListView