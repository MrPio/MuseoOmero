import os
from unittest import TestCase

from backend.low_level.network.drop_box_api import DropBoxAPI


class TestDropBoxAPI(TestCase):
    def setUp(self) -> None:
        self.dropbox_api = DropBoxAPI()
        self.path = 'junk/TestDropBoxAPI/'
        self.filename = 'OneOfMyTurns-PinkFloyd.flac'
        self.filename_downloaded = 'OneOfMyTurns-PinkFloyd [downloaded].flac'

    def test_download(self):
        if os.path.exists(self.path + self.filename_downloaded):
            os.remove(self.path + self.filename_downloaded)
        self.assertTrue(
            expr=self.dropbox_api.download(
                cloudPath=DropBoxAPI.cloud_root_dir + self.filename,
                localPath=self.path + self.filename_downloaded
            ),
        )
        self.assertTrue(os.path.exists(self.path + self.filename_downloaded))

    def test_upload(self):
        self.assertTrue(
            expr=self.dropbox_api.upload(
                path=self.path,
                filename=self.filename,
            ),
        )

    def test_list_file(self):
        print(
            'files list->',
            self.dropbox_api.listFile(
                cloudDirectory=DropBoxAPI.cloud_root_dir,
            ),
        )

    def test_list_file2(self):
        print(self.dropbox_api.listFile(DropBoxAPI.cloud_root_dir + 'backups/'))

    def test_delete_file(self):
        self.assertTrue(
            self.dropbox_api.deleteFile(
                DropBoxAPI.cloud_root_dir + 'backups/test',
            )
        )
