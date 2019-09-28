class Magic(int):
    def __init__(self, value=0):
        self._value = value
        print('init', self._value)

    def __pos__(self):
        print('pos', self._value)
        self._value += 1
        return self._value
    
    def __neg__(self):
        print('neg', self._value)
        self._value -= 1
        print(self._value)
        return self._value

i = Magic()
assert i == 0
assert ++i == 1
assert ++i == 2
assert --i == 1
assert --i == 0
assert --i == -1
