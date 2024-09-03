from typing import List
import threading
import random
import time


class Screwdriver:
    def __init__(self, doctor):
        self.doctor = doctor
        self.lock = threading.Lock()

    def take(self, timeout=-1):
        return self.lock.acquire(timeout=timeout)

    def drop(self):
        self.lock.release()


class Doctor:
    def __init__(self, number, screwdrivers):
        self.number = number
        self.left_screwdriver = screwdrivers[number - 9]
        self.right_screwdriver = screwdrivers[number - 10]

    def run(self):
        while True:
            time.sleep(random.randint(5, 10))
            self.take_screwdrivers()
            print(f"Doctor {self.number}: BLAST!")
            self.drop_screwdrivers()

    def take_screwdrivers(self):
        while True:
            if not self.right_screwdriver.take(0.1):
                continue
            if self.left_screwdriver.take(0.1):
                break
            else:
                self.right_screwdriver.drop()

    def drop_screwdrivers(self):
        self.left_screwdriver.drop()
        self.right_screwdriver.drop()


if __name__ == "__main__":
    screwdrivers = [Screwdriver(i) for i in range(9, 14)]
    doctors = [Doctor(i, screwdrivers) for i in range(9, 14)]

    for doctor in doctors:
        threading.Thread(target=doctor.run).start()
