import ctypes
import sys

import winotify
from PyQt5.QtWidgets import QApplication

from frontend.controller.amministrazione.controller_gestione_dipendenti import ControllerGestioneDipendenti
from frontend.controller.controller_home import ControllerHome
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.vista_home import VistaHome


# for name, value in locals().items():
#     setattr(self,name, value)


def startApp():
    # fix icona non visibile
    myappid = 'museum.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    # MVC
    vista_home = VistaGestioneDipendenti()
    controller_home = ControllerGestioneDipendenti(vista_home,None,None)
    controller_home.connettiEventi()
    controller_home.showView()

    sys.exit(app.exec())


if __name__ == '__main__':
    # TODO continuare a runnure e a risolvere tutti gli errori che si presentano
    startApp()

