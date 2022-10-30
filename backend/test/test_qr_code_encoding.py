from unittest import TestCase

import cv2
import qrcode


class TestQRCodeEncoding(TestCase):

    def test_encode(self):
        img = qrcode.make('Ciao, questo è un QrCode di prova')
        img.save("junk\\test_QrCode_image\QrCode.png")

    def test_decode(self):
        image = cv2.imread("junk\\test_QrCode_image\QrCode.png")
        print(cv2.QRCodeDetector().detectAndDecode(image)[0])
