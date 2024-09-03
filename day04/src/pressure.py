from random import randint
from time import sleep


def emil_get(step: int):
    pressure = 50
    while True:
        step = (yield pressure)
        if step >= 0:
            delta = randint(0, step)
        else:
            delta = randint(step, 0)
        pressure += delta

        if pressure > 100 or pressure < 0:
            raise ValueError("Pressure went beyond the limit of values")
        elif pressure > 90 or pressure < 10:
            yield pressure
            return


def valve():
    step = 50
    generator = emil_get(step)
    generator.send(None)
    while True:
        try:
            pressure = generator.send(step)
            print(pressure)
            if (pressure > 80 and step > 0) or (pressure < 20 and step < 0):
                step = -step
            sleep(0.5)
        except ValueError as value_error:
            print(str(value_error))
            return
        except StopIteration:
            return


def main():
    valve()


if __name__ == "__main__":
    main()
