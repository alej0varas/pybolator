import argparse

import pybgui
import pyboard


parser = argparse.ArgumentParser()
parser.add_argument('--batch', nargs='?', const=True, default=False,
                    type=argparse.FileType('r'), help="""Disable GUI
                    and run main immediately. If a file name is pased
                    it is, used as a script""" )

args = parser.parse_args()

board = pyboard._board

if args.batch:
    script = None
    if not isinstance(args.batch, bool):
        script = args.batch.read()
    board.main(script)
else:
    pybgui.main(board)

