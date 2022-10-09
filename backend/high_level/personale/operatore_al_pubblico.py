#######################################################
# 
# OperatoreAlPubblico.py
# Python implementation of the Class OperatoreAlPubblico
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.gestione_interna.turno_guida import TurnoGuida
from backend.high_level.personale.lavoro import Lavoro


class OperatoreAlPubblico(Lavoro):
    m_TurnoGuida= TurnoGuida()

    def __init__(self,contratto : str, stipendio : float, qualificaGuida : str):
        pass

    def assegna(turno : TurnoGuida) -> bool:
        pass

    def getListaTurni(self) -> list[TurnoGuida]:
        pass

    def rimuovi(turno : TurnoGuida) -> bool:
        pass

    def getQualificaGuida(self) -> str:
        pass

    def setQualificaGuida(newVal : str) -> None:
        pass