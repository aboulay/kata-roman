#!/usr/bin/python3

import sys

from translator.roman import RomanTranslator 

def main():
    roman_translator = RomanTranslator()
    result = roman_translator.translate(sys.argv[1])
    print(result)

if __name__ == "__main__":
    main()