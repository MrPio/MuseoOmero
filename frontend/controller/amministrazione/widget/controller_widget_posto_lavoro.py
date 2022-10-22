#######################################################
# 
# ControllerWidgetDipendente.py
# Python implementation of the Class ControllerWidgetPostoLavoro
# Generated by Enterprise Architect
# Created on:      07-ott-2022 20:29:22
# Original author: Valerio Morelli
# 
#######################################################
from PyQt5.QtGui import QPixmap

from backend.high_level.personale.amministrazione import Amministrazione
from backend.high_level.personale.posto_lavoro import PostoLavoro
from backend.high_level.personale.reception import Reception
from backend.high_level.personale.segreteria import Segreteria
from frontend.controller.amministrazione.controller_modifica_posto_lavoro import ControllerModificaPostoLavoro
from frontend.controller.amministrazione.widget.strategy_widget_posto_lavoro.strategy_widget_posto_lavoro import \
    StrategyWidgetPostoLavoro
from frontend.controller.controller import Controller
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_modifica_posto_lavoro import VistaModificaPostoLavoro
from frontend.view.amministrazione.widget.widget_posto_lavoro import WidgetPostoLavoro


class ControllerWidgetPostoLavoro(Controller):

    def __init__(self, view: WidgetPostoLavoro, model: PostoLavoro, parent: Controller,
                 strategy: StrategyWidgetPostoLavoro):
        super().__init__(view)
        self.view: WidgetPostoLavoro = view
        self.model = model
        self.parent = parent
        self.strategy = strategy
        self.selected=False
        self.showView()
        self.connettiEventi()
        self.initializeUi()

    def __onAssegnaPostoClicked(self) -> None:
        self.parent.lavoro_scelto = self.model
        # self.notifica('Posto Selezionato', f'Hai selezionato --> {self.model.nome}')
        for controller in self.parent.posti_lavoro:
            controller.view.setEnabled(True)
            controller.selected=False
        self.selected=True
        self.initializeUi()
        self.view.setEnabled(False)

    def __onRimuoviClicked(self) -> None:
        self.model.rimuovi(self.parent.model)
        self.parent.initializeUi()

    def __gotoVistaModificaPostoLavoro(self) -> None:
        self.next = ControllerModificaPostoLavoro(
            view=VistaModificaPostoLavoro(),
            previous=self.parent,
            model=self.model
        )
        self.parent.disableView()

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getAssegnaPostoButton().clicked.connect(self.__onAssegnaPostoClicked)
        self.view.getRimuoviButton().clicked.connect(self.__onRimuoviClicked)
        self.view.getModificaButton().clicked.connect(self.__gotoVistaModificaPostoLavoro)

    def initializeUi(self):
        self.strategy.initializeUi(self)
        self.view.getNomeLabel().setText('{} (piano {})'.format(self.model.nome, self.model.piano))
        self.view.getPostiLiberiLabel().setText('posti liberi {}/{}'.format(
            len(self.model.lavori)+self.selected , self.model.numero_postazioni_totali))

        pixmaps = {
            Reception: QPixmap(":/icons/theater_comedy_FILL1_wght500_GRAD200_opsz48_risultato.png"),
            Segreteria: QPixmap(":/icons/fax_FILL1_wght500_GRAD200_opsz48_risultato.png"),
            Amministrazione: QPixmap(":/icons/shield_FILL1_wght500_GRAD200_opsz48_risultato"),
            None: QPixmap(":/icons/person_FILL1_wght600_GRAD200_opsz48_risultato"),
        }
        self.view.getIcon().setPixmap(pixmaps[type(self.model)])

        # Impedisco la rimozione di un posto lavoro se ce ne è solo uno di quel tipo

        self.view.getRimuoviButton().setEnabled(False)
        self.view.getRimuoviButton().setStyleSheet(open(UI_DIR + '/css/grayButton.css', 'r').read())
        for posto_lavoro in self.parent.model.posti_lavoro:
            if type(posto_lavoro) == type(self.model) and posto_lavoro != self.model:
                self.view.getRimuoviButton().setEnabled(True)
                self.view.getRimuoviButton().setStyleSheet(open(UI_DIR + '/css/redButton.css', 'r').read())
