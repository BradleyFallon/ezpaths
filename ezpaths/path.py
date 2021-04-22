import os
import sys


class Path:
    """This class provides shorthand methods for common os.path functions
    The motivation for development that complex one-liners with os.path can be hard to read.
    This is intended to make complex one-liners easy to understand without comments.
    """

    def __init__(self, path_str: str = None):
        """Constructor method

        :param path_str: The path string to be stored, defaults to None
        :type path_str: str, optional
        """
        if path_str is None:
            path_str = os.getcwd()
        self._path = os.path.abspath(path_str)

    def __add__(self, other) -> 'Path':
        """Creates the joined path appending other (RHS) to self.
        Does not modify self. Same as __truediv__.

        :param other: The path segment to be joined
        :type other: Either a Path or string
        :return: Returns the resulting Path object
        :rtype: Path
        """
        return Path(os.path.join(self._path, str(other)))

    def __truediv__(self, other) -> 'Path':
        """Creates the joined path appending other (RHS) to self.
        Does not modify self. Same as __add__.

        :param other: The path segment to be joined
        :type other: Either a Path or string
        :return: Returns the resulting Path object
        :rtype: Path
        """
        return Path(os.path.join(self._path, str(other)))

    def __str__(self) -> str:
        """Return the stored path string.

        :return: String of target path.
        :rtype: str
        """
        return self._path

    def __repr__(self) -> str:
        """Returns the type and path string in instance brackets.

        :return: String representation of self.
        :rtype: str
        """
        return f"<Path: {self}>"

    def __bool__(self) -> bool:
        """Checks if path exists as either a file or directory.

        :return: True if exists else False.
        :rtype: bool
        """
        return os.path.exists(self._path)

    def __eq__(self, other) -> bool:
        """Checks if the absolute path of self and other are identical.

        :param other: The path to be compared
        :type other: Either a Path or string
        :return: True if identical paths else False
        :rtype: bool
        """
        return os.path.abspath(self._path) == os.path.abspath(str(other))

    def dir(self, extra: int = 0) -> 'Path':
        """Returns path object targeting parent directory of self.

        :param extra: Number of extra levels to ascend recursively, defaults to 0
        :type extra: int, optional
        :return: The parent directory path
        :rtype: Path
        """
        return (
            self.dir().dir(extra - 1)
            if extra > 0
            else Path(os.path.dirname(self._path))
        )

    def dirname(self) -> str:
        """Returns the name of the last directory, with or without file at end of path.

        :return: The name of the last directory in self._path
        :rtype: str
        """
        # If no file, return self.name()
        if self.ext() == "":
            return self.name()
        # If file, get name of parent directory
        else:
            return self.dir().name()

    def split(self) -> (str, str):
        """Return name and extension separately.

        :return: The name and extension of the file.
        :rtype: tuple(name: str, ext: str)
        """
        return os.path.splitext(self._path)

    def ext(self) -> str:
        """Returns just the file extension.

        :return: File extension
        :rtype: str
        """
        return self.split()[1]

    def name(self) -> str:
        """Returns the last file or dir name without extension.

        :return: Last file or dir name
        :rtype: str
        """
        return os.path.basename(self.split()[0])

    def filename(self) -> str:
        """Returns the last file or dir name with extension.

        :return: Last file or dir name
        :rtype: str
        """
        return os.path.basename(self._path)

    def to_sys(self, index: int = 0) -> None:
        """Adds self to sys.path list. Will insert at front by default.
        Inserting at front makes it the first path checked when importing.

        :param index: Index to be inserted at in sys.path list, defaults to 0
        :type index: int, optional
        :return: None
        :rtype: None
        """
        return sys.path.insert(0, str(self))
