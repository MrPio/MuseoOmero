#######################################################
# 
# ControllerModificaTurnoGuida.py
# Python implementation of the Class ControllerModificaTurnoGuida
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
import datetime

from backend.high_level.gestione_interna.turno_guida import TurnoGuida
from backend.high_level.personale.operatore_al_pubblico import OperatoreAlPubblico
from frontend.controller.amministrazione.controller_gestione_dipendenti import ControllerGestioneDipendenti
from frontend.controller.amministrazione.strategy_dipendenti.StrategySelezionaGuida import StrategySelezionaGuida
from frontend.controller.controller import Controller
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.reception.vista_modifica_turno_guida import VistaModificaTurnoGuida


class ControllerModificaTurnoGuida(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaModificaTurnoGuida, previous: Controller, model: TurnoGuida):
        super().__init__(view)
        self.view: VistaModificaTurnoGuida = view
        self.previous = previous
        self.model = model
        self.guida: OperatoreAlPubblico | None = None

        self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()

        self.view.getErrorLabel().setVisible(False)

    def __gotoGestisciDipendenti(self) -> None:
        self.__setModelDataInizioDataFine()

        from backend.high_level.museo import Museo
        self.next = ControllerGestioneDipendenti(
            view=VistaGestioneDipendenti(),
            previous=self,
            model=Museo.getInstance(),
            strategy=StrategySelezionaGuida(),
        )

    def __setModelDataInizioDataFine(self) -> None:
        self.model.capienza = self.view.getCapienzaSpinBox().value()
        data_inizio = datetime.datetime(
            year=self.model.data_inizio.year,
            month=self.model.data_inizio.month,
            day=self.model.data_inizio.day,
            hour=int(self.view.getOreComboBox().currentText()),
            minute=int(self.view.getMinutiComboBox().currentText()),
        )

        self.model.data_inizio = data_inizio
        self.model.data_fine = data_inizio + datetime.timedelta(
            minutes=int(self.view.getDurataComboBox().currentText()))

    def __onConfermaClicked(self) -> None:
        self.__setModelDataInizioDataFine()

        if self.guida is not None and not self.guida.isOccupato(self.model.data_inizio,self.model.data_fine):
            self.guida.assegna(self.model)
        else:
            self.view.getErrorLabel().setVisible(True)
            return

        from backend.high_level.museo import Museo
        if self.model not in Museo.getInstance().turni_guida:
            Museo.getInstance().turni_guida.append(self.model)

        self.__gotoPrevious()

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getConfermaButton().clicked.connect(self.__onConfermaClicked)
        self.view.getCambiaButton().clicked.connect(self.__gotoGestisciDipendenti)

    def initializeUi(self) -> None:
        self.view.getCapienzaSpinBox().setValue(self.model.capienza)
        self.view.getOreComboBox().setCurrentText(str(self.model.data_inizio.hour))
        self.view.getMinutiComboBox().setCurrentText(str((self.model.data_inizio.minute // 15) * 15))
        self.view.getDurataComboBox().setCurrentText(str(self.model.durata))
