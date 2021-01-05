from threading import Thread
import threading


def print_numbers():
    for n in range(100, 111):
        print(n)


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(1, 11):
            print(f"{self.name} {i}")


t1 = PrintThread("First")
t2 = PrintThread("Second")
t3 = Thread(target=print_numbers)
t1.start()
t2.start()
t3.start()
print(threading.active_count())
