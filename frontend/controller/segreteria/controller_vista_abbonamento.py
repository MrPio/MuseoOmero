#######################################################
# 
# ControllerVistaAbbonamento.py
# Python implementation of the Class ControllerVistaAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
import datetime

from backend.high_level.clientela.abbonamento import Abbonamento
from backend.high_level.clientela.cliente import Cliente
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.view.segreteria.vista_abbonamento import VistaAbbonamento


class ControllerVistaAbbonamento(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __init__(self, view: VistaAbbonamento, previous: Controller, model: Abbonamento):
        super().__init__(view)
        self.view: VistaAbbonamento = view
        self.previous = previous
        self.model = model

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()

    def initializeUi(self) -> None:
        for cliente in filter(lambda visitatore: isinstance(visitatore, Cliente), Museo.getInstance().visitatori):
            if self.model in cliente.abbonamenti:
                self.view.getNomeLabel().setText(cliente.nome)
                self.view.getCognomeLabel().setText(cliente.cognome)
                self.view.getCodiceFiscaleLabel().setText(cliente.codiceFiscale)
                self.view.getScadenzaLabel() \
                    .setText('{} ({} giorni '.format(
                    (self.model.data_rilascio + datetime.timedelta(days=self.model.tipo.days)).strftime('%d/%m/%Y'),
                    abs(self.model.giorniAllaScadenza()))
                             + 'rimasti)' if self.model.giorniAllaScadenza() > 0 else 'fa)')

        # TODO inizializzare Qr-Code nella label
