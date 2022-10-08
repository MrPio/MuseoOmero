#######################################################
# 
# RichiestaDonazione.py
# Python implementation of the Class RichiestaDonazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import Ubicazione
import Opera
import Notification

class RichiestaDonazione:
    def __init__(self,opera : Opera, ubicazione : Ubicazione, email : str = "", tel : int = -1):
        pass

    def accetta(self) -> None:
        pass

    def rifiuta(self) -> None:
        pass

    def notifica(channel : Notification) -> None:
        pass

    def getOpera(self) -> Opera:
        pass

    def getEmailDonante(self) -> str:
        pass

    def setEmailDonante(newVal : str) -> None:
        pass

    def getUbicazione(self) -> Ubicazione:
        pass

    def getTelefonoDonante(self) -> int:
        pass

    def setTelefonoDonante(newVal : int) -> None:
        pass