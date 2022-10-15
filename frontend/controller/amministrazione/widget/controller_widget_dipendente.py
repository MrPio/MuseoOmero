#######################################################
# 
# ControllerWidgetDipendente.py
# Python implementation of the Class ControllerWidgetDipendente
# Generated by Enterprise Architect
# Created on:      12-ott-2022 19:37:25
# Original author: Valerio Morelli
#
#######################################################
from types import NoneType

from PyQt5.QtGui import QPixmap

from backend.high_level.museo import Museo
from backend.high_level.personale.amministratore import Amministratore
from backend.high_level.personale.dipendente import Dipendente
from backend.high_level.personale.operatore_al_pubblico import OperatoreAlPubblico
from backend.high_level.personale.reception import Reception
from backend.high_level.personale.segretario import Segretario
from frontend.controller.amministrazione.strategy_dipendenti.StrategyDipendenti import StrategyDipendenti
from frontend.controller.controller import Controller
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.widget.widget_dipendente import WidgetDipendente


class ControllerWidgetDipendente(Controller):

    def __init__(self, view: WidgetDipendente, parent: Controller, model: Dipendente,strategy:StrategyDipendenti):
        super().__init__(view)
        self.view: WidgetDipendente = view
        self.parent = parent
        self.model = model
        self.strategy=strategy
        self.connettiEventi()
        self.initializeUi()

    def __onLicenziaClicked(self) -> None:
        amministratori = list(filter(lambda dipendente: type(dipendente.lavoro) == Amministratore,
                                     Museo.getInstance().dipendenti))
        if type(self.model.lavoro) == Amministratore and len(amministratori) <= 1:
            return
        elif type(self.model.posto_lavoro)==NoneType:
            pass
            # TODO rimuovi il dipendete invece di licenziarlo, e assicurati che il pulsante cambi da 'licenzia' a 'rimuovi'
        self.model.posto_lavoro.licenzia(self.model, 'licenziamento per giusta causa')
        self.parent.initializeUi()

    def __onPromuoviClicked(self) -> None:
        if type(self.model.posto_lavoro) != NoneType:
            self.model.posto_lavoro.promuovi(self.model)
        else:
            for posto_lavoro in Museo.getInstance().posti_lavoro:
                if isinstance(posto_lavoro, Reception) and len(
                        posto_lavoro.lavori) < posto_lavoro.numero_postazioni_totali:
                    posto_lavoro.assumi(self.model)
        self.initializeUi()
        
    def __onSelezionaClicked(self) -> None:
        self.parent.previous.guida=self.model.lavoro
        self.parent.closeView()
        self.parent.previous.enableView()

    def connettiEventi(self) -> None:
        self.view.getLicenziaButton().clicked.connect(self.__onLicenziaClicked)
        self.view.getPromuoviButton().clicked.connect(self.__onPromuoviClicked)
        self.view.getSelezionaButton().clicked.connect(self.__onSelezionaClicked)

    def initializeUi(self):
        self.strategy.initializeWidgetUi(self)
        self.view.getNomeLabel().setText('{} {}'.format(self.model.nome, self.model.cognome))
        pixmaps = {
            OperatoreAlPubblico: QPixmap(":/icons/theater_comedy_FILL1_wght500_GRAD200_opsz48_risultato.png"),
            Segretario: QPixmap(":/icons/fax_FILL1_wght500_GRAD200_opsz48_risultato.png"),
            Amministratore: QPixmap(":/icons/shield_FILL1_wght500_GRAD200_opsz48_risultato"),
            NoneType: QPixmap(":/icons/person_FILL1_wght600_GRAD200_opsz48_risultato"),
        }
        self.view.getIcon().setPixmap(pixmaps[type(self.model.lavoro)])
        if type(self.model.lavoro) == Amministratore:
            self.view.getPromuoviButton().setStyleSheet(open(UI_DIR + '/css/grayButton.css', 'r').read())
            self.view.getPromuoviButton().setEnabled(False)
        if self.model.autogenerato:
            self.view.getLicenziaButton().setStyleSheet(open(UI_DIR + '/css/grayButton.css', 'r').read())
            self.view.getLicenziaButton().setEnabled(False)
        else:
            self.view.getLicenziaButton().setStyleSheet(open(UI_DIR + '/css/redButton.css', 'r').read())
