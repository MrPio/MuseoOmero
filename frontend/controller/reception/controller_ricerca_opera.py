#######################################################
# 
# ControllerRicercaOpera.py
# Python implementation of the Class ControllerRicercaOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.controller.reception.strategy_ricerca_opera.strategy_ricerca_opera import StrategyRicercaOpera
from frontend.view.reception.vista_ricerca_opera import VistaRicercaOpera


class ControllerRicercaOpera(Controller):

    def __gotoPrevious(self) -> None:
        pass

    def __init__(self, view: VistaRicercaOpera, previous: Controller, model: Museo, strategy: StrategyRicercaOpera):
        super().__init__(view)

    def __onRicercaClicked(self) -> None:
        pass

    def __gotoVistaOpera(self) -> None:
        pass

    def __onOperaClicked(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def __renderizzaOpere(self) -> list[ControllerWidgetOpera]:
        tipo_ricerca = self.view.getTipoRicercaComboBox().currentText().lower()
        parametro_ricerca = self.view.getParametroRicercaLineEdit().text()
        matches = {
            'autore': lambda opera: parametro_ricerca.lower() in opera.autore.lower(),
            'nome': lambda opera: parametro_ricerca.lower() in opera.nome.lower(),
            'periodo': lambda opera: parametro_ricerca.lower() in opera.periodo.name.lower(),
            'tipo': lambda opera: parametro_ricerca.lower() in opera.composizione.tipo_opera.name.lower(),
        }
        opere_filtrate = filter(matches[tipo_ricerca], self.model.opere)
        result = []

        for opera in opere_filtrate:
            new_widget = WidgetOpera(self.scrollAreaWidgetContents)
            result.append(ControllerWidgetOpera(
                view=new_widget,
                model=opera,
                parent=self,
            ))
        return result

    def initializeUi(self) -> None:
        pass