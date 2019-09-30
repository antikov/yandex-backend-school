# Задание 4.
# Упражнение про метакласс
# Замени троеточие метаклассом, чтобы код выполнялся

class A:
    def f(self):
        return A

class Meta(type):
    def __new__(cls, name, bases, dct):
        for el, value in A.__dict__.items():
            if not el.startswith("__"):
                dct[el] = value
        return type(name, bases, dct)

class B(metaclass=Meta):
    pass


assert B().f() == A
