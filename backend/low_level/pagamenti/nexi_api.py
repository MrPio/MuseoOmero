#######################################################
# 
# NexiApi.py
# Python implementation of the Class NexiApi
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import random

from backend.low_level.pagamenti.pagamento import Pagamento


class NexiApi(Pagamento):
    def paga(self, costo: float) -> bool:
        # simulazione embedded
        return random.choices([True, False], [2, 1])[0]
