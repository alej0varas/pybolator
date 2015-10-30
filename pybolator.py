import argparse

import pybgui
import pyboard


parser = argparse.ArgumentParser()
parser.add_argument('--batch', action='store_true', default=False,
                    help="Disable GUI and run main immediately")
args = parser.parse_args()

if not args.batch:
    pybgui.main(pyboard)
else:
    pyboard._main()
