import ctypes
import sys
from pathlib import Path

lib_path = Path(__file__).parent

if sys.platform.startswith("linux"):
    libfile = lib_path / "libmystr.so"
elif sys.platform == "darwin":
    libfile = lib_path / "libmystr.dylib"
else:
    libfile = lib_path / "mystr.dll"

lib = ctypes.CDLL(str(libfile))

lib.to_upper.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
lib.to_upper.restype = None

input_s = b"Hello World!"
out = ctypes.create_string_buffer(256)
lib.to_upper(input_s, out, ctypes.sizeof(out))

print(out.value.decode())
