class RomanTranslator(object):

    def translate(self, value):
      int_value = int(value)
      roman_value = ""
      
      while int_value != 0:
        if (int(int_value / 10) > 0):
          roman_value += "X"
          int_value -= 10
        elif (int(int_value / 5) > 0):
          roman_value += "V"
          int_value -= 5
        else:
          roman_value += "I"
          int_value -= 1
      return roman_value