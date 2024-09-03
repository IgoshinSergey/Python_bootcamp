import time
import ctypes


class Timespec(ctypes.Structure):
    _fields_ = [
        ("tv_sec", ctypes.c_longlong),
        ("tv_nsec", ctypes.c_longlong)
    ]


def monotonic() -> float:
    libc = ctypes.CDLL('libc.so.6')
    clock_gettime = libc.clock_gettime
    clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(Timespec)]
    clock_gettime.restype = ctypes.c_int
    timespec = Timespec()
    clock_gettime(1, ctypes.pointer(timespec))
    return timespec.tv_sec + timespec.tv_nsec * 1e-9


def main():
    print(f"{time.monotonic()=}")
    print(f"{monotonic()=}")


if __name__ == '__main__':
    main()
