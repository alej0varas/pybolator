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
