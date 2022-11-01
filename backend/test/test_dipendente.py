from datetime import datetime
from unittest import TestCase

from backend.high_level.personale.amministratore import Amministratore
from backend.high_level.personale.amministrazione import Amministrazione
from backend.high_level.personale.credenziale import Credenziale
from backend.high_level.personale.dipendente import Dipendente
from backend.high_level.personale.segretario import Segretario
from backend.low_level.sicurezza.sha256_hashing import SHA256Hashing


class TestDipendete(TestCase):

    def setUp(self) -> None:
        self.username = 'Mario145'
        self.password = 'superPassword'
        self.hashing = SHA256Hashing()

        self.dipendente = Dipendente(
            nome="Mario",
            cognome="Rossi",
            dataNascita=datetime(2000, 1, 1),
            credenziale=Credenziale(
                username=self.username,
                password=self.password,
                hashing=self.hashing,
            )
        )
        self.amministrazione=Amministrazione(
            nome='amm1',
            piano=2,
            numPostazioni=5,
            descrizione='test',
        )
        self.amministratore=Amministratore(
            stipendio=2200,
            numPostazione=0,
        )
        self.segretario=Segretario(
            stipendio=1800,
            numPostazione=5,
            sportelloAssegnato=0,
        )

    def test_eta(self):
        self.assertEqual(
            first=self.dipendente.calcolaEta(),
            second=22
        )

    def test_credenziale(self):
        self.assertEqual(
            first=self.dipendente.credenziale.username,
            second=self.username
        )

        self.assertEqual(
            first=self.dipendente.credenziale.enc_password,
            second=self.hashing.hash(self.password)
        )

    def test_lavoro(self):
        with self.assertRaises(Exception) as context:
            self.dipendente.assumi(self.segretario, self.amministrazione)
            self.assertTrue('Non posso assumere un Segretario in una Amministrazione!' in context.exception.args)

        with self.assertRaises(Exception) as context:
            self.dipendente.licenzia('licenziamento per giusta causa')
            self.assertTrue('Non posso licenziare un dipendente che non ha un lavoro, prima devi assumerlo!' in context.exception.args)

        self.assertTrue(self.dipendente.assumi(self.amministratore,self.amministrazione))

