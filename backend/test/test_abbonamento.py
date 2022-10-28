from datetime import datetime
from unittest import TestCase

from backend.high_level.clientela.abbonamento import Abbonamento
from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento


class TestAbbonamento(TestCase):

        def setUp(self) -> None:
                self.abbonamento_scaduto = Abbonamento(dataRilascio=datetime(2022, 1, 1), tipo= TipoAbbonamento.MENSILE)
                self.abbonamento_scaduto.pagato=True
                self.abbonamento_valido  = Abbonamento(dataRilascio=datetime(2022, 10, 16), tipo= TipoAbbonamento.ANNUALE)
                self.abbonamento_valido.pagato = True
                self.abbonamento_non_pagato = Abbonamento(dataRilascio=datetime(2022, 10, 16), tipo=TipoAbbonamento.ANNUALE)
                self.abbonamento_non_pagato.pagato = False

        def test_convalida(self):
                print(self.abbonamento_scaduto.isScaduto())
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

        # ============================================================================
        '''# Parte relativa al test ABBONAMENTO, da togliere nel programma terminato
        cliente = Cliente(
            nome='Mario',
            cognome='Rossi',
            codFis="RSSMRA01E07D546X",
            email="email@gmail.com",
            tel="3466787656",
        )'''


        # ============================================================================
        ''''# Parte relativa al test BIGLIETTO, da togliere nel programma terminato
        cliente= Cliente(
                nome='Ciccio',
                cognome='Bello',
                codFis = "codFis",
                email = "email",
                tel = "3355",
                #data_registrazione = datetime.now(),
        )

        biglietto= Biglietto(dataRilascio= datetime(2022, 9, 17))
        biglietto.qr_code.id='AAAAAAAAAA'
        cliente.biglietti.append(biglietto)
        self.model.visitatori.append(cliente)'''

    # ============================================================================