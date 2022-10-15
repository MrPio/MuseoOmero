from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi


class MyWidget(QWidget):
    def __init__(self, uiFile, parent):
        # Se non funziona lo scroll di un qualsiasi scroll area + layout, devi stattare MIN/MAX
        # sulla form contenente il widget!!
        super().__init__(parent)
        loadUi(uiFile, self)
        for bigButton in list(filter(lambda el: 'icon' in el.lower(), self.__dict__.keys())):
            getattr(self, bigButton).setMargin(10)
