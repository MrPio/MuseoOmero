#######################################################
# 
# VistaInserimentoManuale.py
# Python implementation of the Class VistaInserimentoManuale
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLineEdit

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaInserimentoManuale(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/InserisciManualmente.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getIdLineEdit(self) -> QLineEdit:
        return self.idLineEdit

    def getConfermaButton(self) -> QPushButton:
        return self.confermaButton
