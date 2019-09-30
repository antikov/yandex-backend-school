# Задание 4.
# Упражнение про метакласс
# Замени троеточие метаклассом, чтобы код выполнялся

class A:
    def f(self):
        return A

class Meta(type):
    def __init__(cls, name, bases, dct):
        super(Meta, cls).__init__(name, bases, dct)
        cls.f = A().f

class B(metaclass=Meta):
    pass

assert B().f() == A
