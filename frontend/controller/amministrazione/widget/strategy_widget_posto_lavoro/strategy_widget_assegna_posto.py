#######################################################
# 
# StrategyWidgetAssegnaPosto.py
# Python implementation of the Class StrategyWidgetAssegnaPosto
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from frontend.controller.amministrazione.widget.strategy_widget_posto_lavoro.strategy_widget_posto_lavoro import \
    StrategyWidgetPostoLavoro
from frontend.ui.location import UI_DIR


class StrategyWidgetAssegnaPosto(StrategyWidgetPostoLavoro):
    def initializeUi(self, c: 'ControllerWidgetPostoLavoro') -> None:
        c.view.getAssegnaPostoButton().setVisible(True)
        c.view.getModificaButton().setVisible(False)
        c.view.getRimuoviButton().setVisible(False)
        if len(c.model.lavori) >= c.model.numero_postazioni_totali:
            c.view.getAssegnaPostoButton().setEnabled(False)
            c.view.getAssegnaPostoButton().setStyleSheet(open(UI_DIR + '/css/grayButton.css', 'r').read())
