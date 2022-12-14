#######################################################
# 
# QRCodeEncoding.py
# Python implementation of the Class QRCodeEncoding
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import PIL
import cv2
import qrcode

from backend.low_level.sicurezza.encoding import Encoding


class QRCodeEncoding(Encoding):

    def encode(self, text: str) -> PIL.Image:
        '''
        Conversione da testo a QrCode\n
        :param text
        :return: PIL.Image
        '''
        return qrcode.make(text)

    def decode(self, image: PIL.Image) -> str:
        '''
        Conversione da QrCode a testo

        :param image
        :return: str
        '''
        return cv2.QRCodeDetector().detectAndDecode(image)[0]
