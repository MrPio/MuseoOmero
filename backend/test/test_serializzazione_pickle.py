import datetime
from unittest import TestCase

from backend.high_level.clientela.biglietto import Biglietto
from backend.high_level.clientela.enum.tariffa import Tariffa
from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
from backend.low_level.io.serializzazione_pickle import SerializzazionePickle


class TestSerializzazionePickle(TestCase):

    def setUp(self) -> None:
        self.serializzatore_pickle = SerializzazionePickle()
        self.biglietto_test = Biglietto(
            dataRilascio=datetime.datetime.now(),
            reparto=RepartoMuseo.MOSTRA,
            tariffa=Tariffa.RIDOTTO,
        )
        self.path = 'junk/TestSerializzazionePickle/'
        self.filename = 'biglietto123.pickle'

    def test_serializza(self):
        self.assertTrue(
            expr=self.serializzatore_pickle.serializza(
                obj=self.biglietto_test,
                path=self.path,
                filename=self.filename,
            ),
        )

    def test_deserializza(self):
        self.assertEqual(
            first=self.biglietto_test.tariffa,
            second=self.serializzatore_pickle.deserializza(
                path=self.path + self.filename,
            ).tariffa,
        )
