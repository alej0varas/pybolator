import argparse

import pybgui
import pyboard


parser = argparse.ArgumentParser()
parser.add_argument('--batch', nargs='?', const=True, default=False,
                    type=argparse.FileType('r'), help="""Disable GUI
                    and run main immediately. If a file name is pased
                    it is, used as a script""" )

args = parser.parse_args()

if args.batch:
    script = None
    if not isinstance(args.batch, bool):
        script = args.batch.read()
    pyboard._main(script)
else:
    pybgui.main(pyboard)

