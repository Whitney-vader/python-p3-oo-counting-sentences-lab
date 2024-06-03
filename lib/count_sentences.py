class MyString:
    def __init__(self, value = ""):
        self._value = value
    def get_value(self):
        return self._value
    def set_value(self, strings):
        if (type(strings) == str):
           self._value = strings 
        else:            
            print("The value must be a string.")
    value = property(get_value, set_value)
    def is_sentence(self):
        if (self._value[-1] == "."):
            return True
        else:
            return False
    def is_question(self):
        if (self._value[-1] == "?"):
            return True
        else:
            return False
    def is_exclamation(self):
        if (self._value[-1] == "!"):
            return True
        else:
            return False
    def count_sentences(self):
        value = self.value
        for mark in ["!","?"]:
            value = value.replace(mark, ".")
        words = [i for i in value.split(".") if i]
        return len(words)