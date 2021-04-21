import sys
import os

# Insert local path at 0 so that local module is imported before installed version
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ezpaths import Path

if __name__ == "__main__":
    # Verify that local instance is imported
    import ezpaths

    path_file = Path(ezpaths.__file__)
    path_this = Path(__file__)
    root_file = path_file.dir(2)
    root_this = path_this.dir(2)
    print("path_file: ", path_file)
    print("path_this: ", path_this)
    print("root_file: ", root_file)
    print("root_this: ", root_this)
    assert root_file == root_this
    print("Context is correct.")
