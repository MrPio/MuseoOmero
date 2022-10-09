import ctypes
import sys

import cv2
from PyQt5.QtWidgets import QApplication

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
    controller_home = ControllerHome(VistaHome())
    controller_home.connettiEventi()
    controller_home.showView()
    sys.exit(app.exec())


if __name__ == '__main__':
    startApp()
    # img = cv2.imread('qrcode.png')
    # val, _, _ = detector = cv2.QRCodeDetector().detectAndDecode(img)
    # print(val)

    # img = qrcode.make('Ragazzi ho scoperto che ursino invece la vede la tesina.')
    # img.save('qrcode.png')
    # print(QR().decode(filename='qrcode.png'))
    # print()
