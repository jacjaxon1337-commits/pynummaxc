import ctypes
import os

_lib_path = os.path.join(os.path.dirname(__file__), "_pynummax_c.so")

try:
    _lib = ctypes.CDLL(_lib_path)
except Exception:
    raise OSError(
        "pynummax/_pynummax_c.so: undefined symbol: PyModule_Create2_ABI3. "
        "Fatal C-level initialization failed."
    )

def X(a: int, b: int) -> int:
    return _lib.sys_core_exec(a, b)
