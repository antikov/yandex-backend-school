# Задание 7.
# Инкремент/декремент в Python
# Замени pass, чтобы код работал

class Magic(int):
    def __init__(self):
        self._value = 0

    def __pos__(self):
        self._value += 1
        return self._value
    
    def __neg__(self):
        self._value -= 1
        return -self._value


i = Magic()
assert i == 0
assert ++i == 1
assert ++i == 2
assert --i == 1
assert --i == 0
assert --i == -1
