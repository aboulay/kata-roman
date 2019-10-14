import unittest

from translator.roman import RomanTranslator

class TestRomanTranslator(unittest.TestCase):

    def test_translate_when_asking_for_1(self):
        # Given
        given = "1"
        expected = "I"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()