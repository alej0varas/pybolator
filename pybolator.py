import argparse
import json

import pybgui
import pyboard


parser = argparse.ArgumentParser()
parser.add_argument('--batch', nargs='?', const=True, default=False,
                    type=argparse.FileType('r'), help="""Disable GUI
                    and run main immediately. If a file name is pased
                    it is, used as a script""" )

parser.add_argument('--hardware', type=argparse.FileType('r'),
                    default='pyboard.json', help="""Load a hardware
                    definition from a hardware file""" )


args = parser.parse_args()

hardware = json.loads(args.hardware.read())
board = pyboard._board.init(hardware)


if args.batch:
    script = None
    if not isinstance(args.batch, bool):
        script = args.batch.read()
    board.main(script)
else:
    pybgui.main(board)

