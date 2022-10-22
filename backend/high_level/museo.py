#######################################################
# 
# Museo.py
# Python implementation of the Class Museo
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import os
from datetime import datetime

import winotify

from backend.high_level.clientela.visitatore import Visitatore
from backend.high_level.gestione_interna.mostra import Mostra
from backend.high_level.gestione_interna.opera import Opera
from backend.high_level.gestione_interna.turno_guida import TurnoGuida
from backend.high_level.personale.amministratore import Amministratore
from backend.high_level.personale.amministrazione import Amministrazione
from backend.high_level.personale.credenziale import Credenziale
from backend.high_level.personale.dipendente import Dipendente
from backend.high_level.personale.posto_lavoro import PostoLavoro
from backend.low_level.io.serializzatore import Serializzatore
from backend.low_level.io.serializzazione_pickle import SerializzazionePickle
from backend.low_level.network.cloud_storage import CloudStorage
from backend.low_level.network.drop_box_api import DropBoxAPI
from frontend.ui.location import UI_DIR


class Museo:
    MUSEO_DIR = os.path.dirname(os.path.abspath(__file__))
    __backup_path = MUSEO_DIR + '/backups/'
    __backup_folder = 'backups/'
    __key = object()
    __instance: 'Museo' = None
    __cloud_storage: CloudStorage = DropBoxAPI()
    __serializzatore: Serializzatore = SerializzazionePickle()

    def __init__(self, key) -> None:
        assert (key == Museo.__key), \
            "Per garantire la presenza di una sola istanza del classificatore Museo, utilizza il metodo Museo.getInstance"
        self.nome = 'Museo Omero'
        self.sito_web = 'https://www.museoomero.it/'
        self.data_fondazione = datetime(1993, 5, 29)
        self.indirizzo = 'Mole Vanvitelliana, Banchina Giovanni da Chio, 28, 60100 Ancona AN'
        self.telefono_fisso = '0712811935'
        self.email = 'info@museoomero.it'
        self.descrizione = "Il Museo tattile statale Omero di Ancona è uno dei pochi musei " \
                           "tattili al mondo. L'istituto fa conoscere l'arte attraverso il tatto," \
                           " dando ai visitatori la possibilità di vedere con le mani. Nato per" \
                           " promuovere l'integrazione delle persone con disabilità visiva è " \
                           "uno spazio accessibile a tutti."
        self.visitatori: list[Visitatore] = []
        self.dipendenti: list[Dipendente] = []
        self.posti_lavoro: list[PostoLavoro] = []
        self.mostre: list[Mostra] = []
        self.turni_guida: list[TurnoGuida] = []
        self.opere: list[Opera] = []

        self.dipendenti.append(
            Dipendente(
                nome='admin',
                cognome='admin',
                dataNascita=datetime.now(),
                email='admin@admin.admin',
                credenziale=Credenziale(
                    username='admin',
                    password='admin',
                ),
                lavoro=Amministratore(
                    stipendio=0,
                    numPostazione=0,
                    fondatore=True,
                ),
                autogenerato=True,
            )
        )

        self.posti_lavoro.append(
            Amministrazione(
                nome='Amministrazione',
                piano=0,
                numPostazioni=99,
                descrizione='autogenerata',
            )
        )

    @staticmethod
    def getInstance() -> 'Museo':

        """
        nel rispetto del pattern Singleton, questo metodo mi garanitisce l'univocità dell'istanza.
        Si cerca localmente l'oggetto, poi sul cloud se non lo si trova. Solo in ultima possibilità viene creato nuvo.
        :return: l'unica istanza di Museo
        """
        if not os.path.exists(Museo.__backup_path):
            os.makedirs(Museo.__backup_path)

        if Museo.__instance == None:
            last_backup = Museo.__get_last_backup()
            # if last_backup == '':
            #     Museo.__download_last_backups()
            #     last_backup = Museo.__get_last_backup()
            #     if last_backup != '':
            #         print('ho trovato un backup su cloud, download in corso...')

            if last_backup == '':
                print(  # 'non ho trovato né un backup locale, né un backup su '
                    'cloud --> creo una nuova istanza di Museo.')
                Museo.__instance = Museo(Museo.__key)
            else:
                print('ho trovato il seguente backup --> {}'.format(last_backup))
                Museo.__instance = Museo.__serializzatore.deserializza(Museo.__backup_path + last_backup)
        return Museo.__instance

    def login(self, username: str, password: str) -> Dipendente | None:
        for dipendente in self.dipendenti:
            if dipendente.autentifica(username, password):
                return dipendente
        return None

    @staticmethod
    def __newest_date(list: list[str], format: str = '%Y-%m-%d %H-%M-%S') -> str:
        """
        data una lista di date sotto forma di stringhe, mi ritorna la stringa della data più recente
        :param list: la lista di date sotto forma di stringhe
        :param format: il formato in cui vengono fornite le date, e con il quale viene formattata quella di ritorno
        :return: la data più recente o '' se lista vuota
        """
        dates = []
        for date in list:
            dates.append(datetime.strptime(date, format))
        dates.sort()
        return dates[-1].strftime(format) if len(dates) > 0 else ''

    @staticmethod
    def __get_last_backup() -> str:
        files = next(os.walk(Museo.__backup_path), (None, None, []))[2]
        newest = Museo.__newest_date([file.split('museo ')[1].split('.pickle')[0] for file in files])
        return 'museo ' + newest + '.pickle' if len(newest) > 0 else ''

    def elimina_backup(self, data: str) -> None:
        file = 'museo ' + data + '.pickle'
        if os.path.exists(Museo.__backup_path + file):
            os.remove(Museo.__backup_path + file)
        Museo.__cloud_storage.deleteFile(DropBoxAPI.cloud_root_dir + Museo.__backup_folder + file)

    def list_backups_local(self) -> {str, str}:
        def formatted_size(num, suffix="B") -> str:
            for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
                if abs(num) < 1024.0:
                    return f"{num:3.1f} {unit}{suffix}"
                num /= 1024.0
            return f"{num:.1f}Y{suffix}"

        files = next(os.walk(Museo.__backup_path), (None, None, []))[2]
        result = {}
        for file in files:
            result[file.split('museo ')[1].split('.pickle')[0]] = \
                formatted_size(os.path.getsize(Museo.__backup_path + file))
        return result

    def download_backup(self, data: str) -> None:
        file = 'museo ' + data + '.pickle'
        result = Museo.__cloud_storage.download(
            cloudPath=DropBoxAPI.cloud_root_dir + Museo.__backup_folder + file,
            localPath=Museo.__backup_path + file
        )
        if result:
            Museo.__instance = Museo.__serializzatore.deserializza(Museo.__backup_path + self.__get_last_backup())
            winotify.Notification(
                app_id='Museo Omero',
                title='Backup ripristinato',
                msg=f'Backup ripristinato correttamente! [{data}]',
                icon=UI_DIR + '/ico/museum_white.ico',
                duration='short',
            ).show()

    def upload_backup(self, data: str) -> None:
        file = 'museo ' + data + '.pickle'
        Museo.__cloud_storage.upload(
            path=Museo.__backup_path,
            filename=file,
            cloudFolder=Museo.__backup_folder
        )

    def list_backups_cloud(self) -> list[str]:
        files = Museo.__cloud_storage.listFile(DropBoxAPI.cloud_root_dir + Museo.__backup_folder)
        return [file.split('museo ')[1].split('.pickle')[0] for file in files]

    @staticmethod
    def __download_last_backups() -> None:
        """
        scarica il backup più recente se non già presente sul disco
        """
        files = Museo.__cloud_storage.listFile(DropBoxAPI.cloud_root_dir + Museo.__backup_folder)
        newest = Museo.__newest_date([file.split('museo ')[1].split('.pickle')[0] for file in files])
        file_to_download = 'museo ' + newest + '.pickle' if len(newest) > 0 else ''
        if file_to_download == '' or file_to_download in next(os.walk(Museo.__backup_path), (None, None, []))[2]:
            return
        path = Museo.__backup_folder + file_to_download
        Museo.__cloud_storage.download(DropBoxAPI.cloud_root_dir + path, Museo.__backup_path + file_to_download)

    def make_backup(self) -> None:
        local_path = Museo.__backup_path

        filename = 'museo ' + datetime.now().strftime(
            '%Y-%m-%d %H-%M-%S') + '.pickle'

        Museo.__serializzatore.serializza(self, local_path, filename)
        # Museo.__cloud_storage.upload(local_path, filename)
