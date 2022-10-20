#######################################################
# 
# Encoding.py
# Python implementation of the Interface Encoding
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################

import abc

from PIL.Image import Image


class Encoding(abc.ABC):
    @abc.abstractmethod
    def encode(self, text: str) -> Image:
        pass

    @abc.abstractmethod
    def decode(self, image: Image) -> str:
        pass
