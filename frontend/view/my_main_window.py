import os

import winotify
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from frontend.ui.location import UI_DIR

from frontend import my_res

class MyMainWindow(QMainWindow):
    def __init__(self, uiFile):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        loadUi(uiFile, self)
        # a quanto pare questo trucchetto richiede la versione 5 di pyqt
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QtGui.QIcon(UI_DIR + '/ico/museum_white.ico'))
        if hasattr(self, 'exitButton'):
            self.exitButton.clicked.connect(self.save_and_exit)
            self.maximizeButton.clicked.connect(self.maximize)
            self.reduceButton.clicked.connect(self.showMinimized)

        self.maxHeight = self.height()

        # ATTENZIONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # dopo tanti try&error ho scoperto che gli errori di rendering sono dovuti
        # alle seguenti cose:
        # • la superclasse DEVE essere la stessa classe dell'elemento alla radice del .ui
        # • il CSS nell'elemento radice CAUSA PROBLEMI!
        #   PERSINO COMMENTARLO NON RISOLVE, DEVE ESSERE PROPRIO TOLTO!
        #   Lo rimettiamo poi nel file qui sotto.
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.setStyleSheet(open(UI_DIR + '/css/main.css', 'r').read())

        # poiché si perdono i margini, li setto manualmente
        for bigButton in list(filter(lambda el: 'bigbutton' in el.lower(), self.__dict__.keys())):
            getattr(self, bigButton).setMargin(17)

        for checkBox in list(filter(lambda el: 'checkbox' in el.lower(), self.__dict__.keys())):
            setattr(self, checkBox + 'Status', False)
            getattr(self, checkBox).clicked.connect(self.checkBoxClicked)

        # self.debugLabel = QLabel('Modalità di debug attivata', self)
        # self.debugLabel.setStyleSheet(open(UI_DIR + '/css/debugLabel.css', 'r').read())
        # self.debugLabel.setGeometry(30,10,380,31)
        # self.debugLabel.setVisible(False)

    def go_debug_mode(self,mode=True):
        if mode:
            self.titoloLabelBackup=self.titoloLabel.text()
            self.titoloLabel.setText('Modalità di debug attivata')
            self.setStyleSheet(open(UI_DIR + '/css/main_shift_on.css', 'r').read())
            for element in self.__dict__.values():
                if isinstance(element,QLabel):
                    element.setStyleSheet(element.styleSheet().replace('rgb(104, 194, 253)','#fee84c')
                                          .replace('#1684FC','#F5CA48'))
        else:
            self.titoloLabel.setText(self.titoloLabelBackup)
            self.setStyleSheet(open(UI_DIR + '/css/main.css', 'r').read())
            for element in self.__dict__.values():
                if isinstance(element,QLabel):
                    element.setStyleSheet(element.styleSheet().replace('#fee84c','rgb(104, 194, 253)')
                                          .replace('#F5CA48','#1684FC'))


    def checkBoxClicked(self):
        objName = self.sender().objectName()
        if not getattr(self, objName + 'Status'):
            setattr(self, objName + 'Status', True)
            getattr(self, objName).setStyleSheet(open(UI_DIR + '/css/checkBoxOn.css', 'r').read())
        else:
            setattr(self, objName + 'Status', False)
            getattr(self, objName).setStyleSheet(open(UI_DIR + '/css/checkBoxOff.css', 'r').read())

    def maximize(self):
        if self.height() > 48:
            self.setMinimumHeight(48)
            self.setMaximumHeight(48)
            self.titoloLabel.setGeometry(self.titoloLabel.geometry().x(), 9, self.geometry().width() - 130,
                                         self.titoloLabel.geometry().height())
        else:
            self.setMaximumHeight(self.maxHeight)
            self.setMinimumHeight(self.maxHeight)
            self.titoloLabel.setGeometry(self.titoloLabel.geometry().x(), 57, self.geometry().width() - 60,
                                         self.titoloLabel.geometry().height())



    def mousePressEvent(self, event):
        if event.pos().y() > 50:
            return
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True
        QApplication.setOverrideCursor(Qt.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.pressing = False
        QApplication.restoreOverrideCursor()

    def mouseMoveEvent(self, event):
        if 'pressing' in self.__dict__.keys() and self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                             self.mapToGlobal(self.movement).y(),
                             self.width(),
                             self.height())
            self.start = self.end

    def save_and_exit(self):
        def perform():
            # winotify.Notification(
            #     app_id='Museo Omero',
            #     title='Backup in corso',
            #     msg='Attendi, sto effettuando il backup del museo locale...',
            #     icon=UI_DIR + '/ico/museum_white.ico',
            #     duration='short',
            # ).show()
            # Museo.getInstance().make_backup()
            os._exit(1)

        from frontend.controller.controller_yes_no import ControllerYesNo
        from frontend.view.vista_yes_no import VistaYesNo
        self.next = ControllerYesNo(VistaYesNo(), None, perform,
                                    'Sicuro di voler uscire?\r\n(I progressi NON verranno salvati)')
        self.next.showView()
