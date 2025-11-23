# ctypes vs Extension Modules

- **ctypes**
  - Dynamic runtime loading of shared libraries (.so/.dll).
  - Good for calling simple C functions without building Python extensions.
  - Requires manual declaration of argument and return types in Python.
  - Cross-platform but slower due to runtime conversions.

- **Extension Modules (Python C API / setuptools)**
  - Write C/C++ code that uses Python/C API and compile into a Python module (.so/.pyd).
  - Faster and offers deep integration (new types, exceptions).
  - More boilerplate and build steps; better for performance-critical or complex bindings.

Conclusion: use ctypes for quick and simple C functions; use extension modules for speed and deep integration.
