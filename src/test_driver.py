#!/usr/bin/env python

import sys

from data_injester import DataInjester
from pro_data_handler import ProDataHandler

def main():
    line = injester.get_line()
    while line != "":
        if prof.has_profane(line):
            print "PRO"
        line = injester.get_line()
        #print line

if __name__ == "__main__":
    DATA_FILE = "../data/sample.txt"
    PRO_FILE = "../data/prof.txt"
    injester = DataInjester(DATA_FILE)
    prof = ProDataHandler(PRO_FILE)
    sys.exit(main())
