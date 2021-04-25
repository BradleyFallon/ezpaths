import os
import shutil

from .path import Path


class File:
    """ This class provides methods to handle file level operations such as
    copy, move, delete, and read-write access to files
    """

    def __init__(self, path_str: str):
        """Constructor method

        :param path_str: The path string to be stored, defaults to None
        :type path_str: str
        """
        self.path = Path(path_str)
        self._contents = None

    def copy(self, dest_path_str: str=None, suffix: str="_copy"):
        """Copies this file to the given destination path.

        :param dest_path_str: The destination path this file needs to be copied to. If None, a new copy with the suffix is created in the same location.
        :type dest_path_str: str
        :param suffix: Suffix of the copied file when the same filename exists in the destination folder. Defaults to "_copy".
        :type suffix:
        :return: True if the file has been successfully deleted, False otherwise.
        :rtype: bool
        """
        try:
            shutil.copyfile(self.path._path, dest_path_str)

        except shutil.SameFileError:
            pass


    def move(self):
        pass

    def delete(self) -> bool:
        """Deletes this file from the disk

        :return: True if the file has been successfully deleted, False otherwise.
        :rtype: bool
        """
        if self.path:   # TODO: Does this call Path.__bool__() ?
            os.remove(self.path._path)
            return True

        return False

    def read(self):
        pass

    def write(self):
        pass
