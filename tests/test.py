import unittest
import os
import sys

from .context import Path
from datetime import datetime

def timestamp(): return datetime.now().strftime("%y%m%d_%H%M%S")

class TestPath(unittest.TestCase):
    def test_init_empty(self):
        self.assertEqual(str(Path()), os.getcwd())

    def test_init_full(self):
        path_str = "/root/dir/file.ext"
        self.assertEqual(str(Path(path_str)), os.path.abspath(path_str))

    def test_init_name(self):
        path_str = "file.ext"
        self.assertEqual(str(Path(path_str)), os.getcwd() + os.sep + path_str)

    def test_repr(self):
        path = Path()
        self.assertEqual(repr(path), "<Path: " + str(path) + ">")

    def test_add(self):
        path_a = Path()
        dirname = "dir"
        self.assertEqual(str(Path() + dirname), str(Path()) + os.sep + dirname)

    def test_truediv(self):
        path_a = Path()
        dirname = "dir"
        self.assertEqual(str(Path() / dirname), str(Path()) + os.sep + dirname)

    def test_exists_bool_dir(self):
        self.assertTrue(Path())

    def test_exists_bool_dir_false(self):
        path = Path() / "test" / "test" / "test"
        self.assertFalse(path)

    def test_exists_bool_file(self):
        self.assertTrue(Path(__file__))

    def test_recursive_dir(self):
        self.assertEqual(Path().dir().dir(), Path().dir(1))

    def test_dirname_dir(self):
        dirname = "dirname"
        path = Path() / dirname
        self.assertEqual(dirname, path.dirname())

    def test_dirname_file(self):
        dirname = "dirname"
        filename = "file.ext"
        path = Path() / dirname / filename
        self.assertEqual(dirname, path.dirname())

    def test_filename_file(self):
        filename = "file.ext"
        path = Path() / filename
        self.assertEqual(filename, path.filename())

    def test_ext_file(self):
        path = Path() / "file.ext"
        self.assertEqual(path.ext(), ".ext")

    def test_sys_path(self):
        path = Path() / "test" / "test" / "test"
        missing_before = path not in sys.path
        path.to_sys()
        present_now = path in sys.path
        self.assertTrue(present_now and missing_before)

    def test_touch(self):
        fname = timestamp() + "_test_touch.txt"
        path = Path() + fname
        self.assertFalse(path.exists())
        path.touch()
        self.assertTrue(path.exists())
        path.delete()

    def test_delete(self):
        fname = timestamp() + "_test_delete.txt"
        path = Path() + fname
        self.assertFalse(path.exists())
        path.touch()
        self.assertTrue(path.exists())
        path.delete()
        self.assertFalse(path.exists())

    def test_rename(self):
        fname_before = timestamp() + "_test_rename_before.txt"
        fname_after = timestamp() + "_test_rename_before.txt"
        path = Path() + fname_before
        if path.exists():
            # Was already taken, fail test
            self.fail()
        path.touch()
        if not path.exists():
            self.fail()
        path_destination = Path() + fname_after
        missing_before = path_destination.exists()
        path_old = Path(str(path))
        path.rename(fname_after)
        present_now = path_destination.exists()
        old_removed = path_old.exists()
        path.delete()
        print(path_destination)
        print(path)
        self.assertTrue(path_destination == path)
        self.assertTrue(present_now)
        self.assertTrue(old_removed)


if __name__ == "__main__":
    unittest.main()
