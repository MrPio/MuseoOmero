#######################################################
# 
# Visitatore.py
# Python implementation of the Class Visitatore
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.biglietto import Biglietto
from backend.high_level.clientela.enum.sesso import Sesso


class Visitatore:

    def __init__(self,provenienza : str = "", sesso : Sesso = Sesso.NON_SPECIFICATO, dataNascita : datetime = None):
        self.provenienza=provenienza
        self.sesso=sesso
        self.data_nascita = dataNascita
        self.biglietti:list[Biglietto]=[]
