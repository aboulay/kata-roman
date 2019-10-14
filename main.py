import sys

from translator.roman import RomanTranslator 

def main():
    roman_translator = RomanTranslator()
    roman_translator.translate(sys.argv[1])

if __name__ == "__main__":
    main()