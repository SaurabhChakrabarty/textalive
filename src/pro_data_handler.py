#!/usr/bin/env python

from fuzzywuzzy import fuzz

class ProDataHandler():
    def __init__(self, file_name=None):
        try:
            if file_name == None:
                raise IOError
            self._f_hndl = open(file_name, 'r')
            self._pro_lst = []
            f_data = None
            f_data = self._f_hndl.readline()
            while f_data != "":
                self._pro_lst.append(f_data.strip('\n'))
                f_data = self._f_hndl.readline()
            self._pro_line = ' '.join(self._pro_lst)
        except IOError:
            raise
    def __del__(self):
        self._f_hndl.close()
    def has_profane(self, data):
        for word in self._pro_lst:
            if fuzz.partial_ratio(word, data) == 100:
                return True
        return False
