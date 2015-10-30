import pyb

# This code can be run on your pyboard without modifications

# ##########
# # Switch #
# ##########

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

while True:
    pass
