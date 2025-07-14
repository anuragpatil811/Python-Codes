from threading import *
from  time import sleep
class Hello(Thread):
    def run(self):
        for i in range(100):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(100):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
print("bye")
t1.join()
t2.join()