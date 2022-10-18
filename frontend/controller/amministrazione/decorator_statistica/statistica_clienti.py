#######################################################
# 
# StatisticaClienti.py
# Python implementation of the Class StatisticaClienti
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.clientela.cliente import Cliente
from backend.high_level.clientela.visitatore import Visitatore
from backend.high_level.museo import Museo
from frontend.controller.amministrazione.decorator_statistica.statistica import Statistica


class StatisticaClienti(Statistica):
    def __init__(self, controller: 'ControllerVistaStatistiche'):
        self.controller = controller

    def calcola(self) -> None:
        mese = self.controller.mese_selezionato
        if mese is None:
            return

        convalide_visitatori, convalide_clienti = 0, 0
        for visitatore in Museo.getInstance().visitatori:
            for biglietto in visitatore.biglietti:
                for data in biglietto.date_convalida:
                    if type(visitatore) == Visitatore:
                        convalide_visitatori += 1 if data.year == mese.year and data.month == mese.month else 0
                    elif type(visitatore) == Cliente:
                        convalide_clienti += 1 if data.year == mese.year and data.month == mese.month else 0

        tot=convalide_visitatori+convalide_clienti
        self.controller.view.getNumeroVisitatoriLabel().setText(
            'Numero visitatori: {}'.format(str(tot)))
        self.controller.view.getPercentualeAbbonatiLabel().setText(
            'Percentuale abbonati: {}%'.format(str(round(convalide_clienti/(tot)*100,2) if tot!=0 else 0)))
