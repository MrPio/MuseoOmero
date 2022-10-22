#######################################################
# 
# ControllerGestioneDonazioni.py
# Python implementation of the Class ControllerGestioneDonazioni
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from backend.high_level.museo import Museo
from backend.high_level.personale.segreteria import Segreteria
from frontend.controller.controller import Controller
from frontend.controller.segreteria.widget.controller_widget_richiesta_donazione import \
    ControllerWidgetRichiestaDonazione
from frontend.ui.location import UI_DIR
from frontend.view.segreteria.vista_gestione_donazioni import VistaGestioneDonazioni
from frontend.view.segreteria.widget.widget_richiesta_donazione import WidgetRichiestaDonazione


class ControllerGestioneDonazioni(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaGestioneDonazioni, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaGestioneDonazioni = view
        self.previous = previous
        self.model = model

        # Museo.getInstance().posti_lavoro.append(
        #     Segreteria(
        #         nome='test999',
        #         piano=1,
        #         numPostazioni=1,
        #         sportelli=2,
        #         telFisso='000+',
        #         descr='',
        #         richieste_donazione=[
        #             RichiestaDonazione(
        #                 opera=Museo.getInstance().opere[-1],
        #                 ubicazioneProvvisoria=Ubicazione(),
        #                 notification=SMSMessage('999+'),
        #             )
        #         ]
        #     )
        # )
        self.previous.disableView()
        self.connettiEventi()
        self.initializeUi()
        self.showView()

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()

    def __renderizzaRichiestaDonazioni(self) -> list[ControllerWidgetRichiestaDonazione]:
        result = []

        for posto_lavoro in self.model.posti_lavoro:
            if isinstance(posto_lavoro, Segreteria):
                for richiesta_donazione in posto_lavoro.richieste_donazione:
                    if richiesta_donazione.presa_in_carico:
                        continue
                    result.append(ControllerWidgetRichiestaDonazione(
                        view=WidgetRichiestaDonazione(self.view.getDonazioniListView()),
                        parent=self,
                        model=richiesta_donazione,
                    ))
        return result

    def initializeUi(self) -> None:
        self.richieste_donazioni = self.__renderizzaRichiestaDonazioni()

        # rimuovo tutti i widget
        for i in reversed(range(self.view.getVerticalLayout().count())):
            self.view.getVerticalLayout().itemAt(i).widget().setParent(None)

        if len(self.richieste_donazioni) == 0:
            label = QLabel('Niente da mostrate qui.', self.view.getDonazioniListView())
            label.setStyleSheet(open(UI_DIR + '/css/textLabel.css', 'r').read())
            label.setAlignment(Qt.AlignCenter)
            self.view.getVerticalLayout().addWidget(label)
        for controller in self.richieste_donazioni:
            self.view.getVerticalLayout().addWidget(controller.view)
