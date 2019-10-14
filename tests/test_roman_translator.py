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

    def test_translate_when_asking_for_2(self):
        # Given
        given = "2"
        expected = "II"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)

    def test_translate_when_asking_for_3(self):
        # Given
        given = "3"
        expected = "III"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)
    
    def test_translate_when_asking_for_5(self):
        # Given
        given = "5"
        expected = "V"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)
    
    def test_translate_when_asking_for_7(self):
        # Given
        given = "7"
        expected = "VII"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)
    
    def test_translate_when_asking_for_10(self):
        # Given
        given = "10"
        expected = "X"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)
    
    def test_translate_when_asking_for_16(self):
        # Given
        given = "16"
        expected = "XVI"
        translator = RomanTranslator()
        # When
        result = translator.translate(given)
        # Then
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()