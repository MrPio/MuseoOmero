#######################################################
# 
# Segreteria.py
# Python implementation of the Class Segreteria
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import random

from backend.high_level.museo import Museo
from backend.high_level.personale.amministrazione import Amministrazione
from backend.high_level.personale.dipendente import Dipendente
from backend.high_level.personale.posto_lavoro import PostoLavoro
from backend.high_level.personale.richiesta_donazione import RichiestaDonazione
from backend.high_level.personale.segretario import Segretario


class Segreteria(PostoLavoro):
    def __init__(self, nome: str, piano: int, numPostazioni: int, sportelli: int, telFisso: str, descr: str = ""):
        super().__init__(nome, piano, numPostazioni)
        self.sportelli = sportelli
        self.telefono_fisso = telFisso
        self.descrizione = descr
        self.richieste_donazione: list[RichiestaDonazione] = []

    def assumi(self, dipendente: Dipendente) -> bool:
        lavoro = Segretario(
            contratto='contratto a tempo indeterminato',
            stipendio=max(800.0, random.gauss(1300, 260)),
            numPostazione=len(self.lavori) + 1,
            sportelloAssegnato=len(self.lavori) + 1
        )
        if esito := dipendente.assumi(lavoro=lavoro):
            dipendente.posto_lavoro = self
            self.lavori.append(lavoro)
        return esito

    def promuovi(self, dipendente: Dipendente) -> bool:
        for lavoro in Museo.getInstance().posti_lavoro:
            if isinstance(lavoro, Amministrazione):
                if len(lavoro.lavori) < lavoro.numero_postazioni_totali:
                    self.licenzia(dipendente, 'promosso ad amministratore')
                    lavoro.assumi(dipendente)
                    return True
        return False
