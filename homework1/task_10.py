# Задание 10.
# Декораторы, context manager, генераторы
# Написать аналог contextlib.contextmanager.

class context_manager_decorator:
    def __init__(self, func, args, kwargs):
        self.func = func(*args, **kwargs)

    def __enter__(self):
        return next(self.func)
    
    def __exit__(self, a, b, c):
        pass

def my_own_context_manager_decorator(func):
    def wrapper(*args, **kwargs):
        return context_manager_decorator(func, args, kwargs)
    return wrapper

@my_own_context_manager_decorator
def example_context_manager_func(arg1, arg2):
    try:
        print(f'enter {arg1} {arg2}')
        mananged_resource_result = arg1 + arg2
        yield mananged_resource_result
    finally:
        print('exit')

with example_context_manager_func('arg1', 'arg2') as managed_resource:
    print(managed_resource)
