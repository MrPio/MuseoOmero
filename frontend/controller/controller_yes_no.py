#######################################################
# 
# ControllerYesNo.py
# Python implementation of the Class ControllerYesNo
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################

from frontend.controller.controller import Controller
from frontend.view.vista_yes_no import VistaYesNo


class ControllerYesNo(Controller):
    def __init__(self, view: VistaYesNo, previous: Controller | None, onConfermaCliked: 'function',
                 message: str = 'Sicuro di voler procedere?') -> object:
        super().__init__(view)
        self.view: VistaYesNo = view
        self.previous: Controller = previous
        self.onConfermaCliked = onConfermaCliked
        self.view.getMessaggioLabel().setText(message)
        if self.previous is not None:
            self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()

    def __onAnnullaClicked(self) -> None:
        self.closeView()
        if self.previous is not None:
            self.previous.enableView()

    def __onConfermaClicked(self) -> None:
        self.closeView()
        if self.previous is not None:
            self.previous.enableView()
        self.onConfermaCliked()

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getConfermaButton().mouseReleaseEvent = lambda _: self.__onConfermaClicked()
        self.view.getAnnullaButton().mouseReleaseEvent = lambda _: self.__onAnnullaClicked()
