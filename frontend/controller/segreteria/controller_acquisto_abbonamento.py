#######################################################
# 
# ControllerAcquistoAbbonamento.py
# Python implementation of the Class ControllerAcquistoAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.abbonamento import Abbonamento
from backend.high_level.clientela.cliente import Cliente
from backend.high_level.clientela.enum.sesso import Sesso
from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento
from backend.high_level.clientela.subscriber import Subscriber
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.view.segreteria.vista_acquisto_abbonamento import VistaAcquistoAbbonamento


class ControllerAcquistoAbbonamento(Controller, Subscriber):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaAcquistoAbbonamento, previous: Controller, model: Abbonamento):
        super().__init__(view)
        self.view: VistaAcquistoAbbonamento = view
        self.previous = previous
        self.model = model
        self.model.subscribe(self)
        self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()

    def __onConfermaClicked(self) -> None:
        data_nascita = None
        try:
            data_nascita = datetime.strptime(self.view.getDataNascitaLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return
        if len(self.view.getNomeLineEdit().text()) > 0 and len(self.view.getCognomeLineEdit().text()) > 0 \
                and len(self.view.getProvenienzaLineEdit().text()) > 0 and len(
            self.view.getCodiceFiscaleLineEdit().text()) > 0 and len(self.view.getCodiceFiscaleLineEdit().text()) == 16:

            if not self.model.acquista():
                self.notifica('Attenzione', 'Si è verificato un errore nel pagamento, si prega di riprovare...')
                return
            self.notifica('Abbonamento acquistato', f'Abbonamento acquistato con successo! \r\n ID --> {self.model.qr_code.id}')

            # Registro il nuovo cliente con tanto di abbonamento nel sistema.
            nuovo_cliente = Cliente(
                nome=self.view.getNomeLineEdit().text(),
                cognome=self.view.getCognomeLineEdit().text(),
                codFis=self.view.getCodiceFiscaleLineEdit().text(),
                sesso=Sesso[self.view.getSessoComboBox().currentText().upper().replace(' ', '_')],
                prov=self.view.getProvenienzaLineEdit().text(),
                nasc=data_nascita,
                abbonamenti=[self.model],
            )
            Museo.getInstance().visitatori.append(nuovo_cliente)

            self.closeView()
            self.previous.enableView()
        else:
            self.notifica('Attenzione', 'Per favore, compila correttamente tutti i campi!')

    def __onDurataChanged(self) -> None:
        self.model.tipo = TipoAbbonamento[self.view.getDurataComboBox().currentText().upper()]

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getConfermaButton().clicked.connect(self.__onConfermaClicked)
        self.view.getDurataComboBox().currentTextChanged.connect(self.__onDurataChanged)

    def __subscribeView(self) -> None:
        self.model.subscribe(self)

    def update(self) -> None:
        self.view.getCostoLabel().setText('€ {}'.format(self.model.calcolaCosto()))
