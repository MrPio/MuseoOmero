import ctypes
import datetime
import random
import string
import sys

from PyQt5.QtWidgets import QApplication

from backend.high_level.clientela.enum.tariffa import Tariffa
from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento
from backend.high_level.gestione_interna.opera import Opera
from frontend.controller.amministrazione.controller_gestione_dipendenti import ControllerGestioneDipendenti
from frontend.controller.amministrazione.controller_home_amministrazione import ControllerHomeAmministrazione
from frontend.controller.controller_home import ControllerHome
from frontend.controller.reception.controller_acquisto_biglietto import ControllerAcquistoBiglietto
from frontend.controller.reception.controller_home_reception import ControllerHomeReception
from frontend.controller.reception.controller_ricerca_opera import ControllerRicercaOpera
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.amministrazione.vista_home_amministrazione import VistaHomeAmministrazione
from frontend.view.reception.vista_acquisto_biglietto import VistaAcquistoBiglietto
from frontend.view.reception.vista_home_reception import VistaHomeReception
from frontend.view.reception.vista_ricerca_opera import VistaRicercaOpera
from frontend.view.vista_home import VistaHome


# for name, value in locals().items():
#     setattr(self,name, value)
def popolaMuseo():
    from backend.high_level.museo import Museo
    from backend.high_level.clientela.biglietto import Biglietto
    from backend.high_level.clientela.enum.sesso import Sesso
    from backend.high_level.clientela.visitatore import Visitatore
    from backend.high_level.clientela.cliente import Cliente
    from backend.high_level.clientela.abbonamento import Abbonamento
    from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
    from backend.high_level.gestione_interna.enum.periodo_storico import PeriodoStorico

    museo = Museo.getInstance()

    # creo i biglietti per i visitatori e per i clienti
    biglietti = [Biglietto() for _ in range(500)]
    for biglietto in biglietti:
        biglietto.date_convalida.append(
            datetime.datetime.strptime(str(random.randrange(1, 28)) + '/10/2022', '%d/%m/%Y'))
    # aggiungo i visitatori
    visitatori = []
    for i in range(random.randrange(50, 150)):
        visitatori.append(
            Visitatore(
                provenienza=random.choices(['ITA', 'FRA', 'GER', 'ING', 'AMERICA'], [4, 1, 1, 1, 2])[0],
                dataNascita=datetime.datetime.strptime('10/02/' + str(random.randrange(1920, 2020)), '%d/%m/%Y'),
                sesso=random.choices([Sesso.MASCHIO, Sesso.FEMMINA, Sesso.NON_SPECIFICATO], [3, 3, 1])[0],
                biglietti=[biglietti[i]],
            )
        )
    # aggiungo i biglietti ai visitatori
    for visitatore in visitatori:
        visitatore.biglietti.extend(
            [Biglietto(
                reparto=random.choice([e for e in RepartoMuseo]),
                tariffa=random.choice([e for e in Tariffa]),
                dataRilascio=datetime.datetime.strptime(
                    str(random.randrange(1, 28)) + '/' + str(random.randrange(1, 13)) + '/2022', '%d/%m/%Y'),
                turno=random.choice([None, *museo.turni_guida]),
            ) for _ in range(random.randrange(1, 50))]
        )

    museo.visitatori.extend(visitatori)

    # aggiungo i clienti
    clienti = []
    for i in range(random.randrange(30, 80)):
        # aggiungo gli abbonamenti ai clienti
        abbonamenti = [
            Abbonamento(
                dataRilascio=datetime.datetime.strptime('15/' + str(random.randrange(1, 13)) + '/2022', '%d/%m/%Y'),
                tipo=random.choice([e for e in TipoAbbonamento])
            ) for _ in range(random.randrange(1, 3))]
        for abbonamento in abbonamenti:
            abbonamento.date_convalida.extend(
                [datetime.datetime.strptime(str(random.randrange(1, 28)) + '/' +
                                            str(random.randrange(1, 13)) + '/2022', '%d/%m/%Y') for _ in
                 range(random.randrange(5, 50))]
            )
            rinnovi = {
                datetime.datetime.strptime('10/' + str(random.randrange(1, 13)) + '/2022', '%d/%m/%Y'):
                    random.choice([e for e in TipoAbbonamento]) for _ in range(random.randrange(1, 10))
            }
            abbonamento.date_rinnovo = {**abbonamento.date_rinnovo, **rinnovi}

        clienti.append(
            Cliente(
                nome='pippo',
                cognome='baudo',
                codFis='AAA',
                prov=random.choices(['ITA', 'FRA', 'GER', 'ING', 'AMERICA'], [4, 1, 1, 1, 2])[0],
                nasc=datetime.datetime.strptime('10/02/' + str(random.randrange(1920, 2020)), '%d/%m/%Y'),
                sesso=random.choices([e for e in Sesso], [3, 3, 1, 0])[0],
                biglietti=[biglietti[i + 150]],
                abbonamenti=abbonamenti,
            )
        )
    museo.visitatori.extend(clienti)

    # aggiungo le opere
    opere = []
    for i in range(50):
        opera = Opera(
            autore=random.choice(['Picasso', 'Botticelli', 'DaVinci', 'Raffaello', 'Michelangelo', 'Dalì', 'Klimt']),
            titolo=''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
            descrizione='',
            immagine=None,
            costo=random.randrange(100, 5000),
            reparto=random.choice([e for e in RepartoMuseo]),
            periodo=random.choice([e for e in PeriodoStorico]),
        )
        rand_data = datetime.datetime.strptime('20/' + str(random.randrange(1, 13)) + '/2022', '%d/%m/%Y')
        rand = random.randrange(0, 3)
        if rand == 1:
            opera.data_vendita = rand_data
        elif rand == 2:
            opera.data_acquisto = rand_data
        opere.append(opera)

    museo.opere.extend(opere)
    museo.make_backup()


def startApp():
    # fix icona non visibile
    myappid = 'museum.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    # MVC
    vista_home = VistaHome()
    controller_home = ControllerHome(vista_home)
    from backend.high_level.personale.dipendente import Dipendente
    controller_home = ControllerHomeAmministrazione(VistaHomeAmministrazione(), None,
                                                    Dipendente('a', 'b', datetime.datetime.now()))

    controller_home.connettiEventi()
    controller_home.showView()

    sys.exit(app.exec())

    # TODO
    # turno widget
    # duplicazione


if __name__ == '__main__':
    # TODO fare vista inserisciUbicazione
    # popolaMuseo()
    startApp()
    # TODO finire di settare l-aspect ratio in widget opera e in vistaOpera
