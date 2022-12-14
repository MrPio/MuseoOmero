#######################################################
#
# ControllerGestioneMostre.py
# Python implementation of the Class ControllerGestioneMostre
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
#
#######################################################
import datetime

from backend.high_level.gestione_interna.enum.periodo_storico import PeriodoStorico
from backend.high_level.gestione_interna.mostra import Mostra
from backend.high_level.museo import Museo
from frontend.controller.amministrazione.controller_allestisci_mostra import ControllerAllestisciMostra
from frontend.controller.amministrazione.controller_mostra import ControllerMostra
from frontend.controller.controller import Controller
from frontend.view.amministrazione.vista_allestisci_mostra import VistaAllestisciMostra
from frontend.view.amministrazione.vista_gestione_mostre import VistaGestioneMostre
from frontend.view.amministrazione.vista_mostra import VistaMostra


class ControllerGestioneMostre(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaGestioneMostre, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaGestioneMostre = view
        self.previous = previous
        self.model = model

        self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()

    def __gotoVistaMostra(self) -> None:
        mostra_attuale = None
        for mostra in Museo.getInstance().mostre:
            if mostra.isInCorso():
                mostra_attuale = mostra
        if mostra_attuale is None:
            self.notifica('Nessuna mostra in corso', 'Al momento non è in corso alcuna mostra!')
        else:
            self.next = ControllerMostra(
                view=VistaMostra(),
                previous=self,
                model=mostra_attuale,
            )

    def __gotoVistaAllestisciMostra(self) -> None:
        mostra_attuale = None
        for mostra in Museo.getInstance().mostre:
            if mostra.isInCorso():
                mostra_attuale = mostra
        if mostra_attuale is None:
            self.next = ControllerAllestisciMostra(
                view=VistaAllestisciMostra(),
                previous=self,
                model=Mostra(
                    dataInizio=datetime.datetime.now(),
                    dataFine=datetime.datetime.now(),
                    titolo='',
                    descrizione='nuova mostra',
                    tema=PeriodoStorico.PREISTORIA,
                ),
            )


        else:
            self.notifica('Mostra in corso',
                                'Al momento è già in corso una mostra, aspetta che termini o rimuovila per allestirne un\'altra')

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getVisualizzaMostraAttualeButton().mouseReleaseEvent = lambda _: self.__gotoVistaMostra()
        self.view.getAllestisciNuovaMostraButton().mouseReleaseEvent = lambda _: self.__gotoVistaAllestisciMostra()
