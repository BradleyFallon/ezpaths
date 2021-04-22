import unittest
import os
import sys

from .context import Path


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


if __name__ == "__main__":
    unittest.main()
