# Задание 4.
# Упражнение про метакласс
# Замени троеточие метаклассом, чтобы код выполнялся

class A:
    def f(self):
        return A

class Meta(type, A):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        return x
class B(metaclass=Meta):
    pass
print(A().f())
print(A)
print(B())
print(B().f())
assert B().f() == A
