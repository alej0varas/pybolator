from tkinter import *

CONTROL_ROW = 0
BOARD_ROW = CONTROL_ROW + 1
LEDS_COLUMN = 0
SWITCH_COLUMN = LEDS_COLUMN + 1


class LED:

   def __init__(self, obj, widget):
      self.obj = obj
      self.widget = widget

   def update(self):
      if self.obj.state:
         print('GUI:LED:ON')
         self.widget.config(background='blue')
      if not self.obj.state:
         print('GUI:LED:OFF')
         self.widget.config(background='white')


class App:

    def delay(self):
        pass

    def __init__(self, master, board):
        self.frame = Frame(master)
        self.frame.pack()
        self.board = board
        self.leds = []
        self.switch = None
        self.init()

    def init(self):
        self.init_leds()
        self.init_switch()

        b0 = Button(
            self.frame, text="RUN!", background="green", command=self.run_code
        )
        b0.grid(row=CONTROL_ROW, column=0)

    def init_leds(self):
        Label(self.frame, text="leds").grid(row=BOARD_ROW, column=LEDS_COLUMN)
        count = BOARD_ROW + 1
        for led in self.board.leds:
            led_w = Button(
                self.frame, background="white", state=DISABLED
            )
            led_w.grid(row=count, column=LEDS_COLUMN)
            count += 1
            led = LED(led, led_w)
            self.leds.append(led)

    def init_switch(self):
        def switch_push():
            self.board.switch._down()

        Label(self.frame, text="switch").grid(row=BOARD_ROW, column=SWITCH_COLUMN)
        switch = Button(
            self.frame, background="black", command=switch_push
            )
        switch.grid(row=BOARD_ROW + 1, column=SWITCH_COLUMN)
        self.switch = switch

    def run_code(self):
        self.board._run_code()

root = Tk()
