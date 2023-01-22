import unittest
from ibm_cloud_sdk_core import ApiException
from .translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        with self.assertRaises(ApiException):
            english_to_french("")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        with self.assertRaises(ApiException):
            french_to_english("")
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()
