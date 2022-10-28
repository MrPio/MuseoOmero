from datetime import datetime
from unittest import TestCase
from backend.high_level.personale.dipendente import Dipendente


class TestDipendete(TestCase):


        def setUp(self) -> None:
                self.dipendente = Dipendente(nome="Mario", cognome="Rossi", dataNascita= datetime(2000, 1, 1))

        def test_convalida(self):

                self.assertEqual(
                        first=self.dipendente.credenziale.username,
                        second="MarioRossi"
                )

                self.assertEqual(
                        first=self.dipendente.calcolaEta(),
                        second=22
                )

