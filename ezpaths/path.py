import os
import sys
import shutil


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

    def delete(self) -> bool:
        """Deletes this file from the disk

        :return: True if the file has been successfully deleted, False otherwise.
        :rtype: bool
        """
        if os.path.isfile(self._path):
            os.remove(self._path)
            return True

        elif os.path.isdir(self._path):
            shutil.rmtree(self._path)
            return True

        return False

    def rename(self, new_name: str) -> bool:
        """New name for the file or the directory in the path

        :param new_name: New name for the filename.
        :type new_name: str
        :return: True if the file has been successfully renamed, False otherwise.
        :rtype: bool
        """
        if not new_name or not isinstance(new_name, str):
            return False

        self._path = os.path.join(
            self.dir()._path,
            "{}{}".format(new_name, self.ext()),
        )

        return True

    def copy(self, destination: "Path"=None, suffix: str="copy") -> "Path":
        """Copies this file/folder to the given destination path.

        :param destination: The destination path this file needs to be copied to. If None, a new copy with the suffix is created in the same location.
        :type destination: Path, optional
        :param suffix: Suffix of the copied file when the same filename exists in the destination folder. Defaults to "copy".
        :type suffix:
        :return: Path instance of the destination.
        :rtype: Path
        """
        if isinstance(destination, str):
            destination = Path(destination)

        elif destination is None:
            destination = Path(self._path)
            destination.rename("{}_{}".format(destination.name(), suffix))

        # Copy the file/directory
        if os.path.isfile(self._path):
            dest_path_str = shutil.copy2(self._path, destination._path)

        elif os.path.isdir(self._path):
            dest_path_str = shutil.copytree(self._path, destination._path, copy_function=shutil.copy2)

        # Sanity check
        assert dest_path_str == destination._path

        return destination

    def move(self, destination: "Path") -> "Path":
        """Moves this file or folder to the given destination

        :param destination: Path to be moved to.
        :type destination: Path.
        :return: Path instance of the moved file/folder. None if failed.
        :rtype: Path
        """
        if not destination:
            print("Incorrect destination path provided.")
            return None

        if isinstance(destination, str):
            destination = Path(destination)

        # Move the file/folder
        dest_str_path = shutil.move(self._path, destination._path)

        # Sanity check
        assert dest_str_path == destination._path
        self._path = destination._path  # TODO: Is this necessary?

        return destination

    def mkdirs(self) -> "Path":
        """Creates a directory recursively. That means while making leaf
        directory if any intermediate-level directory is missing, this
        method will create them all.

        :return: True if successful, False otherwise.
        :rtype: bool
        """
        if not os.path.exists(self._path):
            os.makedirs(self._path)
            return True

        return False

    def touch(self) -> bool:
        """Implement the touch feature for this Path

        :return: True always.
        :rtype: bool
        """
        with open(self._path, 'a'):
            os.utime(self._path, None)

        return True
