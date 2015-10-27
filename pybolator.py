import pyboard
import pybgui

app = pybgui.App(pybgui.root, pyboard)
pyboard.app = app
pybgui.root.mainloop()
