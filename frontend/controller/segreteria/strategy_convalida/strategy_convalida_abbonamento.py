#######################################################
# 
# StrategyConvalidaAbbonamento.py
# Python implementation of the Class StrategyConvalidaAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################

from backend.high_level.clientela.cliente import Cliente
from backend.high_level.museo import Museo
from frontend.controller.segreteria.controller_vista_abbonamento import ControllerVistaAbbonamento
from frontend.controller.segreteria.strategy_convalida.strategy_convalida import StrategyConvalida
from frontend.view.segreteria.vista_abbonamento import VistaAbbonamento


class StrategyConvalidaAbbonamento(StrategyConvalida):

    # def __init__(self) -> None:
    #     self.abbonamento: 'Abbonamento' | None = None
    #     self.model = Museo.getInstance()

    def initializeUi(self, c: 'ControllerConvalida') -> None:
        c.view.getHeaderLabel().setText('HomeSegreteria ➜ ConvalidaAbbonamento')

    def finalizza(self, c: 'ControllerConvalida', id: str) -> bool:
        for cliente in Museo.getInstance().visitatori:
            if isinstance(cliente,Cliente):
                for abbonamento in cliente.abbonamenti:
                    if id == abbonamento.qr_code.id:
                        c.next = ControllerVistaAbbonamento(
                            view=VistaAbbonamento(),
                            previous=c,
                            model=abbonamento,
                        )
                        if not abbonamento.convalida():
                            c.notifica('Abbonamento scaduto',
                                       "Spiacenti, l\'abbonamento è scaduto "+ str(abbonamento.giorniAllaScadenza()*-1) +" giorni fa.")
                            return False
                        c.next.showView()
                        c.disableView()
                        return True

        c.notifica('Abbonamento non trovato',
                   'Spiacenti, non è stato trovato alcun abbonamento relativo al codice inserito.')
        return False
