#######################################################
# 
# ControllerVistaStatistiche.py
# Python implementation of the Class ControllerVistaStatistiche
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from PyQt5 import sip

from frontend.controller.amministrazione.decorator_statistica.grafico_su_eta import GraficoSuEta
from frontend.controller.amministrazione.decorator_statistica.grafico_su_provenienza import GraficoSuProvenienza
from frontend.controller.amministrazione.decorator_statistica.grafico_su_sesso import GraficoSuSesso
from frontend.controller.amministrazione.decorator_statistica.statistica_clienti import StatisticaClienti
from frontend.controller.controller import Controller
from frontend.view.amministrazione.vista_statistiche import VistaStatistiche


class ControllerVistaStatistiche(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaStatistiche, previous: Controller):
        super().__init__(view)
        self.view: VistaStatistiche = view
        self.previous = previous
        self.current_index = 0
        self.mese_selezionato = None
        self.charts_layout = []
        self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()
        self.view.getMeseLineEdit().setText(datetime.today().strftime("%m/%Y"))

    def __onVisualizzaClicked(self) -> None:
        try:
            self.mese_selezionato = datetime.strptime(self.view.getMeseLineEdit().text(), '%m/%Y')
        except Exception as e:
            print(e)
            return

        self.__svuotaGrafici()
        self.current_index = 0

        # Component base
        self.statistica_decorator = StatisticaClienti(self)

        # Decorators aggiuntivi
        if self.view.provenienzaCheckBoxStatus:
            self.statistica_decorator = GraficoSuProvenienza(self, self.statistica_decorator)
        if self.view.etaCheckBoxStatus:
            self.statistica_decorator = GraficoSuEta(self, self.statistica_decorator)
        if self.view.sessoCheckBoxStatus:
            self.statistica_decorator = GraficoSuSesso(self, self.statistica_decorator)

        self.statistica_decorator.calcola()
        self.initializeUi()

    def __onFrecciaSinistraClicked(self) -> None:
        self.current_index -= 1 if self.current_index > 0 else 0
        self.initializeUi()

    def __onFrecciaDestraClicked(self) -> None:
        self.current_index += 1 if self.current_index < len(self.charts_layout) - 1 else 0
        self.initializeUi()

    def __setVisibilitaFrecce(self) -> None:
        self.view.getLeftArrowIcon().setVisible(self.current_index > 0)
        self.view.getRightArrowIcon().setVisible(self.current_index < len(self.charts_layout) - 1)

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getVisualizzaButton().clicked.connect(self.__onVisualizzaClicked)
        self.view.getLeftArrowIcon().mouseReleaseEvent = lambda _: self.__onFrecciaSinistraClicked()
        self.view.getRightArrowIcon().mouseReleaseEvent = lambda _: self.__onFrecciaDestraClicked()

    def initializeUi(self) -> None:
        if len(self.charts_layout) > 0:
            self.__svuotaGrafici()
            self.statistica_decorator.calcola()
            self.view.getVisualizzaStatisticheFrame().setLayout(self.charts_layout[self.current_index])
        self.__setVisibilitaFrecce()
        self.view.getSessoCheckBox().click()

    def __svuotaGrafici(self):
        def __deleteLayout(layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        __deleteLayout(item.layout())
                sip.delete(layout)

        for layout in self.charts_layout:
            __deleteLayout(layout)
        self.charts_layout = []
