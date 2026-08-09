import ctypes
import os

_lib_path = os.path.join(os.path.dirname(__file__), "_pynummax_c.so")
_lib = ctypes.CDLL(_lib_path)

def X(a: int, b: int) -> int:
    return _lib.sys_core_exec(a, b)
