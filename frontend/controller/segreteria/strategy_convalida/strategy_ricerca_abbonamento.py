#######################################################
# 
# StrategyRicercaAbbonamento.py
# Python implementation of the Class StrategyRicercaAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################

from backend.high_level.clientela.cliente import Cliente
from backend.high_level.museo import Museo
from frontend.controller.segreteria.controller_convalida import ControllerConvalida
from frontend.controller.segreteria.strategy_convalida.strategy_convalida import StrategyConvalida


class StrategyRicercaAbbonamento(StrategyConvalida):

    # def __init__(self) -> None:
    #     self.abbonamento: 'Abbonamento' = None
    #     self.model = Museo.getInstance()

    def initializeUi(self, c: 'ControllerConvalida') -> None:
        from frontend.controller.segreteria.controller_rinnovo_abbonamento import ControllerRinnovoAbbonamento
        from frontend.controller.reception.controller_acquisto_biglietto import ControllerAcquistoBiglietto
        if isinstance(c.previous, ControllerRinnovoAbbonamento):
            c.view.getHeaderLabel().setText('HomeSegreteria ➜ RinnovoAbbonamento')
        elif isinstance(c.previous, ControllerAcquistoBiglietto):
            c.view.getHeaderLabel().setText('CompraBiglietto ➜ RicercaAbbonamento')

    def finalizza(self, c: 'ControllerConvalida', id: str) -> bool:
        from frontend.controller.segreteria.controller_rinnovo_abbonamento import ControllerRinnovoAbbonamento
        from frontend.controller.reception.controller_acquisto_biglietto import ControllerAcquistoBiglietto

        for cliente in Museo.getInstance().visitatori:
            if isinstance(cliente, Cliente):
                for abbonamento in cliente.abbonamenti:
                    if id == abbonamento.qr_code.id:

                        if isinstance(c.previous, ControllerRinnovoAbbonamento):
                            c.previous.model = abbonamento
                            c.previous.showView()
                        elif isinstance(c.previous, ControllerAcquistoBiglietto):
                            c.previous.model.abbonamento = abbonamento

                        if not abbonamento.convalida():
                            c.notifica('Abbonamento scaduto',
                                        "Spiacenti, l\'abbonamento è scaduto " + str(
                                            abbonamento.giorniAllaScadenza() * -1) + " giorni fa.")
                            return False
                        c.previous.showView()
                        c.previous.enableView()
                        c.previous.initializeUi()
                        c.closeView()
                        return True

        c.notifica('Abbonamento non trovato',
                   'Spiacenti, non è stato trovato alcun abbonamento relativo al codice inserito.')

        return False
