#######################################################
# 
# PostoLavoro.py
# Python implementation of the Class PostoLavoro
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import abc



class PostoLavoro(abc.ABC):
    def __init__(self, nome:str , piano: int, numPostazioni: int, descrizione: str = ''):
        self.nome=nome
        self.piano = piano
        self.numero_postazioni_totali = numPostazioni
        self.descrizione = descrizione
        self.lavori = []

    @abc.abstractmethod
    def assumi(self, dipendente: 'Dipendente') -> bool:
        pass

    def licenzia(self, dipendente: 'Dipendente', notaLicensiamento: str) -> bool:
        for lavoro in self.lavori:
            if lavoro is dipendente.lavoro:
                self.lavori.remove(lavoro)
                dipendente.licenzia(notaLicensiamento)
                return True
        return False
    @abc.abstractmethod
    def promuovi(self, dipendente: 'Dipendente') -> bool:
        pass

    def rimuovi(self,museo:'Museo'):
        for dipendente in museo.dipendenti:
            if dipendente.posto_lavoro is self:
                dipendente.posto_lavoro=None
        museo.posti_lavoro.remove(self)