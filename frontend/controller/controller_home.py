#######################################################
# 
# ControllerHome.py
# Python implementation of the Class ControllerHome
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from frontend.controller.amministrazione.controller_home_amministrazione import ControllerHomeAmministrazione
from frontend.controller.controller import Controller
from frontend.controller.controller_login import ControllerLogin
from frontend.controller.reception.controller_home_reception import ControllerHomeReception
from frontend.controller.segreteria.controller_home_segreteria import ControllerHomeSegreteria
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_home_amministrazione import VistaHomeAmministrazione
from frontend.view.reception.vista_home_reception import VistaHomeReception
from frontend.view.segreteria.vista_home_segreteria import VistaHomeSegreteria
from frontend.view.vista_home import VistaHome
from frontend.view.vista_login import VistaLogin


class ControllerHome(Controller):
    def __init__(self, view: VistaHome):
        super().__init__(view,reactOnShift=True)
        self.view: VistaHome = view
        self.connettiEventi()
        self.initializeUi()
        self.showView()

    def __gotoLogin(self, reparto) -> None:
        self.next = ControllerLogin(
            view=VistaLogin(),
            model=Museo.getInstance(),
            home=self,
            repartoScelto=reparto,
        )

        if len(Museo.getInstance().dipendenti) == 1 and Museo.getInstance().dipendenti[0].autogenerato:
            self.notifica('Primo Accesso', '• Username --> {admin} \r\n• Password --> {admin} \r\nNon appena '
                                           'crei un account amministratore rimuoverò questo account temporaneo')

    def __onReceptionClicked(self) -> None:
        if self.shift:
            self.shift = False
            self.view.go_debug_mode(False)

            self.next = ControllerHomeReception(VistaHomeReception(), self, None)
        else:
            self.__gotoLogin('reception')

    def __onSegreteriaClicked(self) -> None:
        if self.shift:
            self.shift=False
            self.view.go_debug_mode(False)

            self.next = ControllerHomeSegreteria(VistaHomeSegreteria(), self, None)
        else:
            self.__gotoLogin('segreteria')

    def __onAmministrazioneClicked(self) -> None:
        if self.shift:
            self.shift = False
            self.view.go_debug_mode(False)

            self.next = ControllerHomeAmministrazione(VistaHomeAmministrazione(), self, None)
        else:
            self.__gotoLogin('amministrazione')

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getReceptionButton().mouseReleaseEvent = lambda _: self.__onReceptionClicked()
        self.view.getSegreteriaButton().mouseReleaseEvent = lambda _: self.__onSegreteriaClicked()
        self.view.getAmministrazioneButton().mouseReleaseEvent = lambda _: self.__onAmministrazioneClicked()
