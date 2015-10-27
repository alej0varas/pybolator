from random import randint
from time import sleep

app = None

LEDS_AMOUNT = 4
SWITCHES_AMOUNT = 1


class Accel:

    def x(self):
        print("ACCEL:")
        print("\tx")

        return randint(0, 10)

    def y(self):
        print("ACCEL:")
        print("\ty")

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
        app.leds[self.led].update()
        print("LED %s:" % self.led)
        print("\t on")

    def off(self):
        self.state = False
        app.leds[self.led].update()
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


leds = [_LED(i) for i in range(LEDS_AMOUNT)]


def LED(number):
    return leds[number - 1]


class _Switch:

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


switch = _Switch()


def Switch():
    return switch


def delay(miliseconds):
    print("PYB:")
    print("\tdelay %s" % miliseconds)

    app.delay()

    sleep(miliseconds / 1000)
