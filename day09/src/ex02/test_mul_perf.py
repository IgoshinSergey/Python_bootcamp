from itertools import tee
import time
from matrix import mul as cython_mul


def python_mul(a, b):
    b_iter = tee(zip(*b), len(a))
    return [
        [
            sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
            for col_b in b_iter[i]
        ] for i, row_a in enumerate(a)
    ]


x = [
    [1, 2, 3.1],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
y = [
    [1, 2],
    [1, 2],
    [3, 4],
]

m1 = [
    [i for i in range(100)] for i in range(100)
]
m2 = [
    [i for i in range(100)] for i in range(100)
]


def main():
    time1_start = time.time()
    res1 = python_mul(m1, m2)
    time1_end = time.time()
    print(f"python_mul: {time1_end - time1_start} s")
    # print(f"{res1}")

    time2_start = time.time()
    res2 = cython_mul(m1, m2)
    time2_end = time.time()
    print(f"cython_mul: {time2_end - time2_start} s")
    # print(f"{res2}")
    print(f"{(time1_end - time1_start) / (time2_end - time2_start):.2f}")


if __name__ == "__main__":
    main()
