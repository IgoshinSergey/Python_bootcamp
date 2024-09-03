import unittest
from unittest.mock import patch
import io
import sys
import os
import shortest_path


class TestLength(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_length(self, mock_stdout):
        del sys.argv[:]
        sys.argv = ["shortest_path.py", "-v"]
        shortest_path.main()
        del sys.argv[:]
        self.assertEqual(mock_stdout.getvalue(), "length: 3\n")


class TestLength2(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_length(self, mock_stdout):
        del sys.argv[:]
        sys.argv = [
            "shortest_path.py",
            "-v",
            "--from",
            "Abdus Salam",
            "--to",
            "Military deployment",
        ]
        shortest_path.main()
        del sys.argv[:]
        self.assertEqual(mock_stdout.getvalue(), "length: 3\n")


class TestNonDirected(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_length(self, mock_stdout):
        del sys.argv[:]
        sys.argv = [
            "shortest_path.py",
            "-v",
            "--from",
            "Erdős number",
            "--to",
            "Hans Georg Dehmelt",
            "--non-directed",
        ]
        shortest_path.main()
        del sys.argv[:]
        self.assertEqual(mock_stdout.getvalue(), "length: 3\n")

class TestDirected(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_length(self, mock_stdout):
        del sys.argv[:]
        sys.argv = [
            "shortest_path.py",
            "--from",
            "Erdős number",
            "--to",
            "Hans Georg Dehmelt",
            "-v",
        ]
        shortest_path.main()
        del sys.argv[:]
        self.assertEqual(mock_stdout.getvalue(), "length: 4\n")


if __name__ == "__main__":
    os.environ["WIKI_FILE"] = "result.json"
    unittest.main()
