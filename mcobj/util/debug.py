def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"DEBUG INFO (function: {func.__name__}): returned {result}")
        return result
    return wrapper