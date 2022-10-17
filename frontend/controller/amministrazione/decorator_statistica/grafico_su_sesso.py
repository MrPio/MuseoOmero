#######################################################
# 
# GraficoSuSesso.py
# Python implementation of the Class GraficoSuSesso
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5 import QtChart
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QColor
from PyQt5.QtWidgets import QVBoxLayout

from backend.high_level.clientela.enum.sesso import Sesso
from backend.high_level.museo import Museo
from frontend.controller.amministrazione.decorator_statistica.grafico import Grafico
from frontend.controller.amministrazione.decorator_statistica.statistica import Statistica


class GraficoSuSesso(Grafico):
    def __init__(self, controller: 'ControllerVistaStatistiche', wrappee: Statistica):
        super().__init__(controller, wrappee)

    def calcola(self) -> None:
        super().calcola()

        mese = self.controller.mese_selezionato
        if mese is None:
            return

        def __onSeriesClicked(slice: QPieSlice):
            slice.setExploded(exploded=not slice.isExploded())
            slice.setLabelVisible(visible=not slice.isLabelVisible())

        conteggio = {
            Sesso.MASCHIO: 0,
            Sesso.FEMMINA: 0,
            Sesso.NON_SPECIFICATO: 0,
        }
        for visitatore in Museo.getInstance().visitatori:
            for biglietto in visitatore.biglietti:
                for data in biglietto.date_convalida:
                    if data.year == mese.year and data.month == mese.month:
                        conteggio[visitatore.sesso] += 1

        self.series = QPieSeries()

        for sesso, num in conteggio.items():
            self.series.append(sesso.name, num)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.legend().setAlignment(Qt.AlignTop)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTheme(QChart.ChartThemeLight)
        self.series.clicked.connect(__onSeriesClicked)
        self.series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
        colors=['#fee84c','#ff5965','#39618d']
        for slice,color in zip(self.series.slices(),colors):
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
            slice.setLabelFont(QFont('Lato', 14, QFont.Light))
            slice.setBrush(QColor(color))

        self.chart.legend().markers(self.series)[0].setLabel("♂  ")
        self.chart.legend().markers(self.series)[1].setLabel("♀  ")
        self.chart.legend().markers(self.series)[2].setLabel("⚥  ")
        self.chart.legend().setFont(QFont('Lato', 26, QFont.Light))
        self.chart.legend().detachFromChart()
        self.chart.legend().setMinimumWidth(300)
        self.chart.legend().setX(97)
        self.chart.legend().setY(-20)
        self.chart.legend().update()
        self.chart.setTitle('Grafico su genere')
        self.chart.setTitleFont(QFont('Lato', 14, QFont.Light))

        self.chart.setContentsMargins(-50, 2, -50, -50)
        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self._chart_view)

        self.controller.charts_layout.append(self.layout)
