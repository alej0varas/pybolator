from tkinter import Button, Canvas, DISABLED, Frame, Label, Tk

CONTROL_ROW = 0
BOARD_ROW = CONTROL_ROW + 1
LEDS_COLUMN = 0
SWITCH_COLUMN = LEDS_COLUMN + 1


class LCD:

    COLORS = ['white', 'black']
    PIXEL_SIZE = 2
    SCREEN_SCALE = PIXEL_SIZE + 1

    def __init__(self, app):
        self.app = app
        self.obj = None
        self.master = self.app.master
        self.widget = None
        self.hardware = self.app.hardware.get('LCD')
        self.build()

    def build(self):
        width = self.hardware.get('x') * LCD.SCREEN_SCALE
        height = self.hardware.get('y') * LCD.SCREEN_SCALE
        skin_position = self.hardware.get('skin_position')
        if skin_position == 'Y':
            width, height = height, width
        canvas = Canvas(self.master, width=width, height=height)
        canvas.pack()
        self.widget = canvas

    def update(self):
        if self.app.board.LCD.skin_position is None:
            return
        if self.obj is None and self.hardware is not None:
            self.obj = self.app.board.LCD

        if self.obj._buffer is None:
            return
        if self.obj._buffer.items() == self.obj._hidden_buffer.items():
            return
        for k, v in self.obj._buffer.items():
            x = (k[0] * LCD.SCREEN_SCALE)
            y = (k[1] * LCD.SCREEN_SCALE)
            color = LCD.COLORS[v]
            rectangle = (x, y, x + LCD.PIXEL_SIZE, y + LCD.PIXEL_SIZE)
            self.widget.create_rectangle(rectangle, outline=color, fill=color)


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
        self.board_is_running = False
        self.hardware = board.hardware
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()
        self.board = board
        self.leds = []
        self.init()

    def init(self):
        self.init_LCD()
        self.init_leds()
        self.init_switches()

        b0 = Button(
            self.frame, text="ON!", background="green", command=self.boot_board
        )
        b0.grid(row=CONTROL_ROW, column=0)
        b1 = Button(
            self.frame, text="OFF!", background="red", command=self.stop_board
        )
        b1.grid(row=CONTROL_ROW, column=1)

    def boot_board(self):
        if not self.board_is_running:
            self.board_is_running = True
            self.board.main()

    def stop_board(self):
        self.board_is_running = False
        self.board.stop()

    def init_LCD(self):
        Label(self.frame, text="LCD").grid(row=BOARD_ROW + 1, column=LEDS_COLUMN)
        self.LCD = LCD(self)

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
        if not self.board_is_running:
            return
        for led in self.leds:
            led.update()
        self.LCD.update()


def main(board):
    root = Tk()
    app = App(root, board)

    def update_gui():
        root.after(5, update_gui)
        app.update()

    root.after(0, update_gui)
    root.mainloop()

    board.stop()
