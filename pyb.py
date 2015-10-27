__name__ = "pyb-mock"

import pyboard


delay = pyboard.delay


def Accel():
    return pyboard.Accel()


def Switch():
    return pyboard.Switch()


def LED(number):
    return pyboard.LED(number)
