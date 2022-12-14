#######################################################
# 
# StrategyRiceviDonazione.py
# Python implementation of the Class StrategyRiceviDonazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
import random

from backend.high_level.museo import Museo
from backend.high_level.personale.richiesta_donazione import RichiestaDonazione
from backend.high_level.personale.segreteria import Segreteria
from backend.low_level.network.sms_message import SMSMessage
from frontend.controller.reception.strategy_aggiungi_opera.strategy_aggiungi_opera import StrategyAggiungiOpera


class StrategyRiceviDonazione(StrategyAggiungiOpera):
    def initializeUi(self, c: 'ControllerAggiungiOpera') -> None:
        c.view.getHeaderLabel().setText('HomeReception ➜ RiceviDonazione')

        museo = Museo.getInstance()
        segreterie = list(filter(lambda s: isinstance(s, Segreteria), museo.posti_lavoro))
        if not segreterie:
            c.notifica('Attenzione!', 'Assicurati di avere almeno una segreteria registrata')
            c.gotoPrevious()

    def onConfermaClicked(self, c: 'ControllerAggiungiOpera') -> None:
        museo = Museo.getInstance()
        richiesta_donazione = RichiestaDonazione(c.model, c.model.ubicazione, SMSMessage('0'))
        segreterie = list(filter(lambda s: isinstance(s, Segreteria), museo.posti_lavoro))
        if segreterie:
            random.choice(segreterie).richieste_donazione.append(richiesta_donazione)
            c.notifica('Richiesta inoltrata','Donazione registrata con successo!')
