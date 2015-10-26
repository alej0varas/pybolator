__name__ = "pyb-mock"

from random import randint


def delay(miliseconds):
    print("PYB:")
    print("\tdelay %s" % miliseconds)

    import time
    time.sleep(miliseconds / 1000)


class Accel:

    def x(self):
        print("ACCEL:")
        print("\tx")

        return randint(0, 10)

    def y(self):
        print("ACCEL:")
        print("\ty")

        return randint(0, 10)


class LED:

    state = False
    intensity_value = 0

    def __init__(self, led):
        self.led = led

    def on(self):
        self.state = True
        print("LED %s:" % self.led)
        print("\t on")

    def off(self):
        self.state = False
        print("LED %s:" % self.led)
        print("\t off")

    def toggle(self):
        if self.state:
            return self.off()
        return self.on()

    def intensity(self, value):
        self.intensity_value = value
        print("LED %s:" % self.led)
        print("\t intensity %s" % self.intensity_value)


class Switch:

    status = False
    callable = None

    def __call__(self):
        print("SWITCH:")
        print("\t call > %s" % self.status)

        return self.status

    def callback(self, callable):
        self.callable = callable
        print("SWITCH:")
        print("\t callback %s" % self.callable)

    def _down(self):
        self.status = True
        self.callable()

    def _up(self):
        self.status = False
