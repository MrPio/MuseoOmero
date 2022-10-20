#######################################################
# 
# ControllerHomeAmministrazione.py
# Python implementation of the Class ControllerHomeAmministrazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from backend.high_level.personale.dipendente import Dipendente
from frontend.controller.amministrazione.controller_acquisto_opere import ControllerAcquistoOpere
from frontend.controller.amministrazione.controller_backups import ControllerBackups
from frontend.controller.amministrazione.controller_gestione_dipendenti import ControllerGestioneDipendenti
from frontend.controller.amministrazione.controller_gestione_mostre import ControllerGestioneMostre
from frontend.controller.amministrazione.controller_gestione_posti_lavoro import ControllerGestionePostiLavoro
from frontend.controller.amministrazione.controller_vista_report_incassi import ControllerVistaReportIncassi
from frontend.controller.amministrazione.controller_vista_statistiche import ControllerVistaStatistiche
from frontend.controller.amministrazione.strategy_dipendenti.StrategyGestisciDipendenti import \
    StrategyGestisciDipendenti
from frontend.controller.controller import Controller
from frontend.controller.controller_account import ControllerAccount
from frontend.controller.reception.controller_turni_guide import ControllerTurniGuide
from frontend.controller.reception.strategy_turni_guide.strategy_gestisci_turni_guide import StrategyGestisciTurniGuide
from frontend.view.amministrazione.vista_acquisto_opere import VistaAcquistoOpere
from frontend.view.amministrazione.vista_backups import VistaBackups
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.amministrazione.vista_gestione_mostre import VistaGestioneMostre
from frontend.view.amministrazione.vista_gestione_posti_lavoro import VistaGestionePostiLavoro
from frontend.view.amministrazione.vista_home_amministrazione import VistaHomeAmministrazione
from frontend.view.amministrazione.vista_report_incassi import VistaReportIncassi
from frontend.view.amministrazione.vista_statistiche import VistaStatistiche
from frontend.view.reception.vista_turni_guide import VistaTurniGuide
from frontend.view.vista_account import VistaAccount


class ControllerHomeAmministrazione(Controller):
    def __init__(self, view: VistaHomeAmministrazione, home: Controller, dipendente: Dipendente):
        super().__init__(view)
        self.view: VistaHomeAmministrazione = view
        self.home = home
        self.dipendente = dipendente
        self.initializeUi()

    def initializeUi(self) -> None:
        if self.dipendente.autogenerato:
            Controller.notifica('Primo Accesso',
                                'Benvenuto! Per favore, prima di iniziare l\'utilizzo del software registra i dipendenti')
            for el in [
                self.view.getGestisciBackupsButton(),
                self.view.getAcquistaOpereButton(),
                self.view.getVisualizzaReportIncassi(),
                self.view.getGestisciMostreButton(),
                self.view.getGestisciTurniGuideButton(),
                # self.view.getGestisciStruttureButton(),
                self.view.getVisualizzaStatisticheButton()
            ]:
                el.setEnabled(False)

    def __gotoVistaAccount(self) -> None:
        self.next = ControllerAccount(
            view=VistaAccount(),
            previous=self,
            home=self.home,
            model=self.dipendente,
        )
        self.next.showView()
        self.disableView()

    def __gotoVistaGestioneDipendenti(self) -> None:
        self.next = ControllerGestioneDipendenti(
            view=VistaGestioneDipendenti(),
            previous=self,
            model=Museo.getInstance(),
            strategy=StrategyGestisciDipendenti()
        )
        self.next.showView()
        self.disableView()

    def __gotoGestionePostiLavoro(self) -> None:
        self.next = ControllerGestionePostiLavoro(
            view=VistaGestionePostiLavoro(),
            previous=self,
            model=Museo.getInstance(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaGestioneTurniGuida(self) -> None:
        self.next = ControllerTurniGuide(
            view=VistaTurniGuide(),
            previous=self,
            model=Museo.getInstance(),
            strategy=StrategyGestisciTurniGuide(),
        )
        self.next.showView()
        self.disableView()

    def __gotoVistaGestioneMostre(self) -> None:
        self.next = ControllerGestioneMostre(
            view=VistaGestioneMostre(),
            previous=self,
            model=Museo.getInstance(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaStatistiche(self) -> None:
        self.next = ControllerVistaStatistiche(
            view=VistaStatistiche(),
            previous=self,
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaReportIncassi(self) -> None:
        self.next = ControllerVistaReportIncassi(
            view=VistaReportIncassi(),
            previous=self,
            model=Museo.getInstance(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaAcquistaOpere(self) -> None:
        self.next = ControllerAcquistoOpere(
            view=VistaAcquistoOpere(),
            previous=self,
            model=Museo.getInstance(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaBackups(self) -> None:
        self.next = ControllerBackups(
            view=VistaBackups(),
            previous=self,
            model=Museo.getInstance(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def connettiEventi(self) -> None:
        self.view.getAccountIcon().mouseReleaseEvent = lambda _: self.__gotoVistaAccount()
        self.view.getGestisciDipendentiButton().mouseReleaseEvent = lambda _: self.__gotoVistaGestioneDipendenti()
        self.view.getGestisciStruttureButton().mouseReleaseEvent = lambda _: self.__gotoGestionePostiLavoro()
        self.view.getGestisciTurniGuideButton().mouseReleaseEvent = lambda _: self.__gotoVistaGestioneTurniGuida()
        self.view.getGestisciMostreButton().mouseReleaseEvent = lambda _: self.__gotoVistaGestioneMostre()
        self.view.getVisualizzaStatisticheButton().mouseReleaseEvent = lambda _: self.__gotoVistaStatistiche()
        self.view.getVisualizzaReportIncassi().mouseReleaseEvent = lambda _: self.__gotoVistaReportIncassi()
        self.view.getAcquistaOpereButton().mouseReleaseEvent = lambda _: self.__gotoVistaAcquistaOpere()
        self.view.getGestisciBackupsButton().mouseReleaseEvent = lambda _: self.__gotoVistaBackups()
