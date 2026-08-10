from .utils import validate_inputs

def X(a: int, b: int) -> int:
    a, b = validate_inputs(a, b)
    return a + b
