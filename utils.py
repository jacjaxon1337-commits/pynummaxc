from .core import X

def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    return a, b
