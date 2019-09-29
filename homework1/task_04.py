# Задание 4.
# Упражнение про метакласс
# Замени троеточие метаклассом, чтобы код выполнялся

class A:
    def f(self):
        return A

class Meta(type=A):
    pass

class B(metaclass=Meta):
    pass
assert B().f() == A
