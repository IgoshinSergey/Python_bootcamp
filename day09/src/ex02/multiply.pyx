import cython

cpdef list mul(list m1, list m2):
    cdef int r1 = len(m1)
    cdef int c1 = len(m1[0])
    cdef int r2 = len(m2)
    cdef int c2 = len(m2[0])

    if c1 != r2:
        raise ArithmeticError

    cdef list res = [[0 for i in range(c2)] for j in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j] += (<int>m1[i][k] * <int>m2[k][j])

    return res
