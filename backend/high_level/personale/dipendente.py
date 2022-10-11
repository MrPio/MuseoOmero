#######################################################
# 
# Dipendente.py
# Python implementation of the Class Dipendente
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.enum.sesso import Sesso
from backend.high_level.personale.credenziale import Credenziale
from backend.high_level.personale.lavoro import Lavoro


class Dipendente():

    def __init__(self, nome: str, cognome: str, dataNascita: datetime, email: str,
                 sesso: Sesso = Sesso.NON_SPECIFICATO, curriculum: str = '',
                 credenziale: Credenziale = None, lavoro: Lavoro | None = None, autogenerato:bool=False):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = dataNascita
        self.email = email
        self.sesso = sesso
        self.curriculum = curriculum
        self.credenziale = Credenziale(nome + cognome) if credenziale == None else credenziale
        self.lavoro = lavoro
        self.autogenerato=autogenerato
        self.lavori_passati: list[Lavoro] = []

    def assumi(self, lavoro: Lavoro) -> bool:
        if self.lavoro is None:
            self.lavoro = lavoro
            return True
        return False

    def licenzia(self, notaLicenziamento: str) -> bool:
        if self.lavoro is not None:
            self.lavoro.licenzia(notaLicenziamento)
            self.lavori_passati.append(self.lavoro)
            self.lavoro = None
            return True
        return False

    def autentifica(self, username: str, password: str) -> bool:
        if self.credenziale is not None:
            return self.credenziale.username == username and self.credenziale.verifica(password)
        return False

    def calcolaEta(self) -> int:
        today = datetime.today()
        # int(True) is 1 and int(False) is 0:
        return today.year - self.data_nascita.year - \
               ((today.month, today.day) < (self.data_nascita.month, self.data_nascita.day))
