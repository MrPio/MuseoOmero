#######################################################
# 
# ControllerAcquistoOpere.py
# Python implementation of the Class ControllerAcquistoOpere
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.gestione_interna.opera import Opera
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.controller.reception.controller_aggiungi_opera import ControllerAggiungiOpera
from frontend.controller.reception.strategy_aggiungi_opera.strategy_acquista_opera import StrategyAcquistaOpera
from frontend.view.amministrazione.vista_acquisto_opere import VistaAcquistoOpere
from frontend.view.reception.vista_aggiungi_opera import VistaAggiungiOpera


class ControllerAcquistoOpere(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaAcquistoOpere, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaAcquistoOpere = view
        self.previous = previous
        self.model = model
        self.connettiEventi()

    def __gotoVistaAggiungiOpera(self) -> None:
        self.next = ControllerAggiungiOpera(
            view=VistaAggiungiOpera(),
            previous=self,
            model=Opera(),
            strategy=StrategyAcquistaOpera(),
        )
        self.next.showView()
        self.disableView()

    def __gotoVistaRicercaOpera(self) -> None:
        Controller.notifica('Funzione non disponibile',
                            'Spiacenti, ma questa funzione non è ancora stata implementata.')

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getInserisciManualmenteButton().mouseReleaseEvent = lambda _: self.__gotoVistaAggiungiOpera()
        self.view.getRicercaSulWebButton().mouseReleaseEvent = lambda _: self.__gotoVistaRicercaOpera()
