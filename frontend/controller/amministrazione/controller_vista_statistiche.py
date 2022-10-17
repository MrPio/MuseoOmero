#######################################################
# 
# ControllerVistaStatistiche.py
# Python implementation of the Class ControllerVistaStatistiche
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime, timedelta

from PyQt5.QtChart import QChartView
from dateutil.relativedelta import relativedelta

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
        self.connettiEventi()
        self.initializeUi()
        self.current_index=0
        # self.grafici

    def __onVisualizzaClicked(self) -> None:
        self.initializeUi()
    def __onFrecciaSinistraClicked(self) -> None:
        date = None
        try:
            date = datetime.strptime(self.view.getDataLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return
        self.view.getDataLineEdit().setText((date - relativedelta(months=1)).strftime('%d/%m/%Y'))
        self.initializeUi()

    def __onFrecciaDestraClicked(self) -> None:
        date = None
        try:
            date = datetime.strptime(self.view.getDataLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return
        self.view.getMeseLineEdit().setText((date + relativedelta(months=1)).strftime('%d/%m/%Y'))
        self.initializeUi()
    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getVisualizzaButton().clicked.connect(self.__onVisualizzaClicked())
        self.view.getLeftArrowIcon().mouseReleaseEvent = lambda _: self.__onFrecciaSinistraClicked()
        self.view.getRightArrowIcon().mouseReleaseEvent = lambda _: self.__onFrecciaDestraClicked()

    def addGrafico(chart : QChartView) -> None:
        pass #TODO

    def mostraStatistiche(clientiTotali : int, mediaGiornaliera : float, devStdGiornaliera : float) -> None:
        pass #TODO

    def initializeUi(self) -> None:

