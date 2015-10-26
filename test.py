import pyb

# This code can be run on your pyboard without modifications

#######
# Led #
#######

# on-off
led = pyb.LED(1)
led.on()
pyb.LED(2).on()

led.off()


# delay
for i in range(10):
    led.toggle()
    pyb.delay(1000)


# fun in a real device
leds = [pyb.LED(i) for i in range(1,5)]
for l in leds:
    l.off()

n = 0
for i in range(10):
    n = (n + 1) % 4
    leds[n].toggle()
    pyb.delay(50)
for l in leds:
    l.off()


# intensity 
led = pyb.LED(4)
intensity = 0
for i in range(10):
    intensity = (intensity + 1) % 255
    led.intensity(intensity)
    pyb.delay(20)


##########
# Switch #
##########

sw = pyb.Switch()

# status
assert sw() == False

# callbacks
sw.callback(lambda:print('press!'))

# sw._down();sw._up()  # REMOVE

sw.callback(None)

def f():
   pyb.LED(1).toggle()

sw.callback(f)


#################
# Accelerometer #
#################

accel = pyb.Accel()


# x
accel.x()


accel = pyb.Accel()
light = pyb.LED(3)
SENSITIVITY = 3

for i in range(10):
    x = accel.x()
    if abs(x) > SENSITIVITY:
        light.on()
    else:
        light.off()

    pyb.delay(100)

# y
xlights = (pyb.LED(2), pyb.LED(3))
ylights = (pyb.LED(1), pyb.LED(4))

accel = pyb.Accel()
SENSITIVITY = 3

for i in range(10):
    x = accel.x()
    if x > SENSITIVITY:
        xlights[0].on()
        xlights[1].off()
    elif x < -SENSITIVITY:
        xlights[1].on()
        xlights[0].off()
    else:
        xlights[0].off()
        xlights[1].off()

    y = accel.y()
    if y > SENSITIVITY:
        ylights[0].on()
        ylights[1].off()
    elif y < -SENSITIVITY:
        ylights[1].on()
        ylights[0].off()
    else:
        ylights[0].off()
        ylights[1].off()

    pyb.delay(100)

# TODO
# continue from here
# http://docs.micropython.org/en/latest/pyboard/tutorial/usb_mouse.html