__version__ = "2.33.1rc1"

import sys

if sys.argv[-1] == "--get-version":
    print(__version__)
