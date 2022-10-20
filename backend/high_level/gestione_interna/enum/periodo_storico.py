#######################################################
#
# PeriodoStorico.py
# Python implementation of the Enumeration PeriodoStorico
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
#
#######################################################

from enum import Enum


class PeriodoStorico(Enum):
    PREISTORIA, CLASSICO, RINASCIMENTO, BAROCCO, NEOCLASSICO, ROMANTICISMO, CONTEMPORANEO, IMPRESSIONISMO, AVANGUARDISTA, *_ = range(
        100)
