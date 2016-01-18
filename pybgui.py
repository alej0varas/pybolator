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
        self.board.interpreter.write("%s-switch:press" % self.obj._name)

    def release_command(self, event):
        self.board.interpreter.write("%s-switch:release" % self.obj._name)


class App:

    def __init__(self, master, board):
        self.frame = Frame(master)
        self.frame.pack()
        self.board = board
        self.leds = []
        self.init()

    def init(self):
        self.init_leds()
        self.init_switches()

        b0 = Button(
            self.frame, text="ON!", background="green", command=self.board.main
        )
        b0.grid(row=CONTROL_ROW, column=0)
        b1 = Button(
            self.frame, text="OFF!", background="red", command=self.board.stop
        )
        b1.grid(row=CONTROL_ROW, column=1)

    def init_leds(self):
        Label(self.frame, text="Leds").grid(row=BOARD_ROW, column=LEDS_COLUMN)
        count = BOARD_ROW + 1
        for led in self.board.leds.values():
            led_w = Button(self.frame, background="white", state=DISABLED,
                           foreground="black")
            led_w.grid(row=count, column=LEDS_COLUMN)
            count += 1
            led = LED(led, led_w)
            self.leds.append(led)

    def init_switches(self):
        label = Label(self.frame, text="Switches")
        label.grid(row=BOARD_ROW, column=SWITCH_COLUMN)

        # user switch
        switch_w = Button(self.frame, background="black")
        switch_w.grid(row=BOARD_ROW + 1, column=SWITCH_COLUMN)
        Switch(self.board, self.board.switch, switch_w)

        # reset switch
        switch_w = Button(self.frame, background="black", foreground='white',
                          text="reset")
        switch_w.grid(row=BOARD_ROW + 1, column=SWITCH_COLUMN + 1)
        Switch(self.board, self.board.reset, switch_w)

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

    board.stop()
