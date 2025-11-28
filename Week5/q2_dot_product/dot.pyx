# dot.pyx

def dot_product(list a, list b):
    cdef int i
    cdef int n = len(a)
    cdef double result = 0

    for i in range(n):
        result += a[i] * b[i]

    return result
