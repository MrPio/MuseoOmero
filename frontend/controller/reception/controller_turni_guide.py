#######################################################
# 
# ControllerTurniGuide.py
# Python implementation of the Class ControllerTurniGuide
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime, timedelta

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.controller.reception.strategy_turni_guide.strategy_turni_guide import StrategyTurniGuide
from frontend.controller.reception.widget.controller_widget_turno_guida import ControllerWidgetTurnoGuida
from frontend.ui.location import UI_DIR
from frontend.view.reception.vista_turni_guide import VistaTurniGuide
from frontend.view.reception.widget.widget_turno_guida import WidgetTurnoGuida


class ControllerTurniGuide(Controller):

    def __init__(self, view: VistaTurniGuide, previous: Controller, model: Museo, strategy: StrategyTurniGuide):
        super().__init__(view)
        self.view: VistaTurniGuide = view
        self.previous = previous
        self.model = model
        self.strategy = strategy
        self.aggiungi_alla_lista = None
        self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    # def __gotoVistaModificaTurnoGuida(self) -> None:
    #     pass
    def __onRicercaClicked(self, c) -> None:
        self.initializeUi()

    def __onFrecciaSinistraClicked(self) -> None:
        date = None
        try:
            date = datetime.strptime(self.view.getDataLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return
        self.view.getDataLineEdit().setText((date - timedelta(days=1)).strftime('%d/%m/%Y'))
        self.initializeUi()

    def __onFrecciaDestraClicked(self) -> None:
        date = None
        try:
            date = datetime.strptime(self.view.getDataLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return
        self.view.getDataLineEdit().setText((date + timedelta(days=1)).strftime('%d/%m/%Y'))
        self.initializeUi()

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getFrecciaSinistra().mouseReleaseEvent = lambda _: self.__onFrecciaSinistraClicked()
        self.view.getFrecciaDestra().mouseReleaseEvent = lambda _: self.__onFrecciaDestraClicked()
        self.button_release = self.view.getRicercaButton().mouseReleaseEvent
        self.view.getRicercaButton().clicked[bool].connect(self.__onRicercaClicked)

    def __renderizzaTurniGuida(self) -> list[ControllerWidgetTurnoGuida]:
        result = []
        self.date = None
        try:
            self.date = datetime.strptime(self.view.getDataLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            self.date = datetime.today()
            self.view.getDataLineEdit().setText(self.date.strftime('%d/%m/%Y'))

        for turno_guida in self.model.turni_guida:
            if (turno_guida.data_inizio.day, turno_guida.data_inizio.month, turno_guida.data_inizio.year) == \
                    (self.date.day, self.date.month, self.date.year):
                result.append(ControllerWidgetTurnoGuida(
                    view=WidgetTurnoGuida(self.view.turniGuideListView),
                    model=turno_guida,
                    parent=self,
                ))
        return result

    def initializeUi(self) -> None:
        self.turni_guida = self.__renderizzaTurniGuida()

        # rimuovo tutti i widget
        self.aggiungi_alla_lista = None
        for i in reversed(range(self.view.verticalLayout.count())):
            self.view.verticalLayout.itemAt(i).widget().setParent(None)

        if len(self.turni_guida) == 0:
            label = QLabel('Niente da mostrate qui.', self.view.turniGuideListView)
            label.setStyleSheet(open(UI_DIR + '/css/textLabel.css', 'r').read())
            label.setAlignment(Qt.AlignCenter)
            self.view.verticalLayout.addWidget(label)
        for controller in self.turni_guida:
            self.view.verticalLayout.addWidget(controller.view)

        self.strategy.initializeUi(self)
