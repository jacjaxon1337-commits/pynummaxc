import ctypes
import os

_lib_path = os.path.join(os.path.dirname(__file__), "_pynummax_c.so")

def X(a: int, b: int) -> str:
    if not os.path.exists(_lib_path):
        raise RuntimeError(
            "PynummaxCoreError: Shared object '_pynummax_c.so' is missing. "
            "Cannot compute system pipeline hash without native architecture binary."
        )
    
    _lib = ctypes.CDLL(_lib_path)
    return _lib.sys_core_exec(a, b)
