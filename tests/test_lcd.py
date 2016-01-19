import pyb

txt = 'Hello World!'
for sp in ['X', 'Y']:
    for color in [0, 1]:
        lcd = pyb.LCD(sp)
        lcd.text(txt, 0, 0, color)

assert lcd.get(0, 0) == 0

lcd.light(True)                 # turn the backlight on
lcd.write('Hello world!\n')     # print text to the screen

x = y = 0
dx = dy = 1
for i in range(10):
    # update the dot's position
    x += dx
    y += dy

    # make the dot bounce of the edges of the screen
    if x <= 0 or x >= 127: dx = -dx
    if y <= 0 or y >= 31: dy = -dy

    lcd.fill(0)                 # clear the buffer
    lcd.pixel(x, y, 1)          # draw the dot
    lcd.show()                  # show the buffer
    pyb.delay(50)               # pause for 50ms

assert lcd.get(0, 0) == 0
lcd.pixel(0, 0, 1)
lcd.show()
assert lcd.get(0, 0) == 1

lcd.contrast(0)
lcd.contrast(47)

# lcd.command(self, instr_data, buf)
