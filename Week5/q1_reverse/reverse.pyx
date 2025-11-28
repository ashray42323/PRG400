# reverse.pyx

def reverse_string(str s):
    cdef int i
    cdef int n = len(s)

    # convert to writable array:
    cdef char[:] arr = bytearray(s, 'utf-8')

    # create output buffer
    cdef char[:] rev = bytearray(n)

    for i in range(n):
        rev[i] = arr[n - i - 1]

    return bytes(rev).decode('utf-8')
