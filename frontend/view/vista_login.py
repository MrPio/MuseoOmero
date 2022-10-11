#######################################################
# 
# VistaLogin.py
# Python implementation of the Class VistaLogin
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaLogin(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/Login.ui')

    def getPreviousLabel(self) -> QLabel:
        return self.previousLabel

    def getErrorLabel(self)->QLabel:
        return self.errorLabel

    def getUsernameLineEdit(self) -> QLineEdit:
        return self.usernameLineEdit

    def getPasswordLineEdit(self) -> QLineEdit:
        return self.passwordLineEdit

    def getLoginButton(self) -> QPushButton:
        return self.ricercaButton
