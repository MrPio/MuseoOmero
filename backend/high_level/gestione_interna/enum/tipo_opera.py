#######################################################
# 
# TipoOpera.py
# Python implementation of the Enumeration TipoOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################


from enum import Enum


class TipoOpera(Enum):
    TELA, STATUA, QUADRO, FOGLIO, *_ = range(100)
