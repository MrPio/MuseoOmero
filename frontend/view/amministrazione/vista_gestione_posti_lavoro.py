#######################################################
# 
# VistaGestionePostiLavoro.py
# Python implementation of the Class VistaGestionePostiLavoro
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QListView
from frontend.view.my_main_window import MyMainWindow


class VistaGestionePostiLavoro(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaGestisciPostiLavoro.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getReceptionsListView(self) -> QListView:
        return self.receptionsListView

    def getSegreterieListView(self) -> QListView:
        return self.segreterieListView

    def getAmministrazioniListView(self) -> QListView:
        return self.amministrazioniListView