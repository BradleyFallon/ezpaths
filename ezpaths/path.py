"""
Commentary:
This class provides shorthand methods for common os.path functions
The motivation for development that complex one-liners with os.path can be hard to read.
This is intended to make complex one-liners easy to understand without comments.
"""

import os
import sys


class Path:

    # create Path object from pathlike string
    def __init__(self, path_str: str = None):
        if path_str is None:
            path_str = os.getcwd()
        self._path = os.path.abspath(path_str)

    # join paths
    def __add__(self, other):
        return Path(os.path.join(self._path, str(other)))

    # join paths
    def __truediv__(self, other):
        return Path(os.path.join(self._path, str(other)))

    # convert to string
    def __str__(self):
        return self._path

    # represent as string
    def __repr__(self):
        return f"<{self}>"

    # check if path exists
    def __bool__(self):
        return os.path.exists(self._path)

    # Check if abspath is same as other
    def __eq__(self, other):
        return os.path.abspath(self._path) == os.path.abspath(str(other))

    # return parent directory object
    def dir(self, extra=0):
        return (
            self.dir().dir(extra - 1)
            if extra > 0
            else Path(os.path.dirname(self._path))
        )

    # return name of parent directory

    def dirname(self) -> str:
        # check if is file
        if self.ext() == "":
            return self.name()
        else:
            return self.dir().name()

    # return name and extension separately
    def split(self) -> (str, str):
        return os.path.splitext(self._path)

    # return extension
    def ext(self) -> str:
        return self.split()[1]

    # return filename with or without extension
    def name(self) -> str:
        return os.path.basename(self.split()[0])

    # return filename with or without extension
    def filename(self) -> str:
        return os.path.basename(self._path)

    # Append to sys.path
    def to_sys(self):
        return sys.path.insert(0, str(self))
