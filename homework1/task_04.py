class A:
    def f(self):
        return A

class Meta(type=A):
    pass

class B(metaclass=Meta):
    pass
assert B().f() == A
