import ctypes
import random
import sys

from PyQt5.QtWidgets import QApplication

from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento
from backend.high_level.gestione_interna.enum.periodo_storico import PeriodoStorico
from frontend.controller.controller_home import ControllerHome
from frontend.ui.location import UI_DIR
from frontend.view.vista_home import VistaHome

# for name, value in locals().items():
#     setattr(self,name, value)


def startApp():
    myappid = 'museum.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    # MVC
    controller_home=ControllerHome(VistaHome())
    controller_home.connettiEventi()
    controller_home.showView()
    sys.exit(app.exec())


if __name__=='__main__':
    # startApp()
    print()
