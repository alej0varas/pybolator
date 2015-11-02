import sys

from tkinter import Button, DISABLED, Frame, Label, Tk

CONTROL_ROW = 0
BOARD_ROW = CONTROL_ROW + 1
LEDS_COLUMN = 0
SWITCH_COLUMN = LEDS_COLUMN + 1


class LED:

    def __init__(self, obj, widget):
        self.obj = obj
        self.widget = widget

    def update(self):
        background='white'
        if self.obj._intensity:
            background = self.obj._color
        text = '%03d' % self.obj._intensity

        self.widget.config(text=text, background=background)


class Switch:

    def __init__(self, board, obj, widget):
        self.board = board
        self.obj = obj
        self.widget = widget
        self.widget.bind("<Button-1>", self.press_command)
        self.widget.bind("<ButtonRelease-1>", self.release_command)

    def press_command(self, event):
        self.board._interpreter.write("switch:press")

    def release_command(self, event):
        self.board._interpreter.write("switch:release")


class App:

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
        for led in self.board._leds:
            led_w = Button(self.frame, background="white", state=DISABLED,
                           foreground="black")
            led_w.grid(row=count, column=LEDS_COLUMN)
            count += 1
            led = LED(led, led_w)
            self.leds.append(led)

    def init_switch(self):
        label = Label(self.frame, text="switch")
        label.grid(row=BOARD_ROW, column=SWITCH_COLUMN)
        switch_w = Button(self.frame, background="black")
        switch_w.grid(row=BOARD_ROW + 1, column=SWITCH_COLUMN)
        switch = Switch(self.board, self.board._switch, switch_w)
        self.switch = switch

    def run_code(self):
        self.board._main()
        # self.load_script()

    def update(self):
        for led in self.leds:
            led.update()


def main(board):
    root = Tk()
    app = App(root, board)

    def update_gui():
        root.after(500, update_gui)
        app.update()

    root.after(0, update_gui)
    root.mainloop()
