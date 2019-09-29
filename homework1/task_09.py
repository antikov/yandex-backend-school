# Задание 9.
# Декораторы
# Написать аналог functools.wraps. Декоратор должен сохранять docstring декорируемой функции.

from functools import wraps
def myown_wraps(func):
    
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        func(*args, **kwargs)
    print(wrapper.__doc__)
    print(func.__doc__)
    wrapper.__doc__ = func.__doc__
    return wrapper

def dec(wrapped):
    @myown_wraps(wrapped)
    #@wraps(wrapped)
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

print(f.__name__)
print(f.__doc__)
assert f.__doc__ == 'f docstring'
