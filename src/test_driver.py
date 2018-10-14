#!/usr/bin/env python

import sys

from twt_adapter import TwtStreamer 

def main():
    twt_l.start_streaming()

if __name__ == "__main__":
    twt_l = TwtStreamer()
    sys.exit(main())
