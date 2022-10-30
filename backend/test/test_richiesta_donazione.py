from unittest import TestCase

from backend.high_level.gestione_interna.opera import Opera
from backend.high_level.gestione_interna.ubicazione import Ubicazione
from backend.high_level.personale.richiesta_donazione import RichiestaDonazione
from backend.low_level.network.email_message import EmailMessage


class TestRichiestaDonazione(TestCase):

    def setUp(self) -> None:
        self.ubicazione = Ubicazione()
        self.opera = Opera()
        self.richiesta = RichiestaDonazione(
            opera=self.opera,
            ubicazioneProvvisoria=self.ubicazione,
            notification=EmailMessage(''),
        )

    def test_convalida(self):
        self.assertEqual(
            first=self.richiesta.accettata,
            second=False
        )

        self.richiesta.accetta(self.ubicazione)
        self.assertEqual(
            first=self.richiesta.accettata,
            second=True
        )

        self.richiesta.rifiuta()
        self.assertEqual(
            first=self.richiesta.accettata,
            second=False
        )
