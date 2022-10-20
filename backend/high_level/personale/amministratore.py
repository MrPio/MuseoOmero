#######################################################
# 
# Amministratore.py
# Python implementation of the Class Amministratore
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.personale.lavoro import Lavoro


class Amministratore(Lavoro):
    def __init__(self, stipendio: float, numPostazione: int, contratto: str = '', fondatore: bool = False):
        super().__init__(stipendio, numPostazione, contratto)
        self.fondatore = fondatore
