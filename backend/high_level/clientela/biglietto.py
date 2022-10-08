#######################################################
# 
# Biglietto.py
# Python implementation of the Class Biglietto
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
import Tariffa
import OperatoreAlPubblico
import Documento

class Biglietto(Documento):
    m_Tariffa= Tariffa()

    def calcolaCosto(self) -> float:
        pass

    def convalida(self) -> bool:
        pass

    def __init__(self,dataRilascio : datetimetime = None, reparto : RepartoMuseo = None, tariffa : Tariffa = None):
        pass

    def getReparto(self) -> RepartoMuseo:
        pass

    def getTariffa(self) -> Tariffa:
        pass

    def setReparto(newVal : RepartoMuseo) -> None:
        pass

    def setTariffa(newVal : Tariffa) -> None:
        pass

    def hasGuida(self) -> bool:
        pass

    def getGuida(self) -> OperatoreAlPubblico:
        pass

    def setGuida(newVal : OperatoreAlPubblico) -> None:
        pass

    def setReparto(newVal : RepartoMuseo) -> None:
        pass