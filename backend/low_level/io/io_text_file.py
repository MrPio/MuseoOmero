#######################################################
# 
# IOTextFile.py
# Python implementation of the Class IOTextFile
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import os

from backend.low_level.io.io_file import IOFile


class IOTextFile(IOFile):
    def salvaFile(self, content: str, path: str, filename: str) -> bool:
        """
        Viene salvato un file di testo nel percorso specificato creando
        ricorsivamente le cartelle necessarie se possibile.
        :param content: il contenuto del file
        :param path: il percorso dove scrivere il file
        :param filename: il nome con estensione del file
        :return: flag di successo
        """
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            return False

        with open(path + filename, 'w') as writer:
            writer.write(content)
        return True

    def leggiFile(self, path: str) -> str:
        """
        Viene letto un file di testo data la sua posizione.
        :param path: il percorso dove leggere il file
        :return: il contenuto del file o '' se non trovato
        """
        if not os.path.exists(path):
            return ''
        with open(path, 'r') as reader:
            return ''.join(line for line in reader.readlines())
