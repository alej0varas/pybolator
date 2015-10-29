from random import randint
from time import sleep
import sys


LEDS_AMOUNT = 4
SWITCHES_AMOUNT = 1


class Accel:

    def x(self):
        sys.stderr.write("ACCEL:\n")
        sys.stderr.write("\tx\n")

        return randint(0, 10)

    def y(self):
        sys.stderr.write("ACCEL:\n")
        sys.stderr.write("\ty\n")

        return randint(0, 10)

accel = Accel()


def Accel():
    return accel


class _LED:

    state = False
    intensity_value = 0

    def __init__(self, led):
        self.led = led

    def on(self):
        self.state = True
        sys.stderr.write("LED %s:\n" % self.led)
        sys.stderr.write("\t on\n")

    def off(self):
        self.state = False
        sys.stderr.write("LED %s:\n" % self.led)
        sys.stderr.write("\t off\n")

    def toggle(self):
        if self.state:
            return self.off()
        return self.on()

    def intensity(self, value):
        self.intensity_value = value
        sys.stderr.write("LED %s:\n" % self.led)
        sys.stderr.write("\t intensity %s\n" % self.intensity_value)


leds = [_LED(i) for i in range(LEDS_AMOUNT)]


def LED(number):
    return leds[number - 1]


class _Switch:

    status = False
    callable = None

    def __call__(self):
        sys.stderr.write("SWITCH:\n")
        sys.stderr.write("\t call > %s\n" % self.status)

        return self.status

    def callback(self, callable):
        self.callable = callable
        sys.stderr.write("SWITCH:\n")
        sys.stderr.write("\t callback %s\n" % self.callable)

    def _down(self):
        self.status = True
        self.callable()

    def _up(self):
        self.status = False


switch = _Switch()


def Switch():
    return switch




def delay(miliseconds):
    sys.stderr.write("PYB:\n")
    sys.stderr.write("\tdelay %s\n" % miliseconds)
    sleep(miliseconds / 1000)


def _run_code():
    def target():
        import os
        MAIN_FILENAME = os.environ.get("PYBOLATOR_MAIN", "main.py")
        obj = compile(open(MAIN_FILENAME).read(), MAIN_FILENAME, 'exec')
        exec(obj, globals())

    import threading
    thread = threading.Thread(target=target)
    thread.start()
