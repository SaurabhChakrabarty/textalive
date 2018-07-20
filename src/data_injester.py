#!/usr/bin/env

class DataInjester():
    def __init__(self, file_name):
        self._file_name = file_name
        try:
            self._f_hndl = open(file_name, 'r')
            if self._f_hndl < 0:
                raise IOError
        except IOError:
            raise
    def __del__(self):
        if self._f_hndl > 0:
            self._f_hndl.close()
    def get_line(self):
        line = self._f_hndl.readline()
        return line
