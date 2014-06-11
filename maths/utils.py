def cache(f):
    '''Decorator to cache values of functions.'''
    _cache = {}
    def _inner(*args, **kwargs):
        if args not in _cache:
            _cache[args] = f(*args, **kwargs)
        return _cache[args]
    return _inner
