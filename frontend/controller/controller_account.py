#######################################################
# 
# ControllerAccount.py
# Python implementation of the Class ControllerAccount
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from types import NoneType

from backend.high_level.personale.dipendente import Dipendente
from frontend.controller.controller import Controller
from frontend.view.vista_account import VistaAccount


class ControllerAccount(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __gotoHome(self) -> None:
        self.closeView()
        self.previous.enableView()
        self.previous.closeView()
        self.home.enableView()
        self.home.showView()

    def __init__(self, view: VistaAccount, previous: Controller, home: Controller, model: Dipendente):
        super().__init__(view)
        self.view: VistaAccount = view
        self.previous = previous
        self.home = home
        self.model = model
        self.initializeUi()

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getLogoutButton().clicked.connect(self.__gotoHome)

    def initializeUi(self) -> None:
        self.view.getNomeLabel().setText('{} {}'.format(self.model.nome, self.model.cognome))
        self.view.getDataNascitaLabel().setText(self.model.data_nascita.strftime('%d/%m/%Y'))
        self.view.getSessoLabel().setText(self.model.sesso.name)
        self.view.getDataAssunzioneLabel().setText(self.model.data_registrazione.strftime('%d/%m/%Y'))
        self.view.getEmailLabel().setText(self.model.email)
        if type(self.model.lavoro) is NoneType:
            self.view.getDataAssegnazioneLavoroLabel().setText(self.model.lavoro.data_assunzione.strftime('%d/%m/%Y'))
            self.view.getOccupazioneLabel().setText(self.model.lavoro.__class__.__name__)
