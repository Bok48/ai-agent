# tests.py

import unittest
from textwrap import dedent
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

class TestGetFilesInfo(unittest.TestCase):
    def test_1(self):
        result = get_file_content("calculator", "main.py")

        print(result)

    def test_2(self):
        result = get_file_content("calculator", "pkg/calculator.py")

        print(result)

    def test_3(self):
        result = get_file_content("calculator", "/bin/cat")

        print(result)

    def test_4(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")

        print(result)



if __name__ == "__main__":
    unittest.main()