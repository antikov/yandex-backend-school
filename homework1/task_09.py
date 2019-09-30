# Задание 9.
# Декораторы
# Написать аналог functools.wraps. Декоратор должен сохранять docstring декорируемой функции.

def myown_wraps(func):
    def wrapper(wrap):
        wrap.__doc__ = func.__doc__
        return wrap
    return wrapper

def dec(wrapped):
    @myown_wraps(wrapped)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        print('before')
        wrapped(*args, **kwargs)
        print('after')
    return wrapper

@dec
def f():
    """f docstring"""
    print('f()')

assert f.__doc__ == 'f docstring'
