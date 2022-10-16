import ctypes
import datetime
import sys

import winotify
from PyQt5.QtWidgets import QApplication

from frontend.controller.amministrazione.controller_gestione_dipendenti import ControllerGestioneDipendenti
from frontend.controller.amministrazione.controller_home_amministrazione import ControllerHomeAmministrazione
from frontend.controller.controller_home import ControllerHome
from frontend.controller.reception.controller_acquisto_biglietto import ControllerAcquistoBiglietto
from frontend.controller.reception.controller_home_reception import ControllerHomeReception
from frontend.controller.reception.controller_ricerca_opera import ControllerRicercaOpera
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.amministrazione.vista_home_amministrazione import VistaHomeAmministrazione
from frontend.view.reception.vista_acquisto_biglietto import VistaAcquistoBiglietto
from frontend.view.reception.vista_home_reception import VistaHomeReception
from frontend.view.reception.vista_ricerca_opera import VistaRicercaOpera
from frontend.view.vista_home import VistaHome


# for name, value in locals().items():
#     setattr(self,name, value)


def startApp():
    # fix icona non visibile
    myappid = 'museum.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    # MVC
    vista_home = VistaHome()
    controller_home = ControllerHome(vista_home)
    from backend.high_level.personale.dipendente import Dipendente
    controller_home = ControllerHomeAmministrazione(VistaHomeAmministrazione(), None,
                                                    Dipendente('a', 'b', datetime.datetime.now()))

    controller_home.connettiEventi()
    controller_home.showView()

    sys.exit(app.exec())

    # TODO
    # turno widget
    # duplicazione


if __name__ == '__main__':
    # TODO fare vista inserisciUbicazione
    startApp()
