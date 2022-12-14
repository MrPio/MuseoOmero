#######################################################
# 
# Segretario.py
# Python implementation of the Class Segretario
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.personale.lavoro import Lavoro


class Segretario(Lavoro):
    def __init__(self, stipendio: float, numPostazione: int, sportelloAssegnato: int, contratto: str = ''):
        super().__init__(stipendio, numPostazione, contratto)
        self.sportello_assegnato = sportelloAssegnato
