from unittest import TestCase

from backend.low_level.sicurezza.hashing import Hashing
from backend.low_level.sicurezza.sha256_hashing import SHA256Hashing


class TestSHA256Hashing(TestCase):
    def setUp(self) -> None:
        self.hashing:Hashing = SHA256Hashing()
        self.plain = 'password_super_segreta'

    def test_hash(self):
        self.assertEqual(
            first=self.hashing.hash(self.plain),
            second='4c2b929779ccab43c5b52fb6aaa14258e05ca3dd7efaaf6113244c6fd79f7161',
        )
