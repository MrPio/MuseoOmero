#######################################################
# 
# StrategyRicercaAbbonamento.py
# Python implementation of the Class StrategyRicercaAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
import winotify

from backend.high_level.clientela.abbonamento import Abbonamento
from backend.high_level.clientela.cliente import Cliente
from backend.high_level.museo import Museo
from frontend.controller.segreteria.controller_convalida import ControllerConvalida
from frontend.controller.segreteria.strategy_convalida.strategy_convalida import StrategyConvalida


class StrategyRicercaAbbonamento(StrategyConvalida):

    def __init__(self) -> None:
        self.abbonamento: 'Abbonamento' | None = None
        self.model = Museo.getInstance()

    def initializeUi(self, c: 'ControllerConvalida') -> None:
        c.view.getHeaderLabel().setText('HomeSegreteria ➜ RicercaAbbonamento')

    def finalizza(self, c: 'ControllerConvalida', id: str) -> bool:
        for cliente in self.model.visitatori:
            if isinstance(cliente, Cliente):
                for abbonamento in cliente.abbonamenti:
                    if id == abbonamento.qr_code.id:
                        titolo = "Abbonamento trovato!"
                        messaggio = ''
                        if abbonamento.giorniAllaScadenza():
                            messaggio = "L'abbonamento appartiene a " + cliente.nome + " " + cliente.cognome + "\r\nTerminerà tra" + str(
                                abbonamento.giorniAllaScadenza()) + " giorni"
                        elif abbonamento.giorniAllaScadenza() == 0:
                            messaggio = "L'abbonamento appartiene a " + cliente.nome + " " + cliente.cognome + "\r\nTerminerà oggi"
                        elif abbonamento.giorniAllaScadenza() < 0:
                            titolo = 'Abbonamento scaduto!'
                            messaggio = "L'abbonamento appartiene a " + cliente.nome + " " + cliente.cognome + "\r\nSi prega di rinnovarlo"

                        c.notifica(titolo, messaggio)
                        c.previous.model.abbonamento = abbonamento
                        c.previous.enableView()
                        c.closeView()
                        return True

        c.notifica('Abbonamento non trovato',
                   'Spiacenti, non è stato trovato alcun abbonamento relativo al codice inserito.')

        return False
