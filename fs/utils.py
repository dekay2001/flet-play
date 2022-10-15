"""
"""
import json as json
import pprint as pprint

class LocalJsonFile:
    def __init__(self, file_path):
        self._file_path = file_path
        self._data = None
        self._read()

    @property
    def content(self):
        return f'{self._data}'
    
    @property
    def pretty_content(self):
        return pprint.pformat(self._data)

    def write(self, key, value):
        self._data[key] = value
        self._write()

    def _read(self):
        with open(self._file_path, 'r') as fp:
            self._data = json.load(fp)

    def _write(self):
        with open(self._file_path, 'w') as fp:
            json.dump(self._data, fp, sort_keys=True, indent=4)