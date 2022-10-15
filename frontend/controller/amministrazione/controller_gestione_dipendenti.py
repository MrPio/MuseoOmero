#######################################################
# 
# ControllerGestioneDipendenti.py
# Python implementation of the Class ControllerGestioneDipendenti
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################

from backend.high_level.museo import Museo
from frontend.controller.amministrazione.controller_assumi import ControllerAssumi
from frontend.controller.amministrazione.strategy_dipendenti.StrategyDipendenti import StrategyDipendenti
from frontend.controller.amministrazione.widget.controller_widget_dipendente import ControllerWidgetDipendente
from frontend.controller.controller import Controller
from frontend.view.amministrazione.vista_assumi import VistaAssumi
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.amministrazione.widget.widget_dipendente import WidgetDipendente


class ControllerGestioneDipendenti(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __init__(self, view: VistaGestioneDipendenti, previous: Controller, model: Museo, strategy: StrategyDipendenti):
        super().__init__(view)
        self.view: VistaGestioneDipendenti = view
        self.previous = previous
        self.model = model
        self.strategy = strategy
        self.connettiEventi()
        self.initializeUi()

    def __gotoVistaAssumi(self) -> None:
        controller = ControllerAssumi(
            view=VistaAssumi(),
            previous=self,
            model=Museo.getInstance(),
        )
        controller.connettiEventi()
        controller.showView()
        self.disableView()

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getAssumiButton().mouseReleaseEvent = lambda _: self.__gotoVistaAssumi()

    def __renderizzaDipendenti(self) -> list[ControllerWidgetDipendente]:
        result = []
        for dipendente in self.model.dipendenti:
            new_widget = WidgetDipendente(self.view.scrollAreaWidgetContents)

            result.append(ControllerWidgetDipendente(
                view=new_widget,
                parent=self,
                model=dipendente,
                strategy=self.strategy,
            ))
        return result

    def initializeUi(self) -> None:
        self.dipendenti = self.__renderizzaDipendenti()
        self.strategy.initializeUi(self)
        # rimuovo tutti i widget
        for i in reversed(range(self.view.verticalLayout.count())):
            self.view.verticalLayout.itemAt(i).widget().setParent(None)
        for controller in self.dipendenti:
            self.view.verticalLayout.addWidget(controller.view)
