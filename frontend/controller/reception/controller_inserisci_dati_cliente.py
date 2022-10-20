#######################################################
# 
# ControllerInserisciDatiCliente.py
# Python implementation of the Class ControllerInserisciDatiCliente
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.enum.sesso import Sesso
from backend.high_level.clientela.visitatore import Visitatore
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.view.reception.vista_inserisci_dati_cliente import VistaInserisciDatiCliente


class ControllerInserisciDatiCliente(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __init__(self, view: VistaInserisciDatiCliente, previous: Controller, model: Visitatore):
        super().__init__(view)
        self.view: VistaInserisciDatiCliente = view
        self.previous = previous
        self.model = model

    def __onConfermaClicked(self) -> None:
        try:
            datetime.strptime(self.view.getDataNascitaLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return

        birth = datetime.strptime(self.view.getDataNascitaLineEdit().text(), '%d/%m/%Y')

        if len(self.view.getProvenienzaLineEdit().text()) > 0:
            nuovo_visitatore = Visitatore(
                dataNascita=birth,
                sesso=Sesso[self.view.getSessoComboBox().currentText().upper().replace(' ', '_')],
                provenienza=self.view.getProvenienzaLineEdit().text(),
            )
            nuovo_visitatore.biglietti.append(self.previous.model)
            Museo.getInstance().visitatori.append(nuovo_visitatore)
            Controller.notifica('Biglietto Creato', 'Biglietto creato con successo!')
            self.closeView()
            self.previous.previous.enableView()
            self.previous.previous.showView()

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getConfermaButton().clicked.connect(self.__onConfermaClicked)
