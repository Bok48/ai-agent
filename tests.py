# tests.py

import unittest
from textwrap import dedent
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_directory(self):
        result = get_files_info("calculator", ".")
        print(dedent(
            f"""
            Expected result for current directory:
            - main.py: file_size=719 bytes, is_dir=False
            - tests.py: file_size=1331 bytes, is_dir=False
            - pkg: file_size=44 bytes, is_dir=True
            """
        ))

        print(dedent(
            f"""
            Actual result for current directory:
            {result}
            """
        ))

    def test_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        print(dedent(
            f"""
            Expected result for 'pkg' directory:
            - calculator.py: file_size=1721 bytes, is_dir=False
            - render.py: file_size=376 bytes, is_dir=False
            """
        ))

        print(dedent(
            f"""
            Actual result for 'pkg' directory:
            {result}
            """
        ))

    def test_outside_directory(self):
        result = get_files_info("calculator", "/bin")
        print(dedent(
            f"""
            Expected result for /bin directory:
            Error: Cannot list "/bin" as it is outside the permitted working directory
            """
        ))

        print(dedent(
            f"""
            Actual result for /bin directory:
            {result}
            """
        ))

    def test_outside_directory_2(self):
        result = get_files_info("calculator", "../")
        print(dedent(
            f"""
            Expected result for ../ directory:
            Error: Cannot list "../" as it is outside the permitted working directory
            """
        ))

        print(dedent(
            f"""
            Actual result for ../ directory:
            {result}
            """
        ))


if __name__ == "__main__":
    unittest.main()