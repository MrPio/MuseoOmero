import ctypes
import sys

from PyQt5.QtWidgets import QApplication

from frontend.controller.controller_home import ControllerHome
from frontend.ui.location import UI_DIR
from frontend.view.vista_home import VistaHome

# for name, value in locals().items():
#     setattr(self,name, value)


if __name__=='__main__':
    myappid = 'museum.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    # MVC
    controller_home=ControllerHome(VistaHome())
    controller_home.connettiEventi()
    controller_home.showView()
    sys.exit(app.exec())
