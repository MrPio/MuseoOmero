#######################################################
# 
# RepartoMuseo.py
# Python implementation of the Enumeration RepartoMuseo
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################


from enum import Enum


class RepartoMuseo(Enum):
    MUSEO_APERTO, MOSTRA, *_ = range(100)
