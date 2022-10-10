from unittest import TestCase

from backend.low_level.io.io_text_file import IOTextFile


class TestIOTextFile(TestCase):
    def setUp(self) -> None:
        self.io_text_file = IOTextFile()
        self.content = 'file di test'
        self.path = 'junk/TestIOTextFile/'
        self.filename = 'test.pickle'

    def test_salva_file(self):
        self.assertTrue(
            expr=self.io_text_file.salvaFile(
                content=self.content,
                path=self.path,
                filename=self.filename,
            )
        )

    def test_leggi_file(self):
        self.assertEqual(
            first=self.io_text_file.leggiFile(
                path=self.path + self.filename,
            ),
            second=self.content,
        )
