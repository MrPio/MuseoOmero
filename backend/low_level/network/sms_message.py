#######################################################
# 
# SMSMessage.py
# Python implementation of the Class SMSMessage
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from backend.low_level.network.notification import Notification


class SMSMessage(Notification):
    def __init__(self, telefono: str):
        self.telefono = telefono

    def send(self, title: str, content: str) -> None:
        # necessario un numero telefono di business e relative api
        pass
