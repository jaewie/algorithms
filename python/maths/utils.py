def cache(f):
    '''Decorator to cache values of functions.'''
    _cache = {}

    def _inner(*args, **kwargs):
        if args not in _cache:
            _cache[args] = f(*args, **kwargs)
        return _cache[args]
    return _inner


def change_type(_type):
    '''Decorator factory to change type of a function.'''

    def type_decorator(f):
        initial_call = True

        def wrapper(*args, **kwargs):
            nonlocal initial_call
            if initial_call:
                initial_call = False
                return_value = _type(f(*args, **kwargs))
                initial_call = True
                return return_value
            else:
                return f(*args, **kwargs)
        return wrapper
    return type_decorator
