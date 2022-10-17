#######################################################
# 
# Abbonamento.py
# Python implementation of the Class Abbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.documento import Documento
from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento
from backend.low_level.pagamenti.nexi_api import NexiApi


class Abbonamento(Documento):

    def __init__(self, tipo: TipoAbbonamento=TipoAbbonamento.MENSILE, dataRilascio: datetime = None):
        super().__init__(NexiApi(), dataRilascio)
        self.date_rinnovo = {}
        self.date_rinnovo[self.data_rilascio]=tipo

    def calcolaCosto(self) -> float:
        return list(self.date_rinnovo.items())[-1][1].cost

    def convalida(self) -> bool:
        self.date_convalida.append(datetime.now())
        return self.pagato and not self.isScaduto()

    def isScaduto(self) -> bool:
        return self.giorniAllaScadenza() > 0

    def giorniAllaScadenza(self) -> int:
        return list(self.date_rinnovo.items())[-1][1].days - (datetime.now() - list(self.date_rinnovo.keys())[-1]).days

    def rinnova(self, tipo: TipoAbbonamento) -> None:
        self.date_rinnovo[datetime.now()]=tipo
        self.acquista()
