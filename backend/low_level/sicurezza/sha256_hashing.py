#######################################################
# 
# SHA256Hashing.py
# Python implementation of the Class SHA256Hashing
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import hashlib

from backend.low_level.sicurezza.hashing import Hashing


class SHA256Hashing(Hashing):

    def hash(self, plain: str) -> str:
        '''
        Metodo di hashing con l'algoritmo SHA256
        :return it testo hash-ato
        '''
        return hashlib.sha256(plain.encode('utf-8')).hexdigest()
