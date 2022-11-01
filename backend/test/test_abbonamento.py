from datetime import datetime
from unittest import TestCase

from backend.high_level.clientela.abbonamento import Abbonamento
from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento


class TestAbbonamento(TestCase):

    def setUp(self) -> None:
        self.abbonamento_scaduto = Abbonamento(
            dataRilascio=datetime(2022, 1, 1),
            tipo=TipoAbbonamento.MENSILE
        )
        self.abbonamento_scaduto.pagato = True
        self.abbonamento_valido = Abbonamento(
            dataRilascio=datetime(2022, 10, 16),
            tipo=TipoAbbonamento.ANNUALE
        )
        self.abbonamento_valido.pagato = True
        self.abbonamento_non_pagato = Abbonamento(
            dataRilascio=datetime(2022, 10, 16),
            tipo=TipoAbbonamento.ANNUALE
        )
        self.abbonamento_non_pagato.pagato = False

    def test_convalida(self):
        self.assertEqual(
            first=self.abbonamento_scaduto.convalida(),
            second=False
        )
        self.assertEqual(
            first=self.abbonamento_valido.convalida(),
            second=True
        )
        self.assertEqual(
            first=self.abbonamento_non_pagato.convalida(),
            second=False
        )
